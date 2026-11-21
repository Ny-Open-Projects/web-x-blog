---
title: [R19-022] useCallback 和 memo 如何配合使用？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-022：useCallback 和 memo 如何配合使用？
**答**：
- memo 让子组件在 props 浅比较不变时跳过重渲染。
- 但函数组件每次渲染都会创建新的内联函数，导致传下去的 props 引用永远不同，memo 失效。
- useCallback 把函数缓存在依赖不变时复用，两者配合才能阻断渲染链。
- 注意依赖数组里的响应式值变化时缓存仍会更新，不要为了稳定引用而漏写依赖。

```jsx
const Child = memo(function Child({ onSelect, label }) {
  console.log('render Child', label);
  return <button onClick={onSelect}>{label}</button>;
});

function Parent() {
  const [count, setCount] = useState(0);

  // 不加 useCallback 时 Parent 每次渲染都会创建新函数，Child 跟着重渲染
  const handleSelect = useCallback(() => {
    console.log('selected');
  }, []);

  return (
    <>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      <Child label="选择" onSelect={handleSelect} />
    </>
  );
}
```
