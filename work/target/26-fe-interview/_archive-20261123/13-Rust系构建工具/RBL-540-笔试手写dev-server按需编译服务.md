---
title: [RBL-540] 笔试：手写 dev server 按需编译服务（ETag 协商 + 按需闭包）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-540：手写 dev server 按需编译服务（ETag 协商 + 按需闭包）
**需求**：539 落地——实现 `createDevServer({ graph, compile })`：1) `handleRequest(path, ifNoneMatch)`：请求模块 → 按需编译（依赖闭包只编译缺失者）→ ETag（内容 hash）→ 304 协商缓存；2) `hmrPush(changedIds)`：HMR 推送（变更列表 + 新 hash）；3) 附用例：协商缓存命中与按需编译。

```javascript
import { createHash } from 'crypto'

function createDevServer({ graph, compile }) {
  const etags = new Map()        // moduleId -> etag
  const etagOf = (code) => createHash('sha256').update(code).digest('hex').slice(0, 16)
  let wsListeners = new Set()

  async function handleRequest(path, ifNoneMatch) {
    const moduleId = path.replace(/^\//, '').replace(/\?.*$/, '')
    // 按需编译：依赖闭包中未编译的先编译
    const closure = graph.closure(moduleId)                       // 依赖闭包
    for (const m of closure) {
      if (!graph.isCompiled(m)) await compile(m)
    }
    const code = graph.getOutput(moduleId)
    const etag = etagOf(code)
    etags.set(moduleId, etag)
    // 304 协商缓存
    if (ifNoneMatch === etag) {
      return { status: 304, etag }
    }
    return { status: 200, etag, body: code, headers: { 'Cache-Control': 'no-cache' } }
  }

  function hmrPush(changedIds) {
    const updates = changedIds.map((id) => {
      const code = graph.getOutput(id)
      const etag = etagOf(code)
      etags.set(id, etag)
      return { id, etag }
    })
    const updateHash = etagOf(JSON.stringify(updates))
    wsListeners.forEach((fn) => fn({ type: 'hmr', updateHash, updates }))   // 推送变更列表+hash
    return { updateHash, updates }
  }

  return {
    handleRequest, hmrPush,
    onWs: (fn) => (wsListeners.add(fn), () => wsListeners.delete(fn)),
    etags: () => Object.fromEntries(etags),
  }
}

// 用例
const graph = {
  closure: (m) => ['dep1', 'dep2', m],
  isCompiled: (m) => compiled.has(m),
  getOutput: (m) => `code-of-${m}@${compiled.get(m) ?? 0}`,
}
const compiled = new Map()
const server = createDevServer({ graph, compile: async (m) => { compiled.set(m, 1) } })

// 首次请求：按需编译 dep1/dep2/main
const r1 = await server.handleRequest('main.js', undefined)
console.log(r1.status, r1.etag.length)             // 200 16
console.log([...compiled.keys()])                  // ['dep1','dep2','main.js']：闭包按需编译

// 二次请求：304 协商缓存
const r2 = await server.handleRequest('main.js', r1.etag)
console.log(r2.status)                             // 304：零传输

// HMR 推送
server.onWs((msg) => console.log('push', msg.type, msg.updates.length))
graph.getOutput = (m) => `code-of-${m}@v2`
server.hmrPush(['main.js'])                        // push hmr 1
```
**评分点**：
- 按需编译（闭包缺失者先编译——模块级 lazy）
- ETag 协商缓存（304 零传输 + no-cache 语义）
- HMR 推送（变更列表 + updateHash）
- dev/build 模块图一致性意识
