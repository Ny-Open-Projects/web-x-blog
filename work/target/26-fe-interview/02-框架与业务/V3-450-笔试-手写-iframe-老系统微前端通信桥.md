---
title: [V3-450] 笔试：手写 iframe 老系统的通信桥（双向消息 + 超时 + 鉴权）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-450：笔试：手写 iframe 老系统的通信桥（双向消息 + 超时 + 鉴权）
**题**：实现 `createBridge(iframeEl, targetOrigin)`：call(method, data, timeout) 返回 Promise；子页面 reply(method) 注册处理器；消息带 requestId 配对响应；校验 event.origin 防恶意消息；超时 reject 并清理配对表。

```javascript
function createBridge(iframeEl, targetOrigin) {
  const pending = new Map()
  const handlers = new Map()
  window.addEventListener('message', (event) => {
    if (event.origin !== targetOrigin) return       // 鉴权：严格校验来源
    const { type, requestId, payload, error } = event.data || {}
    if (requestId && pending.has(requestId)) {      // 响应配对
      const { resolve, reject, timer } = pending.get(requestId)
      clearTimeout(timer); pending.delete(requestId)
      error ? reject(new Error(error)) : resolve(payload)
    } else if (type && handlers.has(type)) {        // 请求处理
      const result = handlers.get(type)(payload)
      Promise.resolve(result).then(r =>
        iframeEl.contentWindow.postMessage({ requestId, payload: r }, targetOrigin))
    }
  })
  function call(method, data, timeout = 5000) {
    return new Promise((resolve, reject) => {
      const requestId = crypto.randomUUID()
      const timer = setTimeout(() => { pending.delete(requestId); reject(new Error('bridge timeout')) }, timeout)
      pending.set(requestId, { resolve, reject, timer })
      iframeEl.contentWindow.postMessage({ type: method, requestId, payload: data }, targetOrigin)
    })
  }
  function reply(method, fn) { handlers.set(method, fn) }
  return { call, reply }
}
```
**评分点**：
- origin 严格校验（'*' 直接扣分——安全核心）。
- requestId 配对响应 + pending 表清理（超时/响应双向）。
- 超时 reject 并清 timer。
- reply 的结果 Promise 化（异步处理器支持）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-de890159-34d0-4b46-b3ec-7c7139345a6b-cwd'; fi
exit "$__zcode_status"
