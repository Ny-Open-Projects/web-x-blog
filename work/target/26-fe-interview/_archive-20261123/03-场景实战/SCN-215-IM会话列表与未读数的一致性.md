---
title: [SCN-215] IM 会话列表与未读数——多端一致怎么保证？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-215：会话列表排序与未读数，手机电脑多端一致怎么保证？

**答**:
- 未读数计算：服务端为准（未读 = 服务器维护的已读游标差值），客户端本地计数只做实时增量（推送到达+1、进入会话清零并上报游标），重连后以服务端值校正——本地计数是缓存不是事实源。
- 多端已读同步：手机读了，电脑未读数要消——已读游标服务端存储+变更推送（读游标变更事件广播到其他端），其他端收到后本地未读数同步清零。
- 会话排序：按 lastMessage 时间排序（服务端下发排序字段），本地新消息到达时更新对应会话并重排（只移动变化的会话项，diff 更新，不整列表重渲）。
- 兜底校正：进入会话列表页全量拉取校正一次（本地漂移累积的修复点）、红点点击后进入会话即清零并上报（交互即同步）。

```javascript
ws.on('msg', (m) => {
  localUnread[m.convId]++;                   // 本地实时 +1
  bumpConversation(m.convId, m);             // 重排该项
});
function enterConversation(convId) {
  const unread = localUnread[convId];
  localUnread[convId] = 0;
  imApi.reportRead(convId, lastSeq(convId)); // 上报游标
  // 其他端收到 read_cursor 事件 → 同步清零
}
ws.on('read_cursor', (e) => {
  if (e.device !== myDevice)
    localUnread[e.convId] = 0;
});
// 进入会话列表：fullSync() 校正未读与排序。
```
