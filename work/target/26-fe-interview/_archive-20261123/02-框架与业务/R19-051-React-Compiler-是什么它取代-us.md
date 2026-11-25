---
title: [R19-051] React Compiler 是什么？它取代 useMemo 吗？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-051：React Compiler 是什么？它取代 useMemo 吗？
**答**：
- React Compiler（原名 React Forget）在编译期自动分析组件与 Hook，插入等价的缓存逻辑。
- 理想情况下不再手写 useMemo、useCallback、memo，代码更简洁且不会漏写依赖。
- 它基于对代码正确性的静态分析：无法证明安全的代码会自动放弃优化，不做错误缓存。
- 定位是"让默认渲染足够快"，特殊场景仍可手动优化，两者不冲突。

```jsx
// 编译前：需要手动 memo 化
function ExpensePage({ expenses }) {
  const total = expenses.reduce((sum, e) => sum + e.amount, 0);
  const handleSort = () => sortByAmount(expenses);
  return <Table total={total} onSort={handleSort} />;
}

// 开启 React Compiler 后，构建期自动等价于：
// const total = useMemo(...)
// const handleSort = useCallback(...)
// const Table = memo(...) 的产物级缓存
// 依赖分析不安全时编译器自动放弃优化，保证行为正确
```
