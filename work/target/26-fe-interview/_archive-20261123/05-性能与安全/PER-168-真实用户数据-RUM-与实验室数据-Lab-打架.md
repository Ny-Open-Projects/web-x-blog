---
title: [PER-168] 真实用户数据（RUM）与实验室数据（Lab）打架时怎么处理？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-168：真实用户数据（RUM）与实验室数据（Lab）打架时怎么处理？

**答**：
- 先确认**口径差异**：RUM 是全量真机分布（含低端机/弱网/登录态），Lab 是固定设备+固定网络（如 Moto G4 + 4G）；两者本来就不该相等。
- 三步归因：差值小（<500ms）视为一致；低端机占比高 → 用户群差异，以 RUM 排期；第三方脚本在 Lab 被拦截 → 环境差异，Lab 复测时放行对比。
- 职责分工：**对外承诺与业务看板用 RUM P75**（SEO、SLA、大盘），**日常回归与 CI 门禁用 Lab**（快、稳定、可复现）。
- 反模式警告：不要用 Lab 数字给真实用户背书，也不要拿 RUM 抖动否定某次代码优化。

```javascript
// RUM 与 Lab 打架：先确认口径，再归因，最后按场景选信源
export function reconcile(rum, lab) {
  const delta = rum.lcpP75 - lab.lcp;

  if (Math.abs(delta) < 500) return { verdict: '一致', action: '按现状优化' };

  // 1. 用户群差异：RUM 含大量低端机/弱网用户，Lab 是固定中端设备
  if (rum.lowEndShare > 0.4) {
    return {
      verdict: '用户群差异',
      action: '以 RUM 为准排期，Lab 用于优化项的回归验证',
      note: `低端机占比 ${rum.lowEndShare}，Lab 设备不代表真实分布`,
    };
  }

  // 2. 环境差异：第三方脚本/缓存命中率/登录态在 Lab 里不出现
  if (rum.thirdPartyBlockedShare > 0.2) {
    return { verdict: '第三方污染', action: 'Lab 复测放行第三方并对比前后差异' };
  }

  // 3. 分工规则：对外承诺看 RUM P75，日常回归与门禁看 Lab，两者各管一段
  return { verdict: '口径或环境差异', action: '分看板管理，不用 Lab 数字给真实用户背书' };
}
```
