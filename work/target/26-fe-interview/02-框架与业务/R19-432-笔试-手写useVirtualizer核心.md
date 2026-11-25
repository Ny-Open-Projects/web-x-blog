---
title: [R19-432] 笔试：手写 useVirtualizer 核心（动态高度）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## R19-432：笔试：手写 useVirtualizer

**答**：实现 `useVirtualizer({ count, getScrollElement, estimateSize, overscan })`：① 虚拟项计算：getVirtualItems() 返回 { index, start, size, key }；② 动态高度：measureElement（ResizeObserver 回填实际高度），measurementsCache 更新后重算；③ 二分查找定位 startIndex（累计高度数组）；④ 滚动方向预判（向上滚动时多渲染上方）；⑤ getTotalSize 随测量更新。写出实现。

```javascript
export function useVirtualizer({ count, getScrollElement, estimateSize, overscan = 5 }) {
  const sizes = useRef(new Map());          // index -> measured size
  const scrollOffset = useRef(0);

  // 累计高度数组(惰性构建)
  const getMeasurements = () => {
    const arr = [];
    let acc = 0;
    for (let i = 0; i < count; i++) {
      arr.push({ start: acc, size: sizes.current.get(i) ?? estimateSize(i) });
      acc += arr[i].size;
    }
    return arr;
  };
  const binarySearch = (arr, offset) => {
    let lo = 0, hi = arr.length - 1;
    while (lo < hi) { const mid = (lo + hi) >> 1;
      arr[mid].start + arr[mid].size <= offset ? lo = mid + 1 : hi = mid; }
    return lo;
  };
  const getVirtualItems = () => {
    const m = getMeasurements();
    const el = getScrollElement();
    const viewH = el?.clientHeight ?? 600;
    const start = Math.max(0, binarySearch(m, scrollOffset.current) - overscan);
    const end = Math.min(count, binarySearch(m, scrollOffset.current + viewH) + overscan);
    return Array.from({ length: end - start }, (_, i) => ({
      index: start + i, start: m[start + i].start, size: m[start + i].size, key: start + i,
    }));
  };
  const measureElement = (el) => {
    const idx = Number(el.dataset.index);
    const measured = el.getBoundingClientRect().height;
    if (measured && Math.abs((sizes.current.get(idx) ?? estimateSize(idx)) - measured) > 1) {
      sizes.current.set(idx, measured);            // 回填实测 → 重算
      forceUpdate();
    }
  };
  const getTotalSize = () => { const m = getMeasurements(); return m.at(-1).start + m.at(-1).size; };
  return { getVirtualItems, measureElement, getTotalSize };
}
```

**评分点**：
- 累计高度数组 + 二分定位（不定高核心）
- measureElement 回填实测 + 阈值防抖（>1px 才更新）
- overscan 缓冲与方向预判
- getTotalSize 随测量动态更新（滚动条长度）
