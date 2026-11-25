---
title: [ZSM-530] IM 会话列表的状态建模与未读排序是怎么做的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-530：IM 会话列表的状态建模与未读排序是怎么做的

**答**：
- 归一化建模：`sessions: Map<sessionId, Session>` 存实体，`order: string[]` 存展示序——新消息到达时只改一个 Map 项 + 调整 order（把该会话移到头部），不重建整个列表对象。
- Session 结构：`{ lastMsg, unread, pinned, muted, updatedAt }`；排序规则一般是「置顶 > 时间倒序」，用派生 selector 计算（`order` 只存原始到达序，展示序派生），排序逻辑改了不用迁移存储。
- 未读数：进房（visible 且聚焦）时调 `markRead(sessionId)` 清零并上报服务端；后台到达的消息 unread++。本地未读与「已读游标」分开存，多端同步用服务端游标为准。
- 性能要点：会话列表几十上百条且高频更新，Map + per-session selector（每行订阅自己的 session），一条新消息只重渲受影响的行；整表排序结果变化时才触发列表层重渲。
- 追问钩子：消息本体不要塞进 session（会撑爆快照比较成本），消息列表单独按会话分页缓存。

```javascript
const useIM = create((set) => ({
  sessions: new Map(),
  order: [],
  onNewMessage(sessionId, msg) {
    set((s) => {
      const cur = s.sessions.get(sessionId)
      const next = new Map(s.sessions)
      next.set(sessionId, {
        ...cur,
        lastMsg: msg,
        unread: cur.unread + (msg.self ? 0 : 1),
        updatedAt: msg.ts,
      })
      // order 头部插入（去重）
      const order = [sessionId, ...s.order.filter((id) => id !== sessionId)]
      return { sessions: next, order }
    })
  },
  markRead(sessionId) {
    set((s) => {
      const next = new Map(s.sessions)
      next.set(sessionId, { ...next.get(sessionId), unread: 0 })
      return { sessions: next }
    })
    api.reportRead(sessionId)   // 异步上报，失败本地游标兜底
  },
}))

// 展示序派生：置顶优先、其余按时间倒序
const useVisibleSessions = () => useIM(useShallow((s) =>
  [...s.order]
    .map((id) => ({ id, ...s.sessions.get(id) }))
    .sort((a, b) => (b.pinned - a.pinned) || (b.updatedAt - a.updatedAt))
))
```
