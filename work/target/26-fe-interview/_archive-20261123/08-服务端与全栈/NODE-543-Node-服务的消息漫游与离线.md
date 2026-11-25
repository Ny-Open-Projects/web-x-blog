---
title: [NODE-543] Node 服务的消息漫游（多端历史同步）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-543：消息漫游实现
**答**:
- 漫游定义：换设备登录后能拉到历史消息（到最早或到保留期）——存储策略决定体验与成本。
- 存储分层：热消息（近期：7 天——Redis/内存索引快）、全量消息（保留期：1 年——DB 分表按会话/时间）、超期消息（归档——按需恢复或只读快照）。保留期是产品决策（成本 vs 漫游时长）——配置化。
- 同步协议：新设备登录 → 按会话拉取（最近 N 条快照 + 更早的按页加载——首屏快后端懒）、增量同步（已知 lastSeq 的设备 → 只拉 gap ARC-392）、消息修订同步（撤回/编辑历史也要漫游——修订记录随消息存储）。
- 性能与成本：漫游查询是重 IO（大会话深翻——索引设计：会话+seq 索引 NODE-400 cursor）、热点会话（万人群漫游——群消息分片 + 端缓存为主，服务端只补 gap）。
- 隐私与合规：消息保留期与用户控制（用户可清除漫游记录——NODE-443 数据权利）、合规存档（监管要求场景的独立存档与业务漫游分离）。
```javascript
// 漫游拉取
app.get('/conv/:id/messages', async (ctx) => {
  const { cursor, limit = 50 } = ctx.query;
  const rows = await msgRepo.bySeq(ctx.params.id, cursor, limit);  // 会话+seq 索引
  ctx.body = { items: rows, nextCursor: rows.at(-1)?.seq ?? null };
});
// 新设备：POST /sync { devices: [{convId, lastSeq}] } → 返回各会话 gap
```
