---
title: [PER-1225] 如何应对"指标改版"（如 INP 替代 FID）的迁移工程
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1225：如何应对"指标改版"（如 INP 替代 FID）的迁移工程

**答**：
- 背景：Chrome 2024 起 INP 替代 FID 作为 Core Web Vitals——口径迁移涉及门禁/看板/预算全链。
- 迁移步骤：双采集期（FID+INP 并行 3 月）→ 相关性分析（FID 与 INP 相关度，历史基线换算）→ 门禁切换（INP 生效、FID 只读）→ 文档更新。
- 坑：INP 含整交互时延，历史 FID 无法换算出 INP 预算——需新采集数据定预算（933 棘轮）。
- 通知：订阅方（业务 Owner/高管报告）提前 1 月告知口径切换日与断点。

```javascript
// 双采集迁移监控
function migrationMonitor(records) {
  const paired = records.filter(r => r.fid != null && r.inp != null);
  const corr = pearson(paired.map(r => r.fid), paired.map(r => r.inp));
  return { samples: paired.length, correlation: +corr.toFixed(2),
    note: corr < 0.5 ? 'FID 无法换算 INP，预算需新采集重定' : '相关性可用辅助换算',
    cutoff: '2024-03-12 后 FID 只读' };
}
function pearson(xs, ys) {
  const n = xs.length;
  const mx = xs.reduce((s, v) => s + v, 0) / n;
  const my = ys.reduce((s, v) => s + v, 0) / n;
  const cov = xs.reduce((s, v, i) => s + (v - mx) * (ys[i] - my), 0);
  return cov / Math.sqrt(xs.reduce((s, v) => s + (v - mx) ** 2, 0) *
    ys.reduce((s, v) => s + (v - my) ** 2, 0));
}
```
