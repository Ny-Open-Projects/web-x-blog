---
title: [NODE-442] Node 服务的审计日志体系（合规级）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-442：审计日志体系（合规级）
**答**:
- 审计 vs 业务日志分离：审计日志（谁对什么资源做了什么敏感操作）是合规证据——独立存储、只追加（append-only）、不可静默修改、保留期长（合规要求 6 个月~3 年）。
- 事件模型：{ actor（谁）, action（操作）, resource（对象）, before/after（变更摘要）, context（IP/UA/时间/traceId）, result }；敏感操作清单化（权限变更/数据导出/删除/支付配置）。
- 写入保障：审计写入失败不阻塞业务（异步 + 本地缓冲重试），但缓冲满要告警（审计缺失是合规风险）；审计事件幂等（事件 ID 去重防重复记录）。
- 查询与告警：按主体/对象/时间检索；高危模式实时告警（批量导出/深夜权限变更——风控联动 ARC-159）。
- 完整性：日志哈希链（每条含前条哈希——防篡改，审计可验证连续性）、访问审计日志本身也要审计（谁能查审计日志）。
```javascript
async function audit(event) {
  const prev = await auditStore.last();
  const entry = { id: uuid(), ...event, prevHash: prev?.hash,
    hash: sha256(JSON.stringify({ ...event, prevHash: prev?.hash })) };  // 哈希链
  await buffer.push(entry);                                      // 异步批量落库（append-only 表）
  if (isHighRisk(event)) await riskCenter.notify(entry);         // 高危实时告警
}
```
