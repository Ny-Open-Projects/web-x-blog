// 课程25 审核流水线 · 实时进度面板（无依赖 node http server，只读扫描）
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..'); // target/25-lowcode
const REPORTS = path.join(ROOT, 'reports');
const BATCHES = [
  ['b1', '批1 预先课 40 篇', 'review-b1-pre.md'],
  ['b2', '批2 第一期 24 篇', 'review-b2-p1.md'],
  ['b3', '批3 第二期 26 篇', 'review-b3-p2.md'],
  ['b4', '批4 第三期 23 篇', 'review-b4-p3.md'],
  ['b5', '批5 第四期 24 篇', 'review-b5-p4.md'],
  ['b6', '批6 第五期 26 篇', 'review-b6-p5.md'],
  ['b7', '批7 第六期 25 篇', 'review-b7-p6.md'],
  ['b8', '批8 第七期 22 篇', 'review-b8-p7.md'],
  ['b9', '批9 第八期 19 篇', 'review-b9-p8.md'],
  ['b10', '批10 知识卡 35 张', 'review-b10-cards.md'],
  ['engA', '工程审计-A 自研版', 'review-eng-a.md'],
  ['engB', '工程审计-B 课程原版', 'review-eng-b.md'],
];
const FINAL = ['review-final.md', 'apply-review.md'];

function statSafe(p) { try { const s = fs.statSync(p); return { size: s.size, mtime: s.mtime }; } catch { return null; } }

function countSev(file) {
  try {
    const t = fs.readFileSync(file, 'utf8');
    return { p0: (t.match(/P0/g) || []).length, p1: (t.match(/P1/g) || []).length, p2: (t.match(/P2/g) || []).length };
  } catch { return null; }
}

function collect() {
  const now = new Date().toISOString().replace('T', ' ').slice(0, 19);
  const batches = BATCHES.map(([id, name, file]) => {
    const p = path.join(REPORTS, file);
    const s = statSafe(p);
    return { id, name, file, status: s ? '✅ 完成' : '… 未产出/进行中', size: s ? s.size : 0, mtime: s ? s.mtime.toISOString().slice(11, 19) : '', sev: countSev(p) };
  });
  const finals = FINAL.map(f => ({ file: f, ...statSafe(path.join(REPORTS, f)) ? '✅' : '—' }));
  const counts = {
    reports: fs.existsSync(REPORTS) ? fs.readdirSync(REPORTS).filter(f => f.endsWith('.md')).length : 0,
    cards: fs.existsSync(path.join(ROOT, 'cards')) ? fs.readdirSync(path.join(ROOT, 'cards')).filter(f => f.endsWith('.md')).length : 0,
    posts: (() => { let n = 0; const w = d => { for (const e of fs.readdirSync(d, { withFileTypes: true })) e.isDirectory() ? w(path.join(d, e.name)) : (e.name.endsWith('.md') && n++); }; try { w(path.join(ROOT, 'posts')); } catch { } return n; })(),
  };
  return { now, counts, batches, finals };
}

const html = d => `<!doctype html><html lang="zh"><head><meta charset="utf-8"><meta http-equiv="refresh" content="15"><title>课程25 审核流水线 · 实时面板</title>
<style>body{font-family:-apple-system,'PingFang SC',sans-serif;background:#0f172a;color:#e2e8f0;margin:0;padding:24px}
h1{font-size:20px;margin:0 0 4px}.sub{color:#94a3b8;font-size:13px;margin-bottom:18px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}
.card{background:#1e293b;border-radius:12px;padding:14px 16px;border:1px solid #334155}
.card h3{margin:0 0 8px;font-size:15px}.ok{color:#4ade80}.wait{color:#fbbf24}.sev{color:#f87171;font-size:12px}
.kpi{display:flex;gap:12px;margin-bottom:18px}.kpi .card{flex:1;text-align:center}.kpi b{font-size:26px;display:block}
table{width:100%;border-collapse:collapse;font-size:13px}td,th{padding:6px 8px;border-bottom:1px solid #334155;text-align:left}
th{color:#94a3b8;font-weight:500}</style></head><body>
<h1>课程25《小滴课堂低代码大课》· 专家审核流水线</h1>
<div class="sub">刷新于 ${d.now} · 每 15 秒自动刷新 · 扫描 work/target/25-lowcode/</div>
<div class="kpi">
<div class="card"><b>${d.counts.posts}</b>成品篇数(posts)</div>
<div class="card"><b>${d.counts.cards}</b>知识卡片</div>
<div class="card"><b>${d.counts.reports}</b>扫描/审核报告</div>
<div class="card"><b>${d.batches.filter(b => b.size > 0).length}/${d.batches.length}</b>批次完成</div>
</div>
<div class="grid"><div class="card"><h3>批次进度</h3><table><tr><th>批次</th><th>状态</th><th>P0/P1/P2</th><th>时间</th></tr>
${d.batches.map(b => `<tr><td>${b.name}</td><td class="${b.size ? 'ok' : 'wait'}">${b.status}</td><td class="sev">${b.sev ? `${b.sev.p0}/${b.sev.p1}/${b.sev.p2}` : '—'}</td><td>${b.mtime || '—'}</td></tr>`).join('')}
</table></div>
<div class="card"><h3>收尾链</h3><table><tr><th>阶段</th><th>状态</th></tr>
${d.finals.map(f => `<tr><td>${f.file}</td><td class="${f.file && f.file !== '—' ? 'ok' : 'wait'}">${f.file && f.file !== '—' ? '✅ 已产出' : '—'}</td></tr>`).join('')}
<tr><td>hexo 重建 + blog 同步</td><td class="wait">由收尾 agent 执行</td></tr></table>
<h3 style="margin-top:14px">最近报告文件</h3><table><tr><th>文件</th><th>大小</th><th>修改时间</th></tr>
${fs.existsSync(REPORTS) ? fs.readdirSync(REPORTS).map(f => { const s = statSafe(path.join(REPORTS, f)); return s ? `<tr><td>${f}</td><td>${(s.size / 1024).toFixed(1)}K</td><td>${s.mtime.toISOString().slice(5, 19).replace('T', ' ')}</td></tr>` : ''; }).join('') : ''}
</table></div></div></body></html>`;

http.createServer((req, res) => {
  const d = collect();
  res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
  res.end(html(d));
}).listen(4317, () => console.log('dashboard on http://127.0.0.1:4317'));
