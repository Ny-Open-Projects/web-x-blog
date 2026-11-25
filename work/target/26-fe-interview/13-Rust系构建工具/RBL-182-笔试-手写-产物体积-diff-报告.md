---
title: [RBL-182] 笔试：手写产物体积 diff 报告（PR 评论用）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-182：笔试：手写产物体积 diff 报告（PR 评论用）

**答**：写 size-diff.mjs：1) 输入基线与当前的产物目录（各含 manifest.json：文件→gzip 字节数）；2) 生成 markdown 报告表格：新增/删除/变化三类，变化列含绝对差与百分比，超阈值（默认 gzip +10KB 或 +5%）标 ⚠️；3) 汇总总 gzip 体积变化；4) 输出可直接贴进 PR 评论的 markdown；5) 文件名带 hash 的（app.abc123.js）要先归一化名字再对比。

```javascript
// size-diff.mjs
import { readFileSync } from 'node:fs';

function normalize(name) {          // app.abc123.js → app.[hash].js
  return name.replace(/\.([a-f0-9]{8,})\.([cm]?js|css|map)$/, '.[hash].$2');
}

export function sizeDiff(baseManifest, curManifest, { warnBytes = 10_240, warnPct = 5 } = {}) {
  const key = m => Object.fromEntries(
    Object.entries(m).map(([f, b]) => [normalize(f), [f, b]]));
  const B = key(baseManifest), C = key(curManifest);
  const rows = [], added = [], removed = [];
  let baseTotal = 0, curTotal = 0;

  for (const [f, [orig, bytes]] of Object.entries(C)) {
    curTotal += bytes;
    if (!B[f]) { added.push(orig); continue; }
    const baseBytes = B[f][1]; baseTotal += baseBytes;
    const d = bytes - baseBytes;
    const pct = baseBytes ? (d / baseBytes * 100) : 100;
    const warn = d > warnBytes || (baseBytes && pct > warnPct);
    rows.push(`| ${orig} | ${fmt(baseBytes)} | ${fmt(bytes)} | ${d >= 0 ? '+' : ''}${fmt(d)} (${pct.toFixed(1)}%) | ${warn ? '⚠️' : ''} |`);
  }
  for (const f of Object.keys(B)) if (!C[f]) { removed.push(B[f][0]); baseTotal += B[f][1]; }

  const lines = [
    '## 产物体积报告', '',
    '| 文件 | 基线 | 当前 | 差异 | |', '|---|---|---|---|---|',
    ...rows,
    '', `**总 gzip：${fmt(baseTotal)} → ${fmt(curTotal)}（${fmt(curTotal - baseTotal)}）**`,
  ];
  if (added.length) lines.push('', `新增: ${added.join(', ')}`);
  if (removed.length) lines.push('', `删除: ${removed.join(', ')}`);
  const warns = rows.filter(r => r.includes('⚠️')).length;
  return { markdown: lines.join('\n'), warnCount: warns };
}
const fmt = b => b >= 1024 * 1024 ? (b / 1024 / 1024).toFixed(2) + 'MB'
  : b >= 1024 ? (b / 1024).toFixed(1) + 'KB' : b + 'B';
const base = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const cur = JSON.parse(readFileSync(process.argv[3], 'utf8'));
console.log(sizeDiff(base, cur).markdown);
```
**评分点**：
- hash 文件名归一化（否则永远全量"新增+删除"）。
- 三类分类完整：新增/删除/变化。
- 阈值双条件（绝对 KB + 相对 %）。
- 输出可直接渲染的 markdown 表格。
- 总量汇总有正负号语义。
