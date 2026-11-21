---
title: [WCN-100] 笔试：手写 Signals 版虚拟滚动（窗口 computed + 总高占位）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-100：笔试：手写 Signals 版虚拟滚动

**题目**：固定行高虚拟列表：① `scrollTop / viewportH / total` 三个 signal；② `window` computed 输出 `{ start, end, offsetY, totalH }`（前后各留 5 条缓冲）；③ 滚动容器 scroll 事件写 scrollTop（rAF 合帧）；④ 渲染层用 `translateY(offsetY)` 偏移窗口内容，总高用占位 spacer；⑤ end 封顶 total；⑥ 返回绑定助手。

**答**：

```javascript
import { createSignal, computed, effect, untrack } from './mini.js';

export function createVirtualList({ itemH = 40, buffer = 5, total }) {
  const [scrollTop, setST] = createSignal(0);
  const [viewportH, setVH] = createSignal(400);
  const [count, setCount] = createSignal(total);

  const view = computed(() => {
    const t = count();
    const totalH = t * itemH;
    const rawStart = Math.floor(untrack(scrollT) / itemH);
    const start = Math.max(0, rawStart - buffer);
    const visible = Math.ceil(untrack(viewH) / itemH) + buffer * 2;
    const end = Math.min(t, rawStart + visible);
    return { start, end, offsetY: start * itemH, totalH };
  });

  // 绑定滚动（合帧）
  function bindScroll(el) {
    let raf = 0;
    const onScroll = () => {
      if (raf) return;
      raf = requestAnimationFrame(() => { raf = 0; setST(el.scrollTop); });
    };
    el.addEventListener('scroll', onScroll, { passive: true });
    const ro = new ResizeObserver(() => setVH(el.clientHeight));
    ro.observe(el);
    return { dispose() { el.removeEventListener('scroll', onScroll); ro.disconnect(); cancelAnimationFrame(raf); } };
  }

  // 渲染：effect(() => { const v = view(); fill(v.start, v.end); spacer.style.height = v.totalH+'px';
  //   inner.style.transform = `translateY(${v.offsetY}px)`; });
  return { view, bindScroll, setCount };
}
// fill(start,end)：只渲染 [start,end) 的行，行内 translateY 定位固定 itemH
```

**评分点**：
- 窗口计算含 buffer，start/有 end 封顶（边界正确性）。
- scroll 事件 passive + rAF 合帧（滚动性能）。
- totalH 占位 + translateY 偏移（布局方案正确：不做 padding 撑高变形）。
- ResizeObserver 更新 viewportH（自适应）。
