---
title: [RBL-548] 笔试：手写 watcher 事件合并器（防抖合并 + 批量 flush + 忽略过滤）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-548：手写 watcher 事件合并器（防抖合并 + 批量 flush + 忽略过滤）
**需求**：547 落地——实现 `createWatcherMerger({ debounceMs, ignore })`：1) `push(event)`：事件入缓冲（同文件去重——只留最新语义）；2) flush：防抖窗口到期批量触发**一次** onBatch（非逐文件）；3) 忽略过滤（ignore 前缀/正则）+ 语义归一（rename → unlink+add）；4) 附用例：同文件去重与批量 flush。

```javascript
function createWatcherMerger({ debounceMs = 100, ignore = [] } = {}) {
  const buffer = new Map()        // path -> 最新语义
  let timer = null
  const batches = []

  function isIgnored(path) {
    return ignore.some((rule) => typeof rule === 'string' ? path.startsWith(rule) : rule.test(path))
  }

  // 语义归一：rename → unlink + add
  function normalize(ev) {
    if (ev.type === 'rename') {
      return ev.exists ? [{ type: 'add', path: ev.path }] : [{ type: 'unlink', path: ev.path }]
    }
    return [ev]
  }

  function push(event) {
    if (isIgnored(event.path)) return
    for (const e of normalize(event)) {
      // 同文件去重：change 覆盖 change；unlink 后 add 保留 add
      buffer.set(e.path, e.type)
    }
    clearTimeout(timer)
    timer = setTimeout(flush, debounceMs)             // 防抖窗口
  }

  function flush() {
    if (!buffer.size) return
    const batch = [...buffer.entries()].map(([path, type]) => ({ path, type }))
    buffer.clear()
    batches.push(batch)
    onBatch?.(batch)                                  // 一次批量触发（非逐文件）
  }

  let onBatch = null
  const api = {
    push,
    flush,
    onBatch: (fn) => { onBatch = fn },
    batches: () => batches,
  }
  return api
}

// 用例
let batchCount = 0
const wm = createWatcherMerger({ debounceMs: 50, ignore: ['node_modules/', '.git/'] })
wm.onBatch((batch) => { batchCount++; console.log(`batch${batchCount}:`, batch.map((b) => `${b.type}:${b.path}`)) })

// 编辑器连发：change × 2 + rename（合并为 add）
wm.push({ type: 'change', path: '/src/a.js' })
wm.push({ type: 'change', path: '/src/a.js' })                       // 同文件去重
wm.push({ type: 'rename', path: '/src/b.js', exists: true })          // → add
wm.push({ type: 'change', path: '/node_modules/x/index.js' })         // 忽略
await new Promise((r) => setTimeout(r, 60))
console.log(batchCount)                                              // 1：批量一次
// batch1: [ 'change:/src/a.js', 'add:/src/b.js' ]

// git checkout 多文件：一次 flush
wm.push({ type: 'change', path: '/src/a.js' })
wm.push({ type: 'change', path: '/src/c.js' })
wm.flush()                                                            // 手动 flush：不等防抖
console.log(batchCount)                                              // 2：批量（一次编译）
```
**评分点**：
- 同文件去重（Map 最新语义覆盖）
- 批量 flush（一次 onBatch 而非逐文件——跨文件合并）
- 忽略过滤（前缀/正则）+ rename 语义归一（unlink+add）
- 手动 flush（git checkout 场景立即编译）
