---
title: [ZSM-309] 笔试：手写微前端 postMessage RPC 封装（超时 + 校验）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-309：手写微前端 postMessage RPC 封装（超时 + 校验）
**答**：实现 `createRpc(targetWindow, targetOrigin)`：1) `call(method, payload)` 返回 Promise，带 10s 超时；2) 消息协议 `{ __rpc: true, id, method, payload }` 与响应 `{ __rpc: true, id, result, error }`；3) 校验来源 origin 与消息标记，非法消息忽略；4) 支持对端注册 handler（`on(method, fn)`）自动回包；5) 多个并发调用按 id 正确配对。

```javascript
export function createRpc(targetWindow, targetOrigin) {
  const pending = new Map()   // id → { resolve, reject, timer }
  const methods = new Map()
  let seq = 0

  window.addEventListener('message', (e) => {
    const msg = e.data
    if (!msg || msg.__rpc !== true) return
    if (e.origin !== targetOrigin) return                 // 来源校验
    if (msg.result !== undefined || msg.error !== undefined) {
      const p = pending.get(msg.id)
      if (!p) return
      clearTimeout(p.timer)
      pending.delete(msg.id)
      msg.error ? p.reject(new Error(msg.error)) : p.resolve(msg.result)
    } else if (methods.has(msg.method)) {                 // 对端请求 → 回包
      Promise.resolve(methods.get(msg.method)(msg.payload))
        .then((result) => post({ __rpc: true, id: msg.id, result }),
              (error) => post({ __rpc: true, id: msg.id, error: String(error?.message ?? error) }))
    }
  })

  function post(msg) { targetWindow.postMessage(msg, targetOrigin) }

  return {
    call(method, payload, timeoutMs = 10_000) {
      const id = ++seq
      return new Promise((resolve, reject) => {
        const timer = setTimeout(() => {
          pending.delete(id); reject(new Error(`rpc timeout: ${method}`))
        }, timeoutMs)
        pending.set(id, { resolve, reject, timer })
        post({ __rpc: true, id, method, payload })
      })
    },
    on(method, fn) { methods.set(method, fn) },
  }
}
```
**评分点**：
- origin 双向校验（发送 targetOrigin、接收 e.origin），不能填 '*'
- id 配对 + 超时后从 pending 删除（超时后迟到响应不再 resolve）
- handler 异常要捕获并回 error 包，不能让对端悬挂等待
- 协议标记 __rpc + 结构校验，防止任意第三方消息误入
