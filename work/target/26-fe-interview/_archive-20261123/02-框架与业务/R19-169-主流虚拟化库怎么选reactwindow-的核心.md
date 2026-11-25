---
title: [R19-169] 主流虚拟化库怎么选？react-window 的核心思想与精简实现？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-169：主流虚拟化库怎么选？react-window 的核心思想与精简实现？
**答**：
- 选型：**react-window**（小而稳、定高最优）、**virtua/react-virtuoso**（动态高度、分组、反向列表强）、**@tanstack/react-virtual**（headless、横向/网格/表格通用）。三者内核同源：只渲染可视区 ± overscan 的窗口。
- react-window 思想三步：外层容器测量高度 -> 用 `itemSize` 算出startIndex/endIndex（scrollTop / itemSize）-> 内层用 padding/translate 撑起总高度，绝对定位渲染窗口项。
- 动态高度方案：先估高渲染，用 ResizeObserver 回填真实高度并修正累计偏移（这就是 virtuoso 的做法）。
- 手写精简版用于理解原理：状态只有 scrollTop，重渲染范围用二分或除法定位。

```tsx
// use-virtual-window.tsx —— react-window 核心思想精简实现
import { useState, useRef, useEffect, type ReactNode } from 'react';

export function FixedSizeList({
  itemCount, itemSize, height, overscan = 5, renderItem,
}: {
  itemCount: number;
  itemSize: number;                       // 定高：定位可以纯除法
  height: number;
  overscan?: number;
  renderItem: (index: number) => ReactNode;
}) {
  const [scrollTop, setScrollTop] = useState(0);
  const outerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = outerRef.current;
    if (!el) return;
    // rAF 节流：滚动事件高频，一帧只更新一次
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        setScrollTop(el.scrollTop);
        ticking = false;
      });
    };
    el.addEventListener('scroll', onScroll, { passive: true });
    return () => el.removeEventListener('scroll', onScroll);
  }, []);

  // 核心：可视区索引窗口
  const startIndex = Math.max(0, Math.floor(scrollTop / itemSize) - overscan);
  const visibleCount = Math.ceil(height / itemSize) + overscan * 2;
  const endIndex = Math.min(itemCount - 1, startIndex + visibleCount);

  const items: ReactNode[] = [];
  for (let i = startIndex; i <= endIndex; i++) {
    items.push(
      <div key={i} style={{ position: 'absolute', top: i * itemSize, left: 0, right: 0, height: itemSize }}>
        {renderItem(i)}
      </div>,
    );
  }

  return (
    <div
      ref={outerRef}
      style={{ height, overflow: 'auto', position: 'relative' }} // 外层：滚动容器
    >
      {/* 内层：撑起总高度，滚动条长度与全量列表一致 */}
      <div style={{ height: itemCount * itemSize, position: 'relative' }}>
        {items} {/* 只渲染窗口内 ± overscan 的项 */}
      </div>
    </div>
  );
}

// 库选型速查：
// react-window        -> 定高列表、性能稳定、API 简单（优先默认选它）
// @tanstack/react-virtual -> headless、支持横向/网格/表格、样式自由
// react-virtuoso      -> 动态高度、分组吸顶、聊天反向滚动等复杂场景
```
