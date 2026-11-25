---
title: [WCN-248] 细粒度更新为什么让 Signals 性能高（对比 VDOM diff）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-248：细粒度更新为什么让 Signals 性能高（对比 VDOM diff）？
**答**：
- VDOM：状态变 → 重渲染组件树 → diff → 打补丁（比例于树大小）。
- Signals：状态变 → 精确知道哪些订阅节点 dirty → 只执行这些节点的直接 DOM 写（比例于受影响节点数）。
- 编译器加持（Solid）：绑定表达式预编译为定向更新函数，连 diff 都省了。
- 代价：编程模型更受限（表达式需要被追踪），逃逸 hatch（untracked）必备。

```javascript
// Solid 编译产物形态
const [count, setCount] = createSignal(0);
// <div>{count()}</div> 编译为：
createEffect(() => dom.textContent = String(count()));   // 定向写，无 diff
r
```
