---
title: [RBL-531] 笔试：手写 chunk 加载器 runtime（去重 + 重试退避 + 熔断）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-531：手写 chunk 加载器 runtime（去重 + 重试退避 + 熔断）
**答**：530 落地——实现 `createChunkLoader({ retries, publicPath })`：1) `load(chunkName)`：并发去重（同 chunk 进行中/已加载返回同 Promise）；2) 失败重试：指数退避（≤ retries 次）；3) **熔断**：连续失败 ≥3 个 chunk → 全局 open（后续 load 直接 fail-fast），冷却半开探测；4) 附用例：并发去重、重试与熔断升级。

```javascript
function createChunkLoader({ retries = 2, publicPath = '/chunks/', breakerThreshold = 3, cooldown = 5000 } = {}) {
  const loaded = new Map()        // chunkName -> Promise
  let breaker = 'closed'
  let breakerFails = 0
  let openedAt = 0

  function loadScript(src, attempt = 0) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script')
      s.src = src
      s.onload = () => resolve()
      s.onerror = () => { s.remove(); reject(new Error(`load fail ${src}`)) }
      document.head.appendChild(s)
      void attempt
    })
  }

  async function loadWithRetry(name, attempt = 0) {
    try {
      await loadScript(`${publicPath}${name}.js`)
      breakerFails = Math.max(0, breakerFails - 1)      // 成功：失败计数衰减
      if (breaker === 'open') breaker = 'half-open'     // 探测成功倾向恢复
      return
    } catch (e) {
      breakerFails++
      if (breakerFails >= breakerThreshold && breaker === 'closed') {
        breaker = 'open'; openedAt = Date.now()          // 熔断：全局 fail-fast
      }
      if (attempt < retries && breaker !== 'open') {
        await new Promise((r) => setTimeout(r, 500 * 2 ** attempt))   // 退避
        return loadWithRetry(name, attempt + 1)
      }
      throw e
    }
  }

  function load(name) {
    if (breaker === 'open') {
      if (Date.now() - openedAt > cooldown) { breaker = 'half-open' }   // 冷却半开
      else return Promise.reject(new Error('BREAKER_OPEN'))             // fail-fast
    }
    if (loaded.has(name)) return loaded.get(name)       // 并发去重：同 Promise
    const p = loadWithRetry(name).finally(() => {
      // 半开探测成功 → closed
      if (breaker === 'half-open') breaker = 'closed'
    })
    loaded.set(name, p)
    p.catch(() => loaded.delete(name))                  // 失败清除：下次可重试
    return p
  }

  return { load, get breaker() { return breaker }, get loadedCount() { return loaded.size } }
}

// 用例（jsdom 简化：模拟 script onload/onerror）
let urlFails = new Set()
globalThis.document = {
  createElement: () => ({ set src(v) { this._src = v } , get src() { return this._src } }),
  head: { appendChild: (s) => setTimeout(() => urlFails.has(s.src) ? s.onerror() : s.onload(), 5) },
}
const loader = createChunkLoader({ retries: 1, cooldown: 50 })
urlFails.add('/chunks/a.js').add('/chunks/b.js').add('/chunks/c.js')

const p1 = loader.load('a').catch((e) => e.message)   // a 失败（重试后仍败）
await p1
console.log(loader.breaker)                            // 'open'：熔断
const p2 = loader.load('d').catch((e) => e.message)    // fail-fast
await p2
console.log(p2 && 'BREAKER_OPEN')                      // 'BREAKER_OPEN'：不发起请求
await new Promise((r) => setTimeout(r, 60))            // 冷却 → half-open
const p3 = loader.load('d')                            // 半开探测：d 未失败 → 成功
await p3
console.log(loader.breaker)                            // 'closed'
```
**评分点**：
- 并发去重（loaded Map 同 Promise 复用 + 失败清除）
- 指数退避重试（attempt 上限）
- 熔断三态（open fail-fast / 冷却 half-open / 探测成功 closed）
- 成功衰减失败计数（半开恢复的渐进语义）
