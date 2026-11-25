---
title: [V3-539] 笔试：手写 useMouseInElement 与 useElementSize
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## V3-539：笔试：手写 useMouseInElement

**答**：实现两个几何类 composable：① `useMouseInElement(targetRef)`：鼠标相对元素坐标（x/y 与元素左上角偏移）+ elementX/Y + elementPositionX/Y（页面坐标）+ isOutside；② mousemove 合帧（rAF 内更新 ref）；③ `useElementSize(targetRef)`：ResizeObserver 跟踪宽高（borderBox 选项）；④ 两者卸载清理；⑤ 元素动态替换（targetRef 变化重绑）。写出实现。

```javascript
export function useMouseInElement(targetRef) {
  const elementX = ref(0), elementY = ref(0);
  const isOutside = ref(true);
  let raf = 0;
  const onMove = (e) => {
    if (raf) return;
    raf = requestAnimationFrame(() => {
      raf = 0;
      const el = targetRef.value;
      if (!el) return;
      const rect = el.getBoundingClientRect();      // rAF 内统一读
      elementX.value = e.clientX - rect.left;
      elementY.value = e.clientY - rect.top;
      isOutside.value = elementX.value < 0 || elementY.value < 0
        || elementX.value > rect.width || elementY.value > rect.height;
    });
  };
  useEventListener(window, 'mousemove', onMove, { passive: true });
  onScopeDispose(() => cancelAnimationFrame(raf));
  return { elementX, elementY, isOutside };
}

export function useElementSize(targetRef, { box = 'border' } = {}) {
  const width = ref(0), height = ref(0);
  let ro = null;
  watch(targetRef, (el) => {
    ro?.disconnect();
    if (!el) return;
    ro = new ResizeObserver(([entry]) => {
      const r = box === 'content' ? entry.contentRect : entry.borderBoxSize?.[0];
      width.value = r ? (r.inlineSize ?? r.width) : el.offsetWidth;
      height.value = r ? (r.blockSize ?? r.height) : el.offsetHeight;
    });
    ro.observe(el);
  }, { immediate: true, flush: 'post' });
  onScopeDispose(() => ro?.disconnect());
  return { width, height };
}
```

**评分点**：
- rAF 合帧内统一「读 rect」（防布局抖动）
- isOutside 判定与坐标语义（相对元素 vs 页面）
- ResizeObserver 的 box 选项与 target 动态重绑
- 双 composable 的清理完整性
