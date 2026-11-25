---
title: [V3-428] 笔试：手写异步组件 hover 预取（路由级代码分割）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-428：笔试：手写异步组件 hover 预取（路由级代码分割）
**答**：实现 `prefetchRoute(name)` 与导航菜单的 hover 预取：hover 时调用 import() 触发 chunk 加载（幂等，重复 hover 不重复加载）；导航点击时组件已缓存（defineAsyncComponent 复用同一 factory）；失败静默（点击时再正常加载）。

```javascript
const factories = new Map()
function prefetchRoute(name) {
  const route = routeMap[name]
  if (!route || factories.has(name)) return // 幂等
  const p = route.component().catch(() => {}) // 失败静默，点击时重试
  factories.set(name, p)
  return p
}
const routes = Object.fromEntries(
  Object.entries(routeMap).map(([name, r]) => [
    name, { ...r, component: defineAsyncComponent(() => factories.get(name) || r.component()) }
  ])
)
// 菜单组件
// <a @mouseenter="prefetchRoute('detail')" @click="router.push('/detail')">详情</a>
```
**评分点**：
- import() 结果缓存 Map（重复 hover 只发一次请求）。
- defineAsyncComponent 复用同一缓存 promise（核心：预取与消费一致）。
- 失败 catch 掉不弹错，点击路径兜底。
- 能说明 defineAsyncComponent 会把同一 factory 的 pending promise 复用。
