---
title: [V3-531] 笔试：手写 useVirtualList 核心
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## V3-531：笔试：手写 useVirtualList

**答**：实现 `useVirtualList(list, { itemHeight, overscan = 5 })`（定高版）：① 返回 { list: 可见项(带 style offset), containerProps, wrapperProps, scrollToIndex }；② 滚动计算：startIndex = floor(scrollTop / h) - overscan，end = start + 可见数 + 2*overscan；③ wrapper 撑高（总高）+ transform 偏移；④ scrollToIndex(i)：scrollTop = i * h - 容器可视一半（居中可选）；⑤ scroll 事件 passive + rAF 合帧。写出实现。

```javascript
import { ref, computed, onMounted } from 'vue';

export function useVirtualList(list, { itemHeight: h, overscan = 5 } = {}) {
  const containerRef = ref(null);
  const scrollTop = ref(0);
  const viewH = ref(0);

  const visible = computed(() => {
    const items = list.value;
    const start = Math.max(0, Math.floor(scrollTop.value / h) - overscan);
    const count = Math.ceil(viewH.value / h) + overscan * 2;
    const end = Math.min(items.length, start + count);
    return {
      start, end,
      items: items.slice(start, end).map((item, i) => ({
        data: item, index: start + i,
        style: { transform: `translateY(${(start + i) * h}px)`, height: `${h}px` },
      })),
    };
  });
  const totalHeight = computed(() => list.value.length * h);

  function onScroll(e) {
    if (!raf) raf = requestAnimationFrame(() => {
      scrollTop.value = e.target.scrollTop;
      raf = 0;
    });
  }
  let raf = 0;
  function scrollToIndex(i, center = false) {
    const target = i * h - (center ? viewH.value / 2 - h / 2 : 0);
    containerRef.value.scrollTop = Math.max(0, target);
  }
  onMounted(() => { viewH.value = containerRef.value.clientHeight; });
  return {
    list: computed(() => visible.value.items),
    containerProps: { ref: containerRef, onScroll, style: { overflowY: 'auto' } },
    wrapperProps: { style: { height: `${totalHeight.value}px`, position: 'relative' } },
    scrollToIndex,
  };
}
```

**评分点**：
- overscan 缓冲区与可见区间计算
- transform 定位（绝对定位也接受，但 transform 不触发 layout）
- scrollToIndex 与居中偏移
- scroll passive + rAF 合帧防抖
