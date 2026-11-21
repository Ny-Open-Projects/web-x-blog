---
title: [ZSM-481] 笔试：手写状态层 Web Worker 镜像
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-481：手写状态层 Web Worker 镜像
**需求**：实现主线程↔Worker 的状态镜像：1) `mirrorToWorker(worker, getState)`：主线程每次 setState 后把状态（或增量 patch）postMessage 给 Worker；2) Worker 侧 `serveWorker(reduce)`：接收 patch 应用到镜像 state，支持 `query` 请求（Worker 内计算重结果回传）；3) 请求协议：`{ id, type: 'patch'|'query', payload }`，响应带同 id；4) 主线程 `queryInWorker(fn, args)`：Promise 化，超时 5s；5) Worker 状态不能有 DOM 依赖（传输前校验可序列化）。

```javascript
// 主线程侧
export function mirrorToWorker(worker, store) {
  let seq = 0
  const pending = new Map()   // id → { resolve, reject, timer }

  worker.onmessage = ({ data: { id, result, error } }) => {
    const p = pending.get(id)
    if (!p) return
    clearTimeout(p.timer); pending.delete(id)
    error ? p.reject(new Error(error)) : p.resolve(result)
  }

  store.subscribe((_s, _p, patch) => {
    worker.postMessage({ id: ++seq, type: 'patch', payload: patch })   // 增量镜像
  })

  function queryInWorker(fnName, args, timeoutMs = 5000) {
    const id = ++seq
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => { pending.delete(id); reject(new Error('worker timeout')) }, timeoutMs)
      pending.set(id, { resolve, reject, timer })
      worker.postMessage({ id, type: 'query', payload: { fnName, args } })
    })
  }
  return { queryInWorker }
}

// Worker 侧
export function serveWorker(reduce, queries) {
  let mirror = {}
  self.onmessage = ({ data: { id, type, payload } }) => {
    if (type === 'patch') {
      mirror = reduce(mirror, payload)                              // 镜像应用
    } else if (type === 'query') {
      try {
        const result = queries[payload.fnName](mirror, payload.args)
        self.postMessage({ id, result })                             // 可序列化校验由 postMessage 天然强制
      } catch (e) { self.postMessage({ id, error: String(e) }) }
    }
  }
}
```
**评分点**：
- 增量镜像协议（patch 优先，减少传输量）+ 双向 id 配对
- query Promise 化 + 超时（Worker 卡死不悬挂主线程）
- postMessage 天然强制可序列化（函数/DOM 传不过去即报错——校验语义说明）
- Worker 重计算与主线程渲染解耦（大列表过滤/统计放 Worker）
