---
title: [PER-927] 前端性能平台如何对接 DevOps 流水线
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-927：前端性能平台如何对接 DevOps 流水线

**答**：
- 接入点：PR 阶段（体积 diff 评论）、合并前（门禁）、部署后（冒烟 Lighthouse）、发版后 24h（RUM 劣化自动回帖到发布单）。
- 反馈形态：流水线里输出人话报告（"本次新增 120KB JS，主要来自 chart.js，建议按需引入"），不做无声拦截。
- 流水线加速：性能检查与单测并行、复用缓存产物、非核心页面抽样跑。
- 度量闭环：统计门禁拦截率与事后真实劣化的吻合度，持续校准阈值，避免门禁形同虚设。

```javascript
// PR 体积评论生成
function prComment(diffManifest, budgets) {
  const lines = Object.entries(diffManifest)
    .filter(([, d]) => d.delta > 10_000)
    .map(([f, d]) => `- `${f}` +${(d.delta / 1024).toFixed(0)}KB` +
      (d.delta > (budgets[f]?.max ?? Infinity) ? ' ⚠️ 超预算' : ''));
  return ['### 构建体积报告', ...lines,
    `总计 ${(diffManifest.__total__.delta / 1024).toFixed(0)}KB`].join('
');
}
// CI 把该评论贴到 PR，开发者合并前即感知
```
