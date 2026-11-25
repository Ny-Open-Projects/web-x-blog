---
title: [NODE-542] Node 服务的消息已读回执与多端同步如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-542：已读回执服务端
**答**:
- 已读模型：会话级 lastReadSeq（ARC-502 服务端实现——seq 由服务端统一发放保证单调）+ 设备维度（各端各自 lastRead——取 max 作为已读水位）。
- 回执链路：客户端上报已读（批量：读到 seq N = N 之前全读——合并上报防高频）→ 服务端更新水位 → 通知对方（单聊：已读回执推送——对方 UI 显示已读）。
- 一致性细节：seq 发放权威（客户端 seq 不可信——服务端按会话 INCR 分发）、乱序上报（seq 回退忽略——单调性保证）、多端同步（设备 A 读了 → 设备 B 未读数同步减——推送各端更新 ARC-500）。
- 群聊语义：已读列表（谁读了谁没读——成员级 lastRead 水位存储，大群裁剪：只维护最近活跃成员——存储权衡）、未读人数计算。
- 性能：已读上报削峰（合并 + 限频）、回执推送节流（对方端收到后批量渲染）。
```javascript
// 已读水位服务端
async function reportRead(convId, uid, seq) {
  if (seq <= await lastRead(convId, uid)) return skip();         // 单调性
  await redis.set(`read:${convId}:${uid}`, seq);
  const members = await convMembers(convId);
  publish(`conv:${convId}`, { type: 'read', uid, seq });         // 通知他人
}
// seq 分发：redis INCR seq:${convId} —— 消息落库时发放
```
