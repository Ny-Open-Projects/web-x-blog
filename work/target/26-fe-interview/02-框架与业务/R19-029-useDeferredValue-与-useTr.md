---
title: [R19-029] useDeferredValue 与 useTransition 的区别？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-029：useDeferredValue 与 useTransition 的区别？
**答**：
- useDeferredValue 接收一个值，返回"延迟版本"，在新值渲染完成前继续显示旧值的渲染结果。
- useTransition 控制的是"更新过程"，useDeferredValue 控制的是"值本身"，无需把 setState 包起来。
- 数据来自 props 或上层时用 useDeferredValue 更自然；自己触发更新时用 useTransition 更直接。
- 两者本质都是给更新降优先级，依赖并发渲染的打断与恢复能力。

```jsx
function SearchResults({ query }) {
  // 输入的 query 立即渲染，列表用延迟值，等价于带调度的防抖
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;

  const results = useMemo(() => searchAll(deferredQuery), [deferredQuery]);

  return (
    <ul style={{ opacity: isStale ? 0.6 : 1 }}>
      {results.map((r) => (
        <li key={r.id}>{r.title}</li>
      ))}
    </ul>
  );
}
```
