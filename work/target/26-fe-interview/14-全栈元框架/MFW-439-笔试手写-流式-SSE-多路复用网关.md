---
title: [MFW-439] 笔试：手写 SSE 多路复用网关（单连接多域分发）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-439：SSE 复用网关
**答**：实现 `createSseHub(upstreamFactory)`：1) 服务端：同用户多频道（order/chat/presence）合一条 SSE（浏览器 6 连接限制——多 Tab 场景必爆）；协议 `event: <domain>\ndata: {...}\n\n`；2) 订阅生命周期与页面绑定（Last-Event-ID 重连补发窗口内事件——不丢不重：序号 per-domain）；3) 背压：慢消费者（socket 缓冲超 1MB）→ 该连接降级模式（只推 P0 域+提示刷新——不做无限缓冲）；4) 鉴权随订阅（每 domain 授权检查——复用连接提权防护：新 domain 订阅要重新 can()）；5) 心跳 15s（代理超时防断）+ 平滑重连指数退避。

```javascript
export function sseHandler(user, streams) {
  const stream = new ReadableStream({
    start(ctrl) {
      const sub = perDomainMap()                              // domain → {seq, unsub}
      for (const d of Object.keys(streams)) {
        if (!can (user, d)) continue                          // 复用连接也要逐域授权
        sub[d] = { seq: lastSeq(user, d), off: sources[d].on((ev) => {
          if (++bufBytes(key) > 1MB) enter LimpMode(key)      // 慢消费者降级
          ctrl.enqueue(`id: ${++seq}\nevent: ${d}\ndata: ${JSON.stringify(ev)}\n\n`)
        }) }
      }
      const hb = setInterval(() => ctrl.enqueue(':hb\n\n'), 15_000)
      cleanup = () => { Object.values(sub).forEach(s => s.off()); clearInterval(hb) }
    },
    cancel: cleanup,
  })
  return new Response(stream, { headers: { 'content-type': 'text/event-stream', 'x-accel-buffering': 'no' } })
}
```
**评分点**：
- 单连接多域协议（event 名分域 + per-domain seq——Last-Event-ID 补发不丢不重）
- 复用连接逐域授权（共享通道提权防护——易漏的安全点）
- 慢消费者 LIMP 降级（1MB 阈值——不做无限缓冲 OOM）
- 心跳+禁缓冲头（代理链路存活）
