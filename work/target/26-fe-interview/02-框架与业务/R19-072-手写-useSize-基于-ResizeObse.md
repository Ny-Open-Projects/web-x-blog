---
title: [R19-072] 手写 useSize，基于 ResizeObserver 监听元素尺寸？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-072：手写 useSize，基于 ResizeObserver 监听元素尺寸？
**答**：
- window.resize 拿不到具体元素尺寸，ResizeObserver 才能精确观察某个容器。
- observer 实例用 ref 缓存复用，每次 effect 只 observe/unobserve 当前元素。
- contentRect 提供 content-box 尺寸；需要 border-box 时用 entry.borderBoxSize。
- 典型场景：图表随容器自适应、虚拟列表测量容器高度。

```jsx
// useSize：ResizeObserver 监听元素尺寸变化
import { useEffect, useRef, useState } from 'react';

export function useSize(target) {
  const [size, setSize] = useState({ width: 0, height: 0 });
  const observerRef = useRef(null);

  useEffect(() => {
    const el = target?.current;
    if (!el) return;
    observerRef.current ??= new ResizeObserver(entries => {
      const { width, height } = entries[0].contentRect;
      setSize({ width, height });
    });
    observerRef.current.observe(el);
    return () => observerRef.current?.unobserve(el);
  }, [target]);

  return size;
}

// 用法：容器自适应布局
function Chart() {
  const ref = useRef(null);
  const { width, height } = useSize(ref);
  return <div ref={ref}><Canvas width={width} height={height} /></div>;
}
```
