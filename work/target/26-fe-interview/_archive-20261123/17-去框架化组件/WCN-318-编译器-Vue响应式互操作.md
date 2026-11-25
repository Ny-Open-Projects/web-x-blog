---
title: [WCN-318] Vue 的响应式（ref/computed）与自研信号互操作的适配层？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-318：Vue 的响应式（ref/computed）与自研信号互操作的适配层？
**答**：
- 桥接：signal → ref（effect 同步），ref → signal（watch 同步）——双向但防回环。
- 方向选择：信号为源，ref 为投影（单向）——避免双向同步环。
- unref 陷阱：响应式值在模板中自动解包，桥接层要显式处理。
- 清理：双向桥的 effect/watch 都随组件卸载释放。

```javascript
function signalToRef(sig) {
  const r = ref(sig.value);
  const stop = effect(() => { r.value = sig.value; });       // 单向投影
  onUnmounted(stop);
  return r;
}
r
```
