---
title: [MFW-205] RSC 边界案例：服务端实时数据（轮询/推送）在 RSC 模型下的落位
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## MFW-205：服务端实时数据在 RSC 模型下的落位

**答**:
- RSC 是「请求-响应」模型，没有长连接——实时数据的三种落位：客户端组件内 WebSocket（数据层在客户端）、Server Action 轮询（客户端定时调用 Action）、RSC 重渲染触发（invalidate Router Cache 定时刷新）
- 选型：高频推送（行情/协作）→ 客户端 WS 直连（RSC 不适合）；中频状态（通知数）→ Action 轮询；低频内容（文章更新）→ 定时 router.refresh()
- 混合架构：RSC 管首屏与静态框架，实时通道由客户端组件独立建立——两层各司其职
- 关键认知：不要试图让 RSC「订阅」数据——它的生命周期止于本次响应

```javascript
// 客户端 WS（高频实时）
'use client'
function LiveTicker() {
  useEffect(() => {
    const ws = new WebSocket('/ws/ticker')
    ws.onmessage = (e) => setPrice(JSON.parse(e.data))     // 数据层在客户端
    return () => ws.close()
  }, [])
}
// 低频内容：定时 RSC 刷新
useEffect(() => { const t = setInterval(() => router.refresh(), 60_000); return () => clearInterval(t) }, [])
```
