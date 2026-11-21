---
title: [R19-031] 设计一个 useDebounce 自定义 Hook，原则是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-031：设计一个 useDebounce 自定义 Hook，原则是什么？
**答**：
- 自定义 Hook 就是使用内置 Hook 的普通函数，命名必须以 use 开头，让 lint 规则识别。
- 原则一：只在顶层调用 Hook；原则二：返回值尽量是数组或对象并配类型；原则三：不包含业务语义，保持可复用。
- useDebounce 内部用 setTimeout + effect 清理实现，值变化时清掉旧定时器。
- 返回"延迟后的值"，消费方在它变化时再触发昂贵操作。

```jsx
import { useEffect, useState } from 'react';

function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    // 值再次变化或卸载时清掉上一次的定时器
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debounced;
}

function Search() {
  const [keyword, setKeyword] = useState('');
  const debouncedKeyword = useDebounce(keyword, 500);

  useEffect(() => {
    if (debouncedKeyword) fetchSearch(debouncedKeyword);
  }, [debouncedKeyword]);

  return <input value={keyword} onChange={(e) => setKeyword(e.target.value)} />;
}
```
