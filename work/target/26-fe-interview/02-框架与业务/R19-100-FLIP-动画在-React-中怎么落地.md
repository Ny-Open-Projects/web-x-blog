---
title: [R19-100] FLIP 动画在 React 中怎么落地？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-100：FLIP 动画在 React 中怎么落地？
**答**：
- FLIP 四步：First 记录旧位置、Last 让 DOM 更新到新位置、Invert 用 transform 反向偏移、Play 过渡回 0。
- React 的切入点是 useLayoutEffect：它在 DOM 更新后、浏览器绘制前同步执行，适合同时完成测量与反演。
- 位置存 ref（不触发渲染），transition 先置 none 防止首次偏移被动画，rAF 下一帧再开启过渡。
- 适用场景：列表重排、卡片换位、拖拽结束的归位动画；比直接操作 class 动画更可控。

```jsx
// ReorderableList.tsx —— 列表重排的 FLIP 动画
import { useLayoutEffect, useRef } from 'react';

function ReorderableList({ items }) {
  const positionsRef = useRef(new Map());
  const listRef = useRef(null);

  useLayoutEffect(() => {
    const children = listRef.current?.children ?? [];
    for (const el of children) {
      const prev = positionsRef.current.get(el.dataset.id);
      const next = el.getBoundingClientRect().top;
      if (prev !== undefined && prev !== next) {
        const delta = prev - next;
        // Invert：反向偏移到旧位置，且禁止过渡
        el.style.transition = 'none';
        el.style.transform = `translateY(${delta}px)`;
        // Play：下一帧过渡回 0
        requestAnimationFrame(() => {
          el.style.transition = 'transform 300ms';
          el.style.transform = '';
        });
      }
      positionsRef.current.set(el.dataset.id, next);   // 记录本轮新位置
    }
  }, [items]);   // 列表顺序变化后、浏览器绘制前执行

  return (
    <ul ref={listRef}>
      {items.map(item => (
        <li key={item.id} data-id={item.id}>{item.label}</li>
      ))}
    </ul>
  );
}
```
