---
title: [BLD-257] Chunk 内再切分与 HTTP 缓存的 ROI 怎么算？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-257：切分 ROI 怎么算？
**答**：
- 切分收益模型：把大 chunk 切小后「变更时只需重新下载变更的小 chunk」（增量收益）vs「额外请求数与头部开销」（成本）。
- 关键变量：chunk 变更频率差异（稳定 vendor 与高频业务分离才有增量收益——同频变更切了白切）、用户回访率（首次访问无增量收益）、HTTP2 多路复用（请求开销下降，切分成本变低）。
- 实践公式：切分的增量收益 ≈ 未变更部分占比 × 回访率 × chunk 大小 − 请求数 × 单请求开销——回访率高的应用切分收益大，首访型应用（营销页）收益趋零。
- 追问钩子：为什么「首访型应用（营销页）」不值得精细切分——切分的全部收益来自「第二次访问的增量下载」；营销页用户几乎不来第二次，切分只增加请求数没有增量收益——分割策略必须看「回访率」这个业务变量，纯技术视角会做出负优化。

```javascript
// 切分 ROI 模型
const roi = (chunk) => ({
  gain: chunk.unchangedRatio * revisitRate * chunk.size,
  cost: extraRequests * perRequestOverhead,
  worth: gain > cost,                                  // vendor/业务分频才切
});
// 按变更频率分组（分离才有效）
manualChunks: (id) => isVendor(id) ? 'vendor' : 'business'
```
