---
title: [NODE-625] Node 服务的消息撤回与编辑（修订传播）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-625：消息撤回与编辑
**答**:
- 模型：消息修订记录（原消息 + 修订事件（撤回/编辑）——不改原文，修订链可追溯（合规审计需要））、修订传播（修订事件广播各端——ARC-622）、修订权限与时效（时限内可撤回/编辑——产品规则；管理员撤回——权限矩阵）。
- 一致性：已读与撤回交错（已读后撤回——端上显示"已撤回"占位——保留列表结构 ARC-501）、多端修订顺序（修订事件 seq——乱序丢弃旧修订）、修订与引用（被引用的消息撤回——引用处同步标注"原消息已撤回"）。
- 索引与搜索联动：撤回消息不入检索索引（NODE-544 filter recalled）、编辑更新索引（内容变更——索引重写）。
- 推送联动：已推送的消息撤回（Push 撤回（端上支持）或通知栏刷新——能力降级）、离线端同步（修订随漫游同步——ARC-543 修订记录入漫游）。
- 合规：撤回不等于删除（合规存档保留原文——监管场景、与用户端展示分离——语义明确）。
```javascript
// 撤回修订链
async function recall(msgId, uid) {
  await checkAuth(msgId, uid);                                   // 权限+时效
  const rev = await msgRepo.addRevision(msgId, { type: 'recall', by: uid, seq: nextSeq() });
  await broadcastToUser(msg.owner, revisionEvent(rev));          // 多端广播
  await es.update(recallFlag(msgId));                            // 索引联动
}
```
