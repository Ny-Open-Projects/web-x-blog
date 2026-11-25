---
title: [RBL-080] 笔试：手写构建报告生成器（体积榜 + 依赖贡献）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-080：笔试：手写构建报告生成器（体积榜 + 依赖贡献）
**答**：实现 buildReport(stats)：输入 { chunks: [{ name, size, modules: [{ path, size, owner }] }] }，输出：1) chunk 体积降序榜（前 5，含 gzip 估算 gzip≈0.3*size）；2) 按 owner（node_modules 包名）聚合的依赖贡献榜；3) 单模块超过 100KB 的告警清单；4) 重复模块检测（同 path 出现于多 chunk）；5) 输出 markdown 报表字符串。

```javascript
const kb = (n) => (n / 1024).toFixed(1);

function buildReport(stats) {
  const lines = ['# Build Report', ''];

  // 1) chunk 体积榜
  const chunks = [...stats.chunks].sort((a, b) => b.size - a.size).slice(0, 5);
  lines.push('## Top chunks');
  for (const c of chunks)
    lines.push(`- ${c.name}: ${kb(c.size)}KB (gzip≈${kb(c.size * 0.3)}KB)`);

  // 2) 依赖贡献榜（node_modules 包聚合）
  const ownerSize = new Map();
  for (const c of stats.chunks)
    for (const m of c.modules)
      if (m.owner.startsWith('node_modules/'))
        ownerSize.set(m.owner, (ownerSize.get(m.owner) || 0) + m.size);
  const owners = [...ownerSize.entries()].sort((a, b) => b[1] - a[1]).slice(0, 5);
  lines.push('', '## Top deps');
  for (const [o, s] of owners) lines.push(`- ${o}: ${kb(s)}KB`);

  // 3) 大模块告警
  const big = [];
  for (const c of stats.chunks)
    for (const m of c.modules)
      if (m.size > 100 * 1024) big.push(`${m.path} (${kb(m.size)}KB in ${c.name})`);
  if (big.length) lines.push('', '## ⚠ Large modules', ...big.map(b => `- ${b}`));

  // 4) 重复模块
  const seen = new Map();
  for (const c of stats.chunks)
    for (const m of c.modules) seen.set(m.path, (seen.get(m.path) || 0) + 1);
  const dup = [...seen.entries()].filter(([, n]) => n > 1);
  if (dup.length) lines.push('', '## ⚠ Duplicated', ...dup.map(([p, n]) => `- ${p} x${n}`));

  return lines.join('\n');
}
module.exports = { buildReport };
```
**评分点**：
- 排序 + 截断（Top N 榜单语义）。
- owner 聚合取包名前缀（node_modules/xxx）。
- 重复模块跨 chunk 检测（splitChunks 失效信号）。
- gzip 估算标注为近似值（不冒充实测）。
- 输出 markdown 可直接贴 PR/CI summary。
