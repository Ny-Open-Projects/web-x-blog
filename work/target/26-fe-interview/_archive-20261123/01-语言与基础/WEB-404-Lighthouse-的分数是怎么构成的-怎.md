---
title: [WEB-404] Lighthouse 的分数是怎么构成的？怎么定优化优先级？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-404：Lighthouse 的分数是怎么构成的？怎么定优化优先级？
**答**：
- 性能分由 LCP(25%)/CLS(25%)/TBT(30%)/FCP(10%)/SI(10%) 加权，中位数设备节流（Moto G4+慢4G）下测。
- 优先级排序：看分数贡献（哪个指标拖分最多）→ 看诊断项（ Opportunities 的节省时间估计）→ 结合业务（转化页优先 LCP）。
- 注意：CI 环境用 lighthouse-ci 固定基准防波动；本地分数不代表真实用户，以 CrUX/RUM 数据校准。

```javascript
const weights = { LCP: .25, CLS: .25, TBT: .3, FCP: .1, SI: .1 };
const deficit = (scores) => Object.entries(weights)
  .map(([k, w]) => [k, w * (1 - scores[k])])
  .sort((a, b) => b[1] - a[1])[0];
console.log(deficit({ LCP: .6, CLS: .9, TBT: .5, FCP: .8, SI: .7 })); // TBT 拖分最多
console.log('先修 TBT（拆长任务），再看 LCP');
```
