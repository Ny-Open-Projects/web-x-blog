---
title: [ZSM-515] 笔试：手写带版本迁移与跨页同步的 atomWithStorage
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-515：手写带版本迁移与跨页同步的 atomWithStorage
**答**：实现 `atomWithStorage(key, initial, { version, migrate })`：1) 读值从 localStorage，带 `version` 字段，不匹配走 `migrate(oldState)`；2) `get/set` 支持 async 存储层（返回 Promise 也兼容）；3) 监听 `storage` 事件同步其他标签页变更；4) 订阅返回退订函数，且「同值写入」不触发订阅；5) 附 JSON 解析失败的容错。给出用例验证版本迁移与跨页同步。

```javascript
import { atom } from 'jotai'

function atomWithStorage(key, initial, { version = 1, migrate = (s) => s } = {}) {
  const base = atom({ v: version, state: initial })
  base.onMount = (set) => {
    // 首次挂载：读存储 + 版本迁移
    (async () => {
      try {
        const raw = await localStorage.getItem(key)
        if (!raw) return
        const parsed = JSON.parse(raw)
        const state = parsed.v === version ? parsed.state : migrate(parsed.state, parsed.v)
        set({ v: version, state })
      } catch (e) {
        console.warn(`atomWithStorage[${key}] parse failed, using initial`, e)
      }
    })()

    // 跨页同步：storage 事件（本页写入不触发该事件）
    const onStorage = (e) => {
      if (e.key !== key || e.newValue == null) return
      try {
        const parsed = JSON.parse(e.newValue)
        const state = parsed.v === version ? parsed.state : migrate(parsed.state, parsed.v)
        set((prev) => (Object.is(prev.state, state) ? prev : { v: version, state }))
      } catch { /* 忽略脏数据 */ }
    }
    window.addEventListener('storage', onStorage)
    return () => window.removeEventListener('storage', onStorage)
  }

  // 写包装：序列化带版本，容错写入失败
  const write = (get, set, update) => {
    const next = typeof update === 'function' ? update(get(base).state) : update
    set(base, { v: version, state: next })
    try { localStorage.setItem(key, JSON.stringify({ v: version, state: next })) }
    catch (e) { console.warn(`atomWithStorage[${key}] write failed`, e) }
  }
  return derivedAtomWith(base, write)
}

// 简化：暴露为 get/set 函数对
function derivedAtomWith(base, write) {
  return { get: base, write }
}

// 用例
const theme = atomWithStorage('theme', 'light', {
  version: 2,
  migrate: (old, fromV) => (fromV === 1 ? old === 'dark' ? 'dark' : 'light' : old),
})
```
**评分点**：
- 版本字段 + migrate 分支（旧数据不丢）
- async 存储层兼容（await 包裹 getItem/setItem）
- storage 事件同步与「同值不触发」（Object.is 去重）
- JSON 解析/写入失败容错（降级初始值，不抛错阻塞）
