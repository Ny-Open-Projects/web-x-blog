---
title: [AGT-295] 多会话与并发任务——前端怎么管理多个 Agent 会话？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-295：用户同时跑多个 Agent 会话/任务，前端怎么管理？

**答**:
- 会话列表与任务面板：会话按"活跃任务/待审批/已完成"分组，活跃任务显示进度摘要（步骤 x/y、当前工具）——用户的核心诉求是"扫一眼知道哪个在等我"；待审批任务置顶并推送通知（AGT-293 审批卡在通知中可直达）。
- 连接管理：活跃会话才保持 SSE 连接，后台会话挂起时断流、切回时拉增量（AGT-294）——几十个会话全开连接会拖垮浏览器与服务端；通知靠服务端推送（Web Push/长轮询心跳）而不是每会话一连接。
- 并发限制与提示：用户级并发任务上限（服务端配额，AGT-277）前端提前提示（"最多同时 3 个任务"），超出进入队列并显示排队位置——比默默拒绝体验好。
- 状态同步：多标签页用 BroadcastChannel/服务端事件同步任务状态变更，避免"这个标签页已批准那个还显示待审批"的分裂。

```javascript
const hub = useSessionHub({
  active: s => attachSSE(s.id),           // 只连活跃会话
  background: s => detachSSE(s.id),
});
onNotify(task => {                        // 审批到达
  if (task.type === 'approval') pushBanner(task);
});
// BroadcastChannel 同步多标签页状态
bc.onmessage = e => e.data.type === 'task_update' && refresh(e.data);
```
