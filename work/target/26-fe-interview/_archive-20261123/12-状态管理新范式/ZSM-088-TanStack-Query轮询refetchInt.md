---
title: [ZSM-088] TanStack Query 怎么做轮询（refetchInterval）？怎么做到「有新消息才轮询」或页面隐藏时暂停？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-088：TanStack Query 怎么做轮询（refetchInterval）？怎么做到「有新消息才轮询」或页面隐藏时暂停？
**答**：
- refetchInterval 设毫秒数轮询；设函数 `(query) => number | false` 可按当前数据/状态动态决定频率或停止。
- 动态策略示例：未读数 > 0 时 5s，无消息时 30s，超出闲时降频；有 WebSocket 推送时直接 false 停轮询。
- refetchIntervalInBackground: false（默认）：页面切后台暂停轮询，回来继续；配合 refetchOnWindowFocus 双保险。
- 轮询替代方案：长轮询/SSE/WS 拿推送后 invalidate 或 setQueryData；轮询只是「无推送能力」的兜底。

```javascript
useQuery({
  queryKey: ['unread'],
  queryFn: api.unread,
  refetchInterval: query => {
    const n = query.state.data?.count ?? 0
    return n > 0 ? 5_000 : 30_000   // 有新消息快轮，闲时降频
  },
  refetchIntervalInBackground: false, // 后台暂停
})
```
