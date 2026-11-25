---
title: [WCN-068] Signals 与 VDOM 更新机制的对比：细粒度更新到底省了什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-068：Signals 与 VDOM 更新机制的对比：细粒度更新到底省了什么？

**答**：
- VDOM 路径：setState → 重跑组件函数（或重渲染子树）→ 新 VDOM → diff → 最小 DOM patch。成本在"重跑 + diff"，即使真实变化只有文本节点。
- Signals 路径：signal 写入 → 脏标记传播 → 直接执行绑定该 signal 的"更新函数"（改文本/属性/类名）。没有重跑、没有 diff、没有中间树。
- 省的三样东西：① 计算成本（不重跑组件/表达式链，computed 惰性）；② 比对成本（无 diff）；③ 更新粒度成本（只触碰受影响节点，GC 压力小）。
- VDOM 并非劣势全无：声明式心智简单、渲染函数可预测、生态调试工具成熟；Signals 的心智成本在于依赖是隐式的（读哪里追哪里），泄漏/过度触发要靠工具检测。
- 混合趋势：React 19 编译器自动 memo 缓解 VDOM 成本；Vue Vapor/Svelte 用编译器把"细粒度"静态化；两者趋同于"运行时少做事"。

```javascript
// 直改绑定：等价 VDOM "diff 后的结果"，但没有中间过程
const el = document.querySelector('#price');
effect(() => { el.textContent = format(price.value); });
// price.value = 99 → 一步到位，仅这一个函数执行
```
