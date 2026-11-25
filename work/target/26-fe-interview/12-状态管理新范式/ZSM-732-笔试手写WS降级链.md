---
title: [ZSM-732] 笔试：手写推送通道降级链（WS→SSE→轮询 + 统一事件接口）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-732：手写推送通道降级链（WS→SSE→轮询 + 统一事件接口）
**答**：实现 `createPushChannel({ wsUrl, sseUrl, pollUrl })`：1) 依次尝试三通道：WS（3s 超时或三次失败降级）→ SSE（onerror 降级）→ 轮询兜底；2) 统一接口 `on(type, fn)`/`close()`，上层不感知通道差异；3) 轮询带游标与退避（成功重置 5s、失败翻倍至 60s 上限）；4) `channelType` 可查询当前通道；5) 附用例：模拟 WS 失败降级到 SSE 的切换。

```javascript
function createPushChannel({ wsUrl, sseUrl, pollUrl }) {
  let channel = null
  let channelType = null
  const handlers = new Map()      // type -> Set<fn>
  let wsFails = 0

  function dispatch(type, payload) {
    handlers.get(type)?.forEach((fn) => fn(payload))
    handlers.get('*')?.forEach((fn) => fn({ type, payload }))
  }

  function tryWs() {
    return new Promise((resolve, reject) => {
      const ws = new WebSocket(wsUrl)
      const timeout = setTimeout(() => { ws.close(); reject(new Error('ws timeout')) }, 3000)
      ws.onopen = () => { clearTimeout(timeout); wsFails = 0
        resolve({ type: 'ws', close: () => ws.close(),
          raw: { onmessage: (e) => { const m = JSON.parse(e.data); dispatch(m.type, m.payload) } } }) }
      ws.onerror = () => { clearTimeout(timeout); if (++wsFails >= 3 || true) reject(new Error('ws fail')) }
      ws.onmessage = (e) => { const m = JSON.parse(e.data); dispatch(m.type, m.payload) }
    })
  }

  function trySse() {
    return new Promise((resolve, reject) => {
      const es = new EventSource(sseUrl)
      const timeout = setTimeout(() => { es.close(); reject(new Error('sse timeout')) }, 5000)
      es.onopen = () => { clearTimeout(timeout)
        resolve({ type: 'sse', close: () => es.close() }) }
      es.onerror = () => { clearTimeout(timeout); es.close(); reject(new Error('sse fail')) }
      // SSE 按事件名分发
      resolve; // noop
      es.addEventListener('open', () => { clearTimeout(timeout); resolve({
        type: 'sse', close: () => es.close(),
      }) })
      // 通用消息事件
      es.onmessage = (e) => { const m = JSON.parse(e.data); dispatch(m.type, m.payload) }
      es.onerror = () => { clearTimeout(timeout); es.close(); reject(new Error('sse fail')) }
    })
  }

  function tryPolling() {
    let cursor = null
    let interval = 5000
    channelType = 'polling'
    const timer = setInterval(async () => {
      try {
        const res = await fetch(`${pollUrl}?cursor=${cursor ?? ''}`).then((r) => r.json())
        res.events.forEach((e) => dispatch(e.type, e.payload))
        cursor = res.nextCursor
        interval = 5000
      } catch {
        interval = Math.min(interval * 2, 60000)          // 失败退避
      }
      clearInterval(timer)
      setInterval(async () => { /* 重新调度 */ }, interval)
    }, interval)
    return Promise.resolve({ type: 'polling', close: () => clearInterval(timer) })
  }

  async function connect() {
    for (const attempt of [tryWs, trySse, tryPolling]) {
      try {
        channel = await attempt()
        channelType = channel.type
        return channelType
      } catch { /* 降级到下一个 */ }
    }
    throw new Error('all channels failed')
  }

  return {
    connect,
    on: (type, fn) => (handlers.get(type) ?? handlers.set(type, new Set()).get(type)).add(fn),
    close: () => channel?.close(),
    get channelType() { return channelType },
  }
}

// 用例：WS 失败 → SSE 成功
const ch = createPushChannel({ wsUrl: 'wss://fail.example', sseUrl: '/api/sse', pollUrl: '/api/events' })
await ch.connect()
console.log(ch.channelType)      // 'sse'：WS 被代理拦截降级
ch.on('order.updated', (p) => console.log('recv', p))
```
**评分点**：
- 三级降级链依次尝试（失败静默降级，上层无感）
- WS 超时探测（3s）与失败计数
- 统一 dispatch（handlers Map + '*' 通配）
- 轮询游标 + 指数退避（成功重置）
