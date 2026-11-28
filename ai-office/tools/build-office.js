// Build ai-office/office.html: the test office (team.html) as ONE file you can open by double-clicking,
// with every bot instruction, knowledge and test file inside it. Opened this way it runs on DeepSeek.
// Run after changing team.html or any file in agents/, knowledge/, templates/ or tests/:
//   node ai-office/tools/build-office.js
const fs = require('fs'), path = require('path');
const base = path.join(__dirname, '..');
const files = {};
for (const dir of ['agents', 'knowledge', 'templates']) {
  for (const f of fs.readdirSync(path.join(base, dir)).sort()) {
    if (f.endsWith('.md') || f.endsWith('.json')) files[dir + '/' + f] = fs.readFileSync(path.join(base, dir, f), 'utf8');
  }
}
files['tests/customer-service-tests.json'] = fs.readFileSync(path.join(base, 'tests', 'customer-service-tests.json'), 'utf8');
// the latest daily news checks (written by the daily task), so the China version sees them too
const intelDir = path.join(base, 'intel');
if (fs.existsSync(intelDir)) fs.readdirSync(intelDir).filter(f => f.endsWith('.json')).sort().slice(-3).forEach(f => { files['intel/' + f] = fs.readFileSync(path.join(intelDir, f), 'utf8'); });
// office pictures, inlined as data URLs so the file works on its own
(function walk(dir, rel) {
  for (const f of fs.readdirSync(dir).sort()) {
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory()) walk(full, rel + f + '/');
    else if (f.endsWith('.jpg')) files['images/' + rel + f] = 'data:image/jpeg;base64,' + fs.readFileSync(full).toString('base64');
  }
})(path.join(base, 'images'), '');

const page = fs.readFileSync(path.join(base, 'team.html'), 'utf8');
const bundle = '<script type="application/json" id="bundle">' + JSON.stringify(files).replace(/</g, '\\u003c') + '</script>\n';
const at = page.indexOf('<script>');
// three.js (MIT) goes inside the file so the 3D office works offline and in mainland China
const three = fs.readFileSync(path.join(base, '..', 'vendor', 'three.min.js'), 'utf8');
if (three.includes('</script')) throw new Error('three.min.js contains a closing script tag');
if (at < 0) throw new Error('team.html has no <script> block');
const out = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">' +
  '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">' +
  '<style>body{margin:0}[hidden]{display:none!important}</style></head><body>\n' +
  page.slice(0, at) + '<script>' + three + '</script>\n' + bundle + page.slice(at) + '\n</body></html>\n';
fs.writeFileSync(path.join(base, 'office.html'), out);
console.log(`Built office.html (${Math.round(out.length / 1024)} KB, ${Object.keys(files).length} files inside)`);
// demo.html: the same office with prepared answers (ai-office/demo/script.json) for showing without an AI key
const demoFiles = Object.assign({}, files, { 'demo/script.json': fs.readFileSync(path.join(base, 'demo', 'script.json'), 'utf8') });
const demoBundle = '<script type="application/json" id="bundle">' + JSON.stringify(demoFiles).replace(/</g, '\\u003c') + '</script>\n';
const demo = out.replace(bundle, () => demoBundle).replace('<html lang="en"><head>', '<html lang="zh-CN"><head><title>Glostudy AI Office · Demo</title>')
  // the demo runs fully offline, even when opened inside Claude: no shared storage, no AI calls
  .replace('var IN_CLAUDE = !!window.claude;', 'var IN_CLAUDE = false;');
fs.writeFileSync(path.join(base, 'demo.html'), demo);
console.log(`Built demo.html (${Math.round(demo.length / 1024)} KB)`);
