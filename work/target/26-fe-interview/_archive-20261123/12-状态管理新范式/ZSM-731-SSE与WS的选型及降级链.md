---
title: [ZSM-731] SSE vs WebSocket vs 轮询：推送通道的选型与降级链
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-731：SSE vs WebSocket vs 轮询：推送通道的选型与降级链

**答**：
- 三通道能力对照：**SSE**（HTTP 单向推送，自动重连、Last-Event-ID 续传内建、文本-only、HTTP/1.1 下 6 连接限制）适合「服务端 → 客户端」的通知流（进度条、通知中心、AI 流式输出）；**WS** 双向、二进制、低延迟，适合协作/聊天/游戏；**轮询** 兜底（代理/老环境/极简后台），长轮询模拟推送但延迟与开销大。
- 选型决策树：需要客户端主动高频发消息 → WS；只需服务端推 + 想要 HTTP 生态（鉴权、CDN、网关兼容）→ SSE；状态更新频率 < 1 次/分钟且实时性要求低 → 轮询（TanStack Query 的 refetchInterval）。
- **降级链设计**：WS 失败（企业代理拦截 upgrade）→ SSE → 长轮询。降级探测：WS connect 超时 3s 或三次失败自动降级，SSE 同理。同一套「消息处理器」接口消费三种通道——上层状态逻辑不感知通道。
- SSE 的实战细节：`EventSource` 不支持自定义 header（鉴权用 cookie 或 query token）；`Last-Event-ID` 由浏览器自动带上（服务端据此续传，天然实现 ZSM-727 的追平）；Nginx 需关闭 `proxy_buffering` 否则消息攒包延迟。
- 追问钩子：HTTP/2 下 SSE 的连接数限制消失（多路复用），SSE 的适用面扩大；但 HTTP/2 的队头阻塞在丢包率高的移动网络上会让 SSE 延迟抖动——弱网场景 WS 仍占优。

```javascript
// 统一推送接口 + 降级链
function createPushChannel(handlers, url) {
  // 统一接口：{ on(type, fn), close() }
  async function connect() {
    try {
      return await connectWs(url, handlers)              // 1) WS 优先
    } catch {}
    try {
      return await connectSse(url, handlers)             // 2) SSE 降级
    } catch {}
    return connectPolling(url, handlers)                 // 3) 长轮询兜底
  }
  return { connect, on: handlers.on, close: handlers.close }
}

// SSE 实现：Last-Event-ID 续传
function connectSse(url, { on }) {
  return new Promise((resolve, reject) => {
    const es = new EventSource(`${url}?token=${getToken()}`)   // token 走 query（无 header 能力）
    es.onopen = () => resolve({
      on: (type, fn) => es.addEventListener(type, (e) => fn(JSON.parse(e.data))),
      close: () => es.close(),
    })
    es.onerror = () => reject(new Error('sse failed'))   // 触发下一级降级
    // 浏览器自动带 Last-Event-ID：服务端据此补发缺口
  })
}

// 轮询兜底：游标 + 退避
function connectPolling(url, { on }) {
  let cursor = null
  let interval = 5000
  const timer = setInterval(async () => {
    try {
      const { events, nextCursor } = await fetch(`${url}/events?cursor=${cursor}`).then((r) => r.json())
      events.forEach((e) => on(e.type, () => {})(e) ?? on(e.type, (fn) => fn(e)))
      cursor = nextCursor
      interval = 5000                                     // 成功重置
    } catch {
      interval = Math.min(interval * 2, 60000)            // 失败退避
    }
  }, interval)
  return { on, close: () => clearInterval(timer) }
}
```
