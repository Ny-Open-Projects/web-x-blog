---
title: [V3-304] Vue 3.5 的 onWatcherCleanup 与旧式 onCleanup 的使用差异是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-304：Vue 3.5 的 onWatcherCleanup 与旧式 onCleanup 的使用差异是什么？
**答**：
- 旧式：`watch(src, (val, old, onCleanup) => onCleanup(fn))`，清理函数作为回调第三个参数注册，只能用在回调内部。
- 新式：`onWatcherCleanup(fn)` 从 `vue` 具名导入，在 watcher 的任何执行上下文（回调、getter 求值中）都可注册，语义是「下一次该 watcher 触发或停止前调用」。
- 适合场景：getter 里创建的临时资源（AbortController、事件订阅）需要在数据变化时取消——以前要靠闭包变量手动管理。
- 两者可并存；组件卸载时二者注册的清理都会执行，等价于 EffectScope 的 stop 语义。
- 追问钩子：`watchEffect` 里 abort 上一次请求的标准写法——见下面代码。
```javascript
import { watchEffect, onWatcherCleanup } from 'vue'
watchEffect(async () => {
  const controller = new AbortController()
  onWatcherCleanup(() => controller.abort()) // 依赖变化/组件卸载时取消
  const res = await fetch(`/api/goods?q=${q.value}`, { signal: controller.signal })
  list.value = await res.json()
})
```
