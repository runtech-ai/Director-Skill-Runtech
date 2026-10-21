#!/usr/bin/env python3
"""Verify decoded 20 fps two-frame exposures, not container FPS alone."""
import argparse
import json
from fractions import Fraction
from pathlib import Path
try:
 from finish_performance import run
except ImportError:
 from finish_performance_20fps import run

def verify(video, expected_duration=None):
 text=run(['-i',str(video),'-map','0:v:0','-an','-fps_mode','passthrough','-f','framemd5','-']).decode()
 tb=None; frames=[]
 for line in text.splitlines():
  if line.startswith('#tb 0:'):tb=Fraction(line.split(':',1)[1].strip())
  elif line and not line.startswith('#'):
   parts=[x.strip() for x in line.split(',')]
   frames.append((int(parts[2]),int(parts[3]),parts[5]))
 errors=[]
 if len(frames)<2 or len(frames)%2:errors.append('Incomplete two-frame exposure')
 if tb is None or any(Fraction(d)*tb!=Fraction(1,20) for _,d,_ in frames):errors.append('Frame durations are not 1/20 second')
 if tb and any((b[0]-a[0])*tb!=Fraction(1,20) for a,b in zip(frames,frames[1:])):errors.append('Nonuniform frame timestamps')
 failed=[i for i in range(0,len(frames)-1,2) if frames[i][2]!=frames[i+1][2]]
 if failed:errors.append('Unequal decoded frame pairs')
 actual=float((frames[-1][0]+frames[-1][1]-frames[0][0])*tb) if frames and tb else 0
 if expected_duration is not None and abs(actual-expected_duration)>1e-6:errors.append('Duration mismatch')
 result={'video':str(Path(video).resolve()),'passed':not errors,'frames':len(frames),'duration':actual,'unequalPairs':len(failed),'firstUnequalPairFrames':failed[:12],'errors':errors,'scope':'Decoded cadence only; does not approve performance, lips, props or camera. A static clip can pass.'}
 return result

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('video');p.add_argument('--duration',type=float);a=p.parse_args()
 r=verify(a.video,a.duration);print(json.dumps(r,indent=2));raise SystemExit(0 if r['passed'] else 1)
