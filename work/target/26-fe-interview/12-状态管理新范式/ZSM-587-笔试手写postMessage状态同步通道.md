---
title: [ZSM-587] 笔试：手写 postMessage 状态同步通道（含握手、白名单与超时）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-587：手写 postMessage 状态同步通道（含握手、白名单与超时）
**答**：实现 `createBridge({ allowedOrigins, timeout })`：1) `connect(targetWindow, targetOrigin)`：发起握手（hello/ack，500ms 未 ack 报错）——防止向未就绪窗口发消息；2) `send(type, payload)`：仅在握手完成后发送，带 msgId；3) `on(type, handler)`：注册处理，**校验来源在 allowedOrigins 白名单**，未授权来源触发 `onReject` 回调；4) `request(type, payload)`：请求-响应模式（Promise，超时 reject）——基于 request/response 简单封装；5) 附用例模拟握手与请求-响应。

```javascript
function createBridge({ allowedOrigins = [], timeout = 5000 } = {}) {
  const handlers = new Map()
  const pending = new Map()      // msgId -> { resolve, reject, timer }
  let ready = false
  let target = null
  let onReject = null
  let msgId = 0

  function handleMessage(e) {
    if (!allowedOrigins.includes(e.origin)) {
      onReject?.(e.origin, e.data)
      return                                    // 未授权来源丢弃
    }
    const msg = e.data
    if (!msg || msg.ns !== 'bridge') return     // 协议外消息丢弃
    switch (msg.type) {
      case 'hello':                             // 收到握手请求
        e.source.postMessage({ ns: 'bridge', type: 'ack' }, e.origin)
        break
      case 'ack':                               // 握手完成
        ready = true
        break
      case 'request': {
        const handler = handlers.get(msg.body)
        Promise.resolve(handler?.(msg.payload)).then((result) => {
          e.source.postMessage({ ns: 'bridge', type: 'response', msgId: msg.msgId, result }, e.origin)
        })
        break
      }
      case 'response': {
        const p = pending.get(msg.msgId)
        if (p) { clearTimeout(p.timer); pending.delete(msg.msgId); p.resolve(msg.result) }
        break
      }
      case 'event': {
        handlers.get(msg.body)?.(msg.payload)
        break
      }
    }
  }
  window.addEventListener('message', handleMessage)

  function connect(targetWindow, targetOrigin) {
    target = { win: targetWindow, origin: targetOrigin }
    target.win.postMessage({ ns: 'bridge', type: 'hello' }, targetOrigin)
    return new Promise((resolve, reject) => {
      const t = setTimeout(() => reject(new Error('handshake timeout')), timeout)
      const check = setInterval(() => {
        if (ready) { clearTimeout(t); clearInterval(check); resolve() }
      }, 50)
    })
  }

  function send(type, payload) {
    if (!ready) throw new Error('bridge not ready')
    target.win.postMessage({ ns: 'bridge', type: 'event', body: type, payload }, target.origin)
  }

  function on(type, handler) { handlers.set(type, handler); return () => handlers.delete(type) }

  function request(type, payload) {
    return new Promise((resolve, reject) => {
      const id = ++msgId
      const timer = setTimeout(() => {
        pending.delete(id)
        reject(new Error(`request ${type} timeout`))
      }, timeout)
      pending.set(id, { resolve, reject, timer })
      target.win.postMessage({ ns: 'bridge', type: 'request', msgId: id, body: type, payload }, target.origin)
    })
  }

  return { connect, send, on, request, set onReject(fn) { onReject = fn } }
}

// 用例（iframe 侧作为 client）
const bridge = createBridge({ allowedOrigins: ['https://parent.example.com'] })
bridge.onReject = (origin) => console.warn('rejected from', origin)
bridge.connect(parent, 'https://parent.example.com')
  .then(() => bridge.request('getUser', { id: 1 }))
  .then((user) => console.log(user))
  .catch((e) => console.error(e.message))
```
**评分点**：
- 握手 hello/ack + 超时（防止向未就绪窗口丢消息）
- origin 白名单校验与拒绝回调（安全边界）
- request-response 的 msgId 配对与超时 reject
- 协议外消息（无 ns / 结构不符）静默丢弃
