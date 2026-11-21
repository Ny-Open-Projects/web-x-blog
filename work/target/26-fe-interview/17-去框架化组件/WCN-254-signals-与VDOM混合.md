---
title: [WCN-254] 「Signals + VDOM」混合架构（如 React signals 包）的原理与边界？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-254：「Signals + VDOM」混合架构（如 React signals 包）的原理与边界？
**答**：
- 信号直接订阅 DOM 节点（绕过 React 渲染）+ React 组件仍走 VDOM——两通道并存。
- 性能收益：高频局部更新（拖拽/输入）走信号通道不触发 React 渲染。
- 边界风险：两通道状态不一致（React 渲染覆盖信号直写的 DOM）——写路径必须单一所有权。
- 适用：性能热区组件用信号绑定，业务流仍走 React——渐进混用。

```javascript
// @preact/signals-react：signal 直接绑定到 JSX 文本节点
function Counter() {
  return <span>{count.value}</span>;   // count 变化只更新这个 span，不触发组件重渲染
}
r
```
