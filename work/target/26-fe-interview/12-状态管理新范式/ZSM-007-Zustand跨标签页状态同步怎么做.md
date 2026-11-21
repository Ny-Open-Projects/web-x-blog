---
title: [ZSM-007] 用 Zustand 怎么实现跨标签页状态同步？storage 事件和 BroadcastChannel 有什么差别？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-007：用 Zustand 怎么实现跨标签页状态同步？storage 事件和 BroadcastChannel 有什么差别？
**答**：
- 两条路：① persist + localStorage，监听 `storage` 事件（其他标签页写入才触发，本页不触发）调 `persist.rehydrate()`；② 自定义中间件用 BroadcastChannel 广播 patch。
- storage 事件只能拿到字符串快照，粒度粗；BroadcastChannel 是结构化消息（不序列化），可传 patch，更灵活且不依赖持久化。
- 收到远端更新时用 `setState(patch, false)` 合并，注意加来源标记防自己广播给自己的回声。
- 典型场景：登录态、主题、IM 未读数在多标签页保持一致。

```javascript
const ch = new BroadcastChannel('app-store')
let self = false

function syncStore(useStore) {
  ch.onmessage = e => {           // 其他标签页的 patch
    useStore.setState(e.data, false)
  }
  useStore.subscribe(state => {   // 本页变化广播出去
    ch.postMessage(state)
  })
}
// 版本2：localStorage 方案
// window.addEventListener('storage', e => { if (e.key === 'cart') useStore.persist.rehydrate() })
```
