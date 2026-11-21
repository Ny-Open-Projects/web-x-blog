---
title: [ZSM-112] SWR 怎么处理 IM 这类推送数据？useSWRSubscription 和 mutate 手动灌数据怎么选？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-112：SWR 怎么处理 IM 这类推送数据？useSWRSubscription 和 mutate 手动灌数据怎么选？
**答**：
- 两条路：useSWRSubscription 把 WebSocket/事件流「接入」SWR 缓存体系，事件回调里向 key 灌增量数据；或者更轻的做法——消息到达时直接对会话 key 做局部 mutate 追加。
- 选择标准：推送逻辑复杂、需要重连/心跳封装时用 subscription Hook 统一管理生命周期；只是往已有列表 append 一条时，mutate 更直接且能复用去重。
- IM 典型结构：`['/api/messages', roomId]` 存历史消息分页，新消息 mutate 到最后一页缓存；未读数走另一个轻 key 单独缓存。
- 追问钩子：本地灌入的数据要标记 `pending: true`，重验证时与服务端对账去重，防止断线重连后重复消息。

```javascript
import useSWRSubscription from 'swr/subscription'
import { mutate } from 'swr'
import useSWR from 'swr'

function ChatRoom({ roomId }) {
  // 1. 订阅推送，增量灌入缓存
  useSWRSubscription(roomId ? ['ws', roomId] : null,
    ([, room], { next }) => {
      const ws = connect(room)
      ws.onmessage = (e) => {
        const msg = JSON.parse(e.data)
        mutate(['/api/messages', room], (pages) => {
          const nextPages = [...pages]
          nextPages[nextPages.length - 1] = {
            ...nextPages.at(-1),
            items: [...nextPages.at(-1).items.filter(m => m.id !== msg.id), msg],
          }
          return nextPages
        }, { revalidate: false })
      }
      return () => ws.close()
    })

  // 2. 历史消息仍走常规 SWR 分页
  const { data: pages } = useSWR(['/api/messages', roomId], fetcher)
  return <Messages items={pages?.flatMap(p => p.items) ?? []}/>
}
```
