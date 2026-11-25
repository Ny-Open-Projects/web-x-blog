---
title: [SCN-704] SLA 看板的指标体系怎么设计？哪些指标该上板哪些不该？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-704：SLA 看板指标体系怎么设计？
**答**：
- 上板原则：每个指标必须「有 SLO + 有 Owner + 可行动」——三者缺一不上板（没有 owner 的指标没人管，不可行动的指标制造焦虑）。
- 指标分层：核心区（4~6 个北极星指标：核心页面可用性/P95 加载/JS 错误率/接口成功率）+ 明细区（按业务线/页面）+ 实验区（新指标放半年观察再转正）。
- 口径版本化：指标口径变更（如 LCP 采样策略调整）必须版本化并标注在图上，否则趋势图会「假跳变」。
- 指标命名规范：`<层级>.<对象>.<指标>.<统计维度>`（如 page.checkout.lcp.p95.region=cn-north）。
- 追问钩子：看板指标越来越多怎么办——每季度指标评审会：砍掉连续一个季度没人看/没触发过行动的指标（看板也要做减法）。

```javascript
const boardMetrics = {
  core: [
    { key: 'ux.core_page.availability', slo: 0.999, owner: 'web-team' },
    { key: 'ux.core_page.lcp_p95', slo: 2500, owner: 'perf-team', unit: 'ms' },
    { key: 'ux.js_error.rate', slo: 0.005, owner: 'fe-stability' },
    { key: 'api.core.success_rate', slo: 0.995, owner: 'gateway-team' },
  ],
  rules: {
    onBoard: (m) => m.slo && m.owner && m.actionable,
    deprecate: (m) => m.idleQuarters >= 1,        // 季度评审砍指标
    versioned: true,                              // 口径变更版本化
  },
};
```
