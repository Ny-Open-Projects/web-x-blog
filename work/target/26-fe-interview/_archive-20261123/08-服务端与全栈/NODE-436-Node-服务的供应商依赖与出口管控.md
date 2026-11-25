---
title: [NODE-436] Node 服务的供应商依赖（SaaS/云服务）与出口管控如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-436：供应商依赖与出口管控
**答**:
- 供应商清单化：每个外部依赖（短信/支付/地图/风控 SaaS）登记（用途/SLA/替代方案/成本/密钥轮换周期）——供应商故障时能快速知道影响哪些功能。
- 出口管控：出站流量经统一出口（egress 网关 ARC-356 思想），实现集中限流/审计/密钥托管（应用不持供应商密钥，网关注入）与供应商切换（适配层路由切换，NODE-425）。
- 供应商风险预案：SLA 违约监控（实际可用性 vs 承诺记录）、替代方案演练（备供应商灰度切换——真切换过才算有备选）、供应商停服/涨价风险（关键能力双供应商）。
- 数据出境与合规：发往第三方的数据分级（哪些 PII 允许出去——ARC-396 合规审查覆盖供应商）、供应商数据处理协议（DPA）。
- 密钥治理：供应商密钥集中管理（KMS + 轮换 NODE-362）、泄漏应急（立即吊销 + 切换流程）。
```javascript
// 供应商注册表
const vendors = {
  sms: { primary: 'aliyun', backup: 'tencent', sla: 99.9,
    egress: '/api/vendor/sms/*', dataClass: 'phone-masked' },    // 出口统一 + 数据分级
  maps: { primary: 'amap', backup: null, risk: '单点，评估备选' }
};
// 出口网关：按 vendors[tag].egress 路由 → 注入密钥 → 计量 → 失败切 backup
```
