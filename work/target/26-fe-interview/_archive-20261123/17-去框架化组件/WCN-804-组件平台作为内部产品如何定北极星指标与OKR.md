---
title: [WCN-804] 组件平台作为「内部产品」如何定义北极星指标与 OKR？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-804：组件平台作为「内部产品」如何定义北极星指标与 OKR？

**答**：
- 结论先行：平台把「业务方」当客户，北极星指标要同时衡量「被用得多」和「用得好」——推荐用「周活跃使用组件的业务页面数 × 契约达标率」这类复合指标，而非单纯的组件数。
- 采纳度维度：周活跃使用页面数、新组件走平台的占比、跨 BU 复用次数——反映「有没有人用」。
- 质量维度：契约达标率（a11y/token 裸值/版本合规）、线上组件事故数、文档新鲜度——反映「用得安不安全」。
- 效率维度：业务方接入耗时（从引 npm 到上线）、需求响应 SLA、贡献组件审查周期——反映「客户体验」。
- OKR 写法示例：O=「让业务方默认选择平台组件」；KR=「新页面平台组件覆盖率 40%→75%」「接入耗时从 3 天降到 4 小时」「a11y 达标率 100%」。
- 追问钩子：面试官会问「指标被刷怎么办」——要点出采纳度必须与质量门禁绑定（用了但契约不达标不算数），并加入满意度（NPS）做交叉验证。

```javascript
// 北极星指标聚合：采纳 × 质量 × 效率，知名度不等于健康度
function northStar({ activePages, totalPages, contractPass, incidents, nps }) {
  const adoption = activePages / totalPages;          // 0~1
  const quality = contractPass * (1 - Math.min(incidents / 10, 1));
  const score = Math.round(100 * Math.cbrt(adoption * quality * Math.max(nps, 0) / 100));
  return { adoption: +(adoption * 100).toFixed(1), quality: +(quality * 100).toFixed(1), score };
}
console.log(northStar({ activePages: 120, totalPages: 400, contractPass: 0.95, incidents: 1, nps: 60 }));
// { adoption: 30, quality: 85.5, score: ... }
```
