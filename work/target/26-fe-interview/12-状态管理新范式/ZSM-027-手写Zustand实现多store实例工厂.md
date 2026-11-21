---
title: [ZSM-027] 笔试：手写 Zustand 多 store 实例工厂（按业务 id 创建独立 store）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-027：手写 Zustand 多 store 实例工厂（按业务 id 创建独立 store）

**题目要求**：
- 场景：IM 页面每个会话一个独立 store（未读数、消息列表）。实现 `createSessionStore(sessionId)`，重复创建返回同一实例（缓存复用）。
- 提供 `destroySessionStore(sessionId)`：清缓存、断开订阅，防内存泄漏。
- 保证并发调用幂等。

```javascript
import { create } from 'zustand'

const registry = new Map()

export function createSessionStore(sessionId) {
  if (registry.has(sessionId)) return registry.get(sessionId)

  const store = create((set, get) => ({
    sessionId,
    messages: [],
    unread: 0,
    push: msg => set(s => ({
      messages: [...s.messages, msg],
      unread: msg.from !== 'me' ? s.unread + 1 : s.unread,
    })),
    markRead: () => set({ unread: 0 }),
    _subs: new Set(), // 组件订阅计数（示意）
  }))
  registry.set(sessionId, store)
  return store
}

export function destroySessionStore(sessionId) {
  const store = registry.get(sessionId)
  if (!store) return
  store.destroy?.()            // zustand 提供的销毁（v4: api.destroy）
  registry.delete(sessionId)   // 释放引用，GC 掉消息数组
}

// 组件内：const store = createSessionStore(id); const unread = store(s => s.unread)
```

**评分点**：
- 用 Map 做实例缓存，重复创建返回同一引用（幂等）。
- destroy 同时清理 store 内部订阅与注册表条目，防内存泄漏。
- 工厂闭包持有 sessionId，store 自带归属信息。
- 能指出内存泄漏风险：只删 Map 不 destroy，消息数组仍被闭包持有。
