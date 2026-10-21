import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const errors = [];
const read = file => fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, '');
const digest = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const walk = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
  const file = path.join(dir, entry.name);
  return entry.isDirectory() ? walk(file) : [file];
});
const config = JSON.parse(read(path.join(root, 'global/director-contract.json')));
if (config.activeContract !== 'v9' || Object.keys(config.profiles).join(',') !== 'v9') {
  errors.push('Director v9 must be the only active and available profile');
}
const profile = config.profiles.v9;
if (!profile || profile.directorSkillId !== 'director-pack-skills' ||
    !fs.existsSync(path.join(root, profile.contract ?? 'missing-contract'))) {
  errors.push('Missing v9 contract or Director skill mapping');
}

// Preserve the historical v9 snapshot without treating later repairs as old bytes.
const manifestPath = path.join(root, config.baseline);
const baseline = JSON.parse(read(manifestPath));
for (const entry of baseline.files) {
  const file = path.join(path.dirname(manifestPath), entry.path);
  if (!fs.existsSync(file) || digest(file) !== entry.sha256) {
    errors.push(`Saved v9 baseline changed: ${entry.path}`);
  }
}
const schemaPath = 'global/skills/director-pack-skills/references/package-schema.md';
const schema = baseline.files.find(entry => entry.path === schemaPath);
// Approved direction-only correction; importer fields and examples remain unchanged.
const normalizedText = file => read(file).replace(/\r\n/g, '\n')
  .replace("If the micro-shot has no structured dialogue, write a visible hold or reaction.", "If the micro-shot has no structured dialogue, direct its authored visible action without spoken words. Silence does not require stillness; a physical hold or reaction must be explicitly motivated by the shot.")
  .replace("\nFor action timing, support/contact transitions and storyboard temporal roles, apply [action physics and timing](action-physics-and-timing.md). Preserve existing fields and distinguish motion review from schema acceptance.\n", '')
  .trimEnd();
if (!schema || normalizedText(path.join(root, schemaPath)) !==
    normalizedText(path.join(path.dirname(manifestPath), schemaPath))) {
  errors.push('The v9 importer schema differs from the preserved baseline');
}

const files = ['skills', 'global/skills'].flatMap(dir => walk(path.join(root, dir)))
  .filter(file => file.endsWith('.md'));
let links = 0;
let entrypoints = 0;
const portableNames = new Set();
for (const file of files) {
  const relative = path.relative(root, file);
  const text = read(file);
  for (const match of text.matchAll(/\]\(([^\s)]+)\)/g)) {
    const target = match[1];
    if (/^(https?:|#)/.test(target)) continue;
    links++;
    if (!fs.existsSync(path.resolve(path.dirname(file), target.split('#')[0]))) {
      errors.push(`${relative}: broken link ${target}`);
    }
  }
  if (path.basename(file) !== 'SKILL.md') continue;
  entrypoints++;
  const match = text.replace(/\r\n/g, '\n').match(/^---\n([\s\S]*?)\n---/);
  if (!match) { errors.push(`${relative}: no frontmatter`); continue; }
  const fields = [...match[1].matchAll(/^([a-z-]+):\s*(.*)$/gm)];
  const values = new Map(fields.map(item => [item[1], item[2]]));
  const name = values.get('name') ?? '';
  const description = values.get('description') ?? '';
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name) || name.length > 64) {
    errors.push(`${relative}: invalid name`);
  }
  if (!description || description.length > 1024 || /[<>]/.test(description)) {
    errors.push(`${relative}: invalid description`);
  }
  if (fields.length !== values.size) errors.push(`${relative}: duplicate frontmatter key`);
  for (const key of values.keys()) {
    if (!['name', 'description', 'metadata', 'allowed-tools', 'license'].includes(key)) {
      errors.push(`${relative}: unexpected frontmatter key ${key}`);
    }
  }
  if (/^\s*\[TODO:/m.test(text)) errors.push(`${relative}: unfinished scaffold`);
  if (relative.startsWith(`skills${path.sep}`)) {
    if (portableNames.has(name)) errors.push(`${relative}: duplicate portable skill name`);
    portableNames.add(name);
  }
}
console.log(JSON.stringify({ valid: errors.length === 0, activeContract: config.activeContract,
  entrypoints, portableSkills: [...portableNames].sort(), markdownFiles: files.length,
  localLinks: links, savedBaselineFiles: baseline.files.length,
  frontmatter: 'small-subset structural validation; run the skill validator for full YAML checks', errors }, null, 2));
if (errors.length) process.exitCode = 1;
