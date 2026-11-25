---
title: [WCN-774] 编译响应式应用的包体积预算如何在 CI 中卡点？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-774：编译响应式应用的包体积预算如何在 CI 中卡点？

**答**：
- 结论：用 size-limit/bundlephobia 在 CI 对关键产物设体积上限（gzip 后），超限即失败；按路由/组件维度拆分预算，避免单个 chunk 膨胀。
- 结合 stats 分析（source-map-explorer）定位体积来源；对新增依赖做体积影响审查（bundle 增量 < 阈值）。
- 追问钩子：gzip 后达标但解析耗时仍高怎么办？考察「压缩体积 ≠ 解析执行成本」——要关注 uncompressed size 与 TBT。

```javascript
// .size-limit.json
[
  { "path": "dist/core.js", "limit": "30 kB" },
  { "path": "dist/button.js", "limit": "8 kB" },
  { "path": "dist/table.js", "limit": "15 kB" }
]
// CI 脚本：比较当前与基线产物体积
function checkBudget(stats, budget) {
  const errs = [];
  for (const [file, limit] of Object.entries(budget)) {
    if ((stats[file] || 0) > limit) errs.push(`${file} 超限: ${stats[file]} > ${limit}`);
  }
  return errs;
}
console.log(checkBudget({ 'core.js': 31 }, { 'core.js': 30 }));
```
