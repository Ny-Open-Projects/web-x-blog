---
title: [WCN-066] Vue 的 ref/reactive 与 Signals 提案是什么关系？Vue 3.4+ 做了哪些对齐优化？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-066：Vue 的 ref/reactive 与 Signals 提案是什么关系？Vue 3.4+ 做了哪些对齐优化？

**答**：
- Vue 的响应式系统就是"信号语义"的先驱：`ref` ≈ signal（.value 读写）、`computed` ≈ computed、`watchEffect` ≈ effect；Signals 提案里多位作者来自 Vue/Solid 团队，语义大量借鉴 Vue。
- 差异：Vue 额外有 `reactive`（Proxy 深层对象响应式，属性级追踪），Signals 标准提案聚焦原始值/浅层信号；Vue 与渲染器（VDOM）耦合，提案目标是框架无关原语。
- Vue 3.4 重构响应式：props 解构响应式、`defineModel` 简化；3.5 引入"响应式属性重构"（dependency tracking 优化，大规模响应式更新提速 ~40%）与 `useTemplateRef`。
- 对齐趋势：Vue 官方表态愿意以提案为底层原语重构实现，保持 API 兼容；同时 `onCleanup`、`pauseTracking` 等细节在提案中均有对应物。
- 追问钩子：Vue 的 `computed` 缓存、脏标记、循环依赖告警与 Signals 规范条款几乎一一对应，可对比回答。

```javascript
// Vue：signal 语义的同构对照
import { ref, computed, watchEffect } from 'vue';
const count = ref(1);                       // ≈ signal(1)
const double = computed(() => count.value * 2); // ≈ computed
const stop = watchEffect(() => {            // ≈ effect（返回 disposer）
  console.log(double.value);
});
count.value = 2;                            // 批处理：一次微任务内合并
stop();                                     // 手动释放
```
