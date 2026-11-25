---
title: [WCN-563] React Compiler 的「不变性推断」：它如何判断一个对象在渲染间是否变化以决定是否 memo？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-563：React Compiler 的「不变性推断」：它如何判断一个对象在渲染间是否变化以决定是否 memo？

**答**：
- 结论：基于「写操作集合」做数据流分析——若对象在渲染期间无任何写入且其来源稳定，则视为不变，可安全缓存。
- 跟踪每个值的来源：props 直接传入、useState、useMemo 结果、字面量，只有来源变化才重算。
- 遇到「escape hatch」（如对象传给未知函数、ref.current 写入）则降级为保守不优化。
- 追问：为什么 React Compiler 是「折中路线」？（答：它在运行时插入 memo 检查，不如信号精准，但改造成本低）

```javascript
function inferStability(ast) {
  const written = new Set();
  walk(ast, n => { if (n.type === 'AssignmentExpression') written.add(n.left.name); });
  return function isStable(valueNode) {
    const refs = collectRefs(valueNode);
    return refs.every(r => !written.has(r)) && valueNode.origin !== 'unknown-call';
  };
}
// const cfg = { theme } 且 theme 未被写 -> cfg 可 memo
// cfg 被 cfg.x = 1 写入 -> 不可 memo
```
