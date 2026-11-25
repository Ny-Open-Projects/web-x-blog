---
title: [WCN-125] React Compiler 的自动 memo 是怎么做的？为什么说它是"折中路线"？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-125：React Compiler 的自动 memo 是怎么做的？

**答**：
- 编译器静态分析组件函数：识别哪些变量/表达式不依赖任何可变状态，把它们提升为缓存值（等价 useMemo/useCallback 自动插入），组件间跳过不变的子树渲染。
- 原理：基于 mutable range 分析——每个值追踪"是否被写、是否逃逸"，不可变且依赖未变则复用上次结果；effect/dispatch 等已知稳定 API 白名单豁免。
- 折中路线的含义：保留 VDOM + 重跑组件模型，用编译期缓存把"重跑"降为"缓存命中短路"；与 Solid/Vapor 的"根本不重跑"相比，上限不同但侵入性最小（代码零改动）。
- 限制：高度动态的 props（新数组/对象每帧新建）仍会失效——编译器按 React 语义必须重算；极端性能场景仍要手动优化。
- 工程接入：babel-plugin-react-compiler；配合 ESLint 规则提示不兼容模式（如运行时改 props）。

```jsx
// 源码（无 memo/useCallback）
function ProductList({ items, onSelect }) {
  const total = items.reduce((s, i) => s + i.price, 0);   // 自动 useMemo
  return <List items={items} onSelect={onSelect} total={total} />;
}

// 编译产物（示意）
function ProductList(t0) {
  const $ = useMemo(() => [t0.items, t0.onSelect]);
  const total = useMemo(() => t0.items.reduce((s, i) => s + i.price, 0), [t0.items]);
  const ListMemo = useMemo(() => <List items={t0.items} onSelect={t0.onSelect} total={total} />, $);
  return ListMemo;   // 依赖未变 → 直接复用上次元素（跳过子树重渲染）
}
```
