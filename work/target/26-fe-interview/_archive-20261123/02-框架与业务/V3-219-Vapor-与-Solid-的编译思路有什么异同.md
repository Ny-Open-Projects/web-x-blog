---
title: [V3-219] Vapor 与 Solid 的编译思路有什么异同？Vue Vapor 的独特取舍是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-219：Vapor 与 Solid 的编译思路有什么异同？Vue Vapor 的独特取舍是什么？
**答**：
- 共同点：都依赖"模板/JSX 静态分析"定位动态点，运行时都是"细粒度订阅 → 定向 DOM 更新"，无组件级重渲染。
- 差异 1（响应式驱动）：Solid 是同步细粒度（写即更新）；Vue Vapor 仍走 Vue 的**批量调度队列**，天然合并更新。
- 差异 2（兼容性）：Vue Vapor 保留 VDOM 模式共存（vdom 与 vapor 组件可混用，靠兼容层），Solid 是唯一运行时。
- 差异 3（作用域/生命周期）：Vapor 沿用 Vue 的 effectScope/生命周期体系；Solid 的清理靠 onCleanup 显式注册。
- 取舍结论：Vue 用 Vapor 换性能与体积，但保留"渐进增强"心智——现有组件不改代码可逐步迁移，这是 Vue 系工程哲学。

```javascript
// 同一逻辑两种心智
// Solid：信号更新同步触发（微批）
const [n, setN] = createSignal(0);
createEffect(() => console.log(n.value)); setN(1); // 同步打印 1
// Vue Vapor：写操作进调度队列，同一 tick 多次写合并
const n = ref(0);
watchEffect(() => console.log(n.value));
n.value = 1; n.value = 2; // nextTick 后打印一次 2
// Vapor 组件与 VDOM 组件可混用：父 Vapor 引子 VDOM 组件经 compat 层转换
```
