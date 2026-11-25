---
title: [TST-281] Lighthouse CI 如何作为性能回归门禁？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-281：Lighthouse CI 如何作为性能回归门禁？
**答**：
- 每次 PR 跑 Lighthouse（预算模式 budget.json：LCP/TBT/体积阈值），超预算直接 fail。
- 关键页清单固定（首页/商详/结算），环境稳定（同一构建产物 + 同网络节流设置）。
- 多次采样取中位数（单次波动大），阈值留 10% 余量防误报。
- 报告趋势入库：分数/指标随时间曲线，异常回看定位引入 commit。

```javascript
// budget.json
[{
  "path": "/*",
  "resourceSizes": [{ "resourceType": "script", "budget": 170 }],
  "resourceCounts": [{ "resourceType": "third-party", "budget": 10 }],
  "timings": [
    { "metric": "largest-contentful-paint", "budget": 2500 },
    { "metric": "total-blocking-time", "budget": 300 }
  ]
}]
r
```
