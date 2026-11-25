---
title: [AGT-285] 数据外泄防护——Agent 时代的数据防泄露（DLP）怎么做？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-285：Agent 能读能写能外发，数据防泄露怎么做？

**答**:
- 新增泄露面：传统 DLP 管"人把数据发出去"，Agent 增加了机器通道——工具外发（Agent 把内部数据 POST 到第三方 API）、上下文外流（内部数据进了模型供应商日志）、越权读取（Agent 读了用户无权的数据并写进了用户可见的文档）——三条通道分别设防。
- 出站管控：外发操作强制白名单+数据分类校验（带敏感标记的数据禁止出站）、出站内容 DLP 扫描（PII/密钥/源码模式检测）、审计留痕；第三方工具的数据处理协议（DPA）与数据驻留选项纳入采购评审。
- 模型侧防护：企业版 API 的零保留承诺（zero data retention）、自托管模型处理最高敏数据、脱敏代理（发往模型前自动脱敏 PII，返回后还原——代理层方案）。
- 读取控制：Agent 的每次数据读取带 ACL 校验（AGT-283），且"读取→写入"的落点也要校验（把 A 部门数据写进 B 部门文档=泄露）——读写两端都管。

```javascript
async function outboundGuard(payload, target) {
  if (!OUTBOUND_WHITELIST.has(target.domain)) throw '出站未授权';
  const classified = await dlpScan(payload);   // PII/密钥/源码
  if (classified.level >= INTERNAL) {
    throw '敏感数据禁止出站';                  // 高敏直接拦
  }
  await audit.log({ target, level: classified.level });
  return send(payload);
}
// 模型侧：ZDR 供应商 / 脱敏代理 / 自托管
```
