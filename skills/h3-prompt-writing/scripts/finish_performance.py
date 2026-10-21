#!/usr/bin/env python3
"""Local deterministic two-frame exposure and single-placement cue audio.
No generation, interpolation, time stretching, overwrite, or live app changes.
"""
import argparse,json,re,shutil,subprocess,tempfile,wave
from pathlib import Path

def ffmpeg():
 p=shutil.which('ffmpeg')
 if p:return p
 try:
  import imageio_ffmpeg
  return imageio_ffmpeg.get_ffmpeg_exe()
 except ImportError:raise SystemExit('Install FFmpeg or imageio-ffmpeg before rendering.')

def run(args,**kw):
 r=subprocess.run([ffmpeg(),'-hide_banner','-loglevel','error',*map(str,args)],capture_output=True,**kw)
 if r.returncode:raise RuntimeError(r.stderr.decode(errors='replace')[-4000:])
 return r.stdout

def duration(path):
 r=subprocess.run([ffmpeg(),'-hide_banner','-i',str(path)],capture_output=True)
 m=re.search(rb'Duration: (\d+):(\d+):(\d+(?:\.\d+)?)',r.stderr)
 if not m:raise ValueError(f'Cannot determine duration: {path}')
 return int(m[1])*3600+int(m[2])*60+float(m[3])

def normalized_audio(path,out):
 run(['-i',path,'-vn','-ar','48000','-ac','2','-c:a','pcm_s16le',out])
 with wave.open(str(out),'rb') as w:return w.getnframes()/w.getframerate()

def render(video,output,manifest=None,bed=None,cadence_only=False,duration_seconds=None):
 video=Path(video).resolve();output=Path(output).resolve()
 if not video.is_file():raise ValueError('Input video is missing')
 if output.exists() or output==video:raise ValueError('Output must be a new file; existing takes are never overwritten')
 if output.suffix.lower() not in {'.mp4','.mkv'}:raise ValueError('Output must be .mp4 or .mkv')
 if cadence_only and (manifest or bed):raise ValueError('Cadence-only cannot also replace audio')
 if not cadence_only and not manifest:raise ValueError('Audio replacement requires a cue manifest')
 plan=json.loads(Path(manifest).read_text()) if manifest else {'duration':duration_seconds or duration(video),'cues':[]}
 total=float(plan['duration']);frames=round(total*20)
 if total<=0 or abs(frames/20-total)>1e-6 or frames%2:raise ValueError('Duration must contain complete two-frame exposures at 20 fps')
 if duration(video)+.02<total:raise ValueError('Input video is shorter than the requested duration; refusing frozen padding')
 with tempfile.TemporaryDirectory(prefix='stone-age-finish-') as temp:
  temp=Path(temp);args=['-i',str(video)];filters=[];audio_labels=[];index=1
  if not cadence_only:
   ids=set()
   if bed:
    norm=temp/'bed.wav';d=normalized_audio(Path(bed).resolve(),norm)
    if d+.001<total:raise ValueError('Clean bed must cover the whole segment; no looping is added')
    args+=['-i',str(norm)];filters.append(f'[{index}:a]atrim=duration={total},asetpts=PTS-STARTPTS[bed]');audio_labels.append('[bed]');index+=1
   for cue in plan['cues']:
    if cue['id'] in ids:raise ValueError('Duplicate utterance ID: '+cue['id'])
    ids.add(cue['id']);start=float(cue['start']);end=float(cue['end'])
    if not 0<=start<end<=total:raise ValueError('Cue outside segment: '+cue['id'])
    p=(Path(manifest).parent/cue['audio_file']).resolve()
    if not p.is_file():raise ValueError('Missing recorded cue: '+str(p))
    norm=temp/f'cue-{index}.wav';d=normalized_audio(p,norm)
    if d>end-start+.001:raise ValueError(f'{cue["id"]}: recording is {d:.3f}s but window is {end-start:.3f}s; re-record or edit timing. No truncation/time stretching applied.')
    args+=['-i',str(norm)];label=f'a{index}';filters.append(f'[{index}:a]adelay={round(start*48000)}S:all=1,apad,atrim=duration={total}[{label}]');audio_labels.append(f'[{label}]');index+=1
   if audio_labels:
    filters.append(''.join(audio_labels)+f'amix=inputs={len(audio_labels)}:duration=longest:normalize=0,atrim=duration={total}[mix]')
   else:filters.append(f'anullsrc=r=48000:cl=stereo,atrim=duration={total}[mix]')
  # fps resampling selects real poses at 10 Hz and duplicates each to 20 Hz;
  # neither filter synthesizes motion or changes wall-clock speed.
  filters.insert(0,f'[0:v]setpts=PTS-STARTPTS,fps=10:start_time=0:round=down:eof_action=pass,fps=20:start_time=0:round=down:eof_action=pass,trim=duration={total}[v]')
  args+=['-filter_complex',';'.join(filters),'-map','[v]']
  args+=['-map','0:a?'] if cadence_only else ['-map','[mix]']
  args+=['-t',str(total),'-fps_mode','cfr','-r','20']
  if output.suffix.lower()=='.mkv':args+=['-c:v','ffv1','-c:a','pcm_s16le']
  else:args+=['-c:v','libx264','-crf','0','-preset','fast','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart']
  run([*args,'-n',output])
 report={'input':str(video),'output':str(output),'duration':total,'fps':20,'exposureFrames':2,'audioMode':'native retained (repetition not repaired)' if cadence_only else 'source audio discarded; supplied stems placed once','cueCount':0 if cadence_only else len(plan['cues']),'limits':'Cadence conforming cannot repair bad poses, morphing, camera movement, lip sync or incorrect actions. Cue recordings require human audio/content review.'}
 output.with_suffix(output.suffix+'.json').write_text(json.dumps(report,indent=2));return report

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--video',required=True);p.add_argument('--output',required=True);p.add_argument('--manifest');p.add_argument('--clean-bed');p.add_argument('--cadence-only',action='store_true');p.add_argument('--duration',type=float)
 a=p.parse_args();print(json.dumps(render(a.video,a.output,a.manifest,a.clean_bed,a.cadence_only,a.duration),indent=2))
if __name__=='__main__':main()
