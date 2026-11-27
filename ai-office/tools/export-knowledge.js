// Export the school/university data and UK routes from v2-pro/index.html into
// knowledge-base files the bots can use. Run: node ai-office/tools/export-knowledge.js
// Re-run whenever the site's explorer data changes.
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = path.join(__dirname, '..', '..');
const html = fs.readFileSync(path.join(root, 'v2-pro', 'index.html'), 'utf8');
function grab(start, end) {
  const a = html.indexOf(start), b = html.indexOf(end, a);
  if (a < 0 || b < 0) throw new Error('Could not find ' + start);
  return html.slice(a, b);
}
const ctx = {};
vm.runInNewContext(grab('var D = [', 'var st = {') + ';this.out={D,QS,GU,SUBJ,SR,QSR,NAT,KIND};', ctx);
vm.runInNewContext(grab('var PATHS = [', '\n  ];') + '\n  ];this.paths=PATHS;', ctx);
const { D, QS, GU, SUBJ, SR, QSR, NAT, KIND } = ctx.out;
const out = path.join(__dirname, '..', 'knowledge');

// 1. One CSV row per school/university (good for Coze / Dify table knowledge)
const esc = v => /[",\n]/.test(String(v)) ? '"' + String(v).replace(/"/g, '""') + '"' : String(v);
const head = ['name_en', 'name_zh', 'type', 'nation', 'city', 'qs_world_2027', 'guardian_uk_2027', 'guardian_subject_positions', 'qs_subject_positions_2026', 'official_site'];
const rows = D.map(d => {
  const gs = SUBJ.filter(s => SR[s[0]] && SR[s[0]][d[0]]).map(s => s[1] + ' #' + SR[s[0]][d[0]]).join('; ');
  const qs = SUBJ.filter(s => QSR[s[0]] && QSR[s[0]][d[0]]).map(s => s[1] + ' #' + QSR[s[0]][d[0]]).join('; ');
  return [d[0], d[1], KIND[d[2]][0] + ' / ' + KIND[d[2]][1], NAT[d[3]][0] + ' / ' + NAT[d[3]][1], d[4], QS[d[0]] || '', GU[d[0]] || '', gs, qs, d[7]];
});
fs.writeFileSync(path.join(out, 'schools-universities.csv'), '﻿' + [head, ...rows].map(r => r.map(esc).join(',')).join('\n') + '\n');

// 2. The same data as Markdown, one section per institution (good for text knowledge bases: each section is one chunk)
let md = '# 英国学校与大学资料库 · UK schools and universities\n\n' +
  '来源：寰学 Glostudy 官网「探索英国学校与大学」。这是入门参考，不是排名，也不是合作名单；寰学与这些学校没有隶属关系。入学要求、年龄和寄宿安排以各校官网为准。\n' +
  'Rankings: QS World University Rankings 2027 (world, top 100 only); The Guardian University Guide 2027 (UK, out of 123; subject tables); QS World University Rankings by Subject 2026 (world).\n\n';
D.forEach((d, i) => {
  const r = rows[i];
  md += `## ${d[0]}${d[1] ? '（' + d[1] + '）' : ''}\n` +
    `- 类型 Type: ${r[2]}\n- 地区 Location: ${d[4]}, ${r[3]}\n` +
    (r[5] ? `- QS 世界排名 2027: #${r[5]}\n` : '') + (r[6] ? `- 《卫报》英国排名 2027: #${r[6]} / 123\n` : '') +
    (r[7] ? `- 《卫报》学科排名 2027: ${r[7]}\n` : '') + (r[8] ? `- QS 学科排名 2026: ${r[8]}\n` : '') +
    `- 官网 Official site: ${d[7]}\n\n`;
});
fs.writeFileSync(path.join(out, 'schools-universities.md'), md);

// 3. UK routes (GCSE, A-level, foundation, UG, PG...) in Chinese and English
let pm = '# 英国升学路径 · Routes into UK education\n\n各阶段简要介绍，具体要求以各校公布为准。Every school sets its own requirements.\n\n';
ctx.paths.forEach(p => {
  pm += `## ${p.title.zh} · ${p.title.en}（${/\d/.test(p.age) ? p.age + ' 岁' : '不限年龄 · any age'}）\n${p.intro.zh}\n${p.intro.en}\n\n`;
  p.rows.forEach(r => { pm += `- ${r.zh[0]}：${r.zh[1]} · ${r.en[0]}: ${r.en[1]}\n`; });
  pm += `\n${p.fit.zh}\n${p.fit.en}\n\n`;
});
fs.writeFileSync(path.join(out, 'uk-routes.md'), pm);
console.log(`Exported ${D.length} institutions and ${ctx.paths.length} routes to ${out}`);
