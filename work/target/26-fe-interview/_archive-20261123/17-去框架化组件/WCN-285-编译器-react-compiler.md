---
title: [WCN-285] React Compiler 的编译目标与信号系的本质区别？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-285：React Compiler 的编译目标与信号系的本质区别？
**答**：
- React Compiler 不消除 VDOM：自动插入 memoization（组件/钩子级），减少不必要的重渲染。
- 信号系：改变更新模型（订阅直达 DOM）；React Compiler：保留模型优化成本（重渲染变便宜）。
- 边界：Compiler 依赖「规则遵守」（不违反纯函数/hooks 规则），违反则静默失效——需要 eslint 插件兜底。
- 评估：重渲染热点组件收益明显；深度交互（高频 setState）仍受 VDOM 上限约束。

```javascript
// Compiler 自动产物（示意）
function Price({ items }) {
  const total = _memo(() => items.reduce((s, i) => s + i.price, 0), [items]); // 自动 memo
  return _memo(<b>{total}</b>, [items]);
}
r
```
