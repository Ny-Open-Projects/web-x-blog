---
title: [ZSM-033] Zustand store 的 destroy 做什么？页面级 store 在路由切换时怎么彻底清理？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-033：Zustand store 的 destroy 做什么？页面级 store 在路由切换时怎么彻底清理？
**答**：
- `api.destroy()` 清空该 store 的全部订阅者（listeners），让组件卸载后不再有残留通知；v4 起 persist 中间件destroy 时不再清 storage。
- 页面级 store 常驻会累积内存：路由卸载时 destroy + 从注册表（Map）删除引用，消息数组、图片缓存随之可被 GC。
- 有 persist 的页面级 store，注销前要手动 `localStorage.removeItem(key)` 或不做 persist。
- 外部资源要自己清理：destroy 不会取消你手动建的定时器、WebSocket，需要在组件 unmount 里单独断开。

```javascript
// 注册表式页面 store
const pageStores = new Map()
function enterPage(routeId) {
  if (!pageStores.has(routeId)) pageStores.set(routeId, createPageStore())
  return pageStores.get(routeId)
}
function leavePage(routeId) {
  const s = pageStores.get(routeId)
  s.destroy()                 // 清订阅
  pageStores.delete(routeId)  // 清引用
}
```
