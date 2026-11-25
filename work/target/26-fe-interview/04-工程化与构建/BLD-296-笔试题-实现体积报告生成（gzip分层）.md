---
title: [BLD-296] 笔试题——实现体积报告生成（raw/gzip/brotli 分层 + 入口聚合）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-296：手写体积报告

**需求与边界**：
- 需求：从产物 manifest 生成体积报告——① 每文件三层数（raw/gzip/brotli）；② 入口聚合（入口下载总量 = entry chunk + 同步依赖链——SCN-ENG-290 入口视角）；③ 与基线 diff（增量报告）；④ 超 Ratchet 预算标记。
- 边界：① 压缩用真实算法（zlib gzip/brotli 质量参数固定——可复现）；② 同步依赖闭包聚合（异步 chunk 不计入首屏）；③ 排序按增量降序（关注最大变化）。

**答**：
```javascript
import zlib from 'zlib';
function sizeReport(manifest, baseline, budgets) {
  const sizes = Object.fromEntries(Object.values(manifest.chunks).map(c => {
    const raw = fs.readFileSync(c.file);
    return [c.file, {
      raw: raw.length,
      gzip: zlib.gzipSync(raw, { level: 9 }).length,       // 固定参数可复现
      brotli: zlib.brotliCompressSync(raw).length,
    }];
  }));
  // 入口聚合：同步依赖闭包（异步不计首屏）
  const entryTotal = (entry) => closureChunks(manifest, entry, { async: false })
    .reduce((s, c) => s + sizes[c.file].gzip, 0);
  const rows = Object.keys(manifest.chunks).map(name => {
    const cur = sizes[name], prev = baseline?.sizes[name] ?? { gzip: 0 };
    const delta = cur.gzip - prev.gzip;
    return { name, ...cur, delta, over: budgets[name] && cur.gzip > budgets[name] };
  }).sort((a, b) => b.delta - a.delta);                // 增量降序
  return {
    rows, entryTotal: entryTotal(manifest.entry.main),
    blocking: rows.some(r => r.over),
    md: ['| chunk | raw | gzip | Δ | budget |', '|---|---|---|---|---|',
      ...rows.map(r => `| ${r.name} | ${kb(r.raw)} | ${kb(r.gzip)} | ${sign(r.delta)} | ${r.over ? '⚠️' : '✅'} |`)].join('\n'),
  };
}
```

**评分点**:
- 三层体积（raw/gzip/brotli）固定压缩参数（可复现——SCN-ENG-222）。
- 入口聚合按同步闭包（异步 chunk 不计首屏——用户真实下载量）。
- 基线 diff + 增量降序（关注最大变化）。
- Ratchet 超标 blocking（SCN-ENG-291 联动）。
