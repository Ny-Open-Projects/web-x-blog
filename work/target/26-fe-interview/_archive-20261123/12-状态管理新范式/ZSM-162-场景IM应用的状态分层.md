---
title: [ZSM-162] 场景：IM 应用的状态怎么分层？会话列表、消息分页、未读数、推送怎么组织？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-162：场景：IM 应用的状态怎么分层？会话列表、消息分页、未读数、推送怎么组织？
**答**：
- 四块划分：会话列表 = 服务端缓存（Query `['conversations']`，推送到达时局部 mutate）；某会话消息 = 双向无限分页缓存（`['messages', roomId]` + maxPages）；未读数 = 服务端派生（按会话 key 小缓存或直接 mutate 维护）；连接状态/草稿 = 客户端 store。
- 推送接线：WS 收到新消息 → ① 消息缓存 mutate 追加（去重按 clientId/id）→ ② 会话列表 mutate 置顶改 lastMsg → ③ 未读数 mutate +1（当前打开的会话除外）——推送是「写缓存的另一种来源」，不走 invalidate（省请求且延迟低）。
- 一致性兜底：本地 mutate 的数据标 pending，断线重连/失焦时对该会话 invalidate 对账；离线消息靠服务端 seq 补拉。
- 面试要点：能按「数据更新来源」划分状态——拉（HTTP）、推（WS）、写（本地输入）三种来源各自的 owner。

```javascript
// 推送接线器：WS → 三个缓存域的局部更新
export function wirePushHandlers(ws, qc) {
  ws.on('message', async (msg) => {
    qc.setQueryData(['messages', msg.roomId], (old = { items: [] }) =>
      old.items.some(m => m.id === msg.id) ? old :            // 去重
        { ...old, items: [...old.items, msg] })
    qc.setQueryData(['conversations'], (old = []) =>
      bumpConversation(old, msg))                              // 置顶 + lastMsg
    if (!isOpenRoom(msg.roomId))
      qc.setQueryData(['unread'], (old = 0) => old + 1)
  })
  ws.on('resumed', () =>                                       // 重连对账
    qc.invalidateQueries({ queryKey: ['messages'] }))
}

// 连接状态（客户端态）与草稿走 Zustand
const useImStore = create((set) => ({
  wsStatus: 'connecting', drafts: {},
  setWsStatus: (wsStatus) => set({ wsStatus }),
  setDraft: (roomId, text) => set(s => ({ drafts: { ...s.drafts, [roomId]: text } })),
}))
```
