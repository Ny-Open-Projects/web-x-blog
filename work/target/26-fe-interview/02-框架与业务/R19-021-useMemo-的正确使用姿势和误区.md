---
title: [R19-021] useMemo 的正确使用姿势和误区？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-021：useMemo 的正确使用姿势和误区？
**答**：
- 语义：缓存一次昂贵计算的结果，依赖不变就复用上一次的值。
- 第二个重要用途：缓存对象/数组的引用，让依赖引用相等性的下游（memo 子组件、其他 effect）不失效。
- 误区一：所有计算都包 useMemo，缓存本身有开销，简单计算不值得。
- 误区二：把改变 state 的逻辑放进 useMemo，它必须是纯计算。

```jsx
const HeavyList = memo(function HeavyList({ items }) {
  return <ul>{items.map((i) => <li key={i.id}>{i.text}</li>)}</ul>;
});

function ProductList({ products, keyword }) {
  // 依赖不变时 filtered 引用稳定，HeavyList 不会白渲染
  const filtered = useMemo(
    () => products.filter((p) => p.name.includes(keyword)),
    [products, keyword]
  );

  return <HeavyList items={filtered} />;
}
```
