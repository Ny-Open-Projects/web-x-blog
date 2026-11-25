---
title: [NODE-394] Node 服务的实时通知系统（站内信/推送合并）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-394：实时通知系统
**答**:
- 通知架构：事件源（业务系统发事件到 MQ）→ 通知服务（模板渲染 + 渠道路由 + 合并抑制）→ 渠道（WS 在线推送 / Web Push 离线 / 站内信落库）。
- 合并与抑制（防轰炸）：同类型事件窗口合并（"3 人赞了你"聚合一条）、用户偏好频道开关、勿扰时段（夜间静默，次日合并推送）、重复抑制（同一对象会话内只推一次）。
- 可靠性：通知落库先于推送（先写站内信表再推实时——推送失败用户仍可在通知中心看到）；推送链路异步化不阻塞业务事件消费；幂等（消息 ID 去重）。
- 在线/离线路由：用户有活跃 WS 连接 → 实时推；无连接 → Web Push/短信（按优先级降级）；推送结果回执更新触达统计。
- 未读数：Redis 计数器（incr）+ 定期与 DB 对账；多端未读同步（ARC-500 广播）。
```javascript
consumer.on('data', async (evt) => {
  if (await seen(evt.id)) return;                                // 幂等
  const notices = await template.render(evt);
  for (const n of await suppress(notices)) {                     // 合并抑制
    await db.insertNotice(n);                                    // 先落库
    if (online(n.uid)) wsGateway.push(n.uid, n);                 // 在线实推
    else await webPush.send(n);                                  // 离线推送
    await unread.incr(n.uid, n.type);
  }
});
```
