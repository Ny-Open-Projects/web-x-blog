---
title: [R19-442] 笔试：手写 useCarousel（React 轮播 hook）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## R19-442：笔试：手写 useCarousel

**答**：实现 `useCarousel(count, { autoplay, interval })`：① current 状态 + goTo/prev/next（循环取模）；② 自动播放（暂停条件：hover/hidden/手动操作后延迟恢复）；③ 无缝循环（translateX 连续：clone 首尾或按 index 模运算渲染）；④ 指示器高亮同步；⑤ 无障碍：aria-roledescription + 键盘方向键。写出实现。

```javascript
export function useCarousel(count, { autoplay = true, interval = 3000 } = {}) {
  const [current, setCurrent] = useState(0);
  const [paused, setPaused] = useState(false);
  const timerRef = useRef(null);
  const lastInteract = useRef(0);

  const goTo = useCallback((i) => {
    setCurrent(((i % count) + count) % count);      // 循环取模
    lastInteract.current = Date.now();              // 手动操作后延迟恢复自动播
  }, [count]);
  const next = useCallback(() => goTo(current + 1), [current, goTo]);
  const prev = useCallback(() => goTo(current - 1), [current, goTo]);

  useEffect(() => {
    if (!autoplay || paused) return;
    const t = setInterval(() => {
      if (Date.now() - lastInteract.current < 5000) return;   // 交互后 5s 内不自动
      setCurrent((c) => (c + 1) % count);
    }, interval);
    return () => clearInterval(t);
  }, [autoplay, paused, interval, count]);

  // 页面隐藏暂停
  useEffect(() => {
    const onVis = () => setPaused(document.hidden);
    document.addEventListener('visibilitychange', onVis);
    return () => document.removeEventListener('visibilitychange', onVis);
  }, []);

  // 键盘
  const onKeyDown = useCallback((e) => {
    if (e.key === 'ArrowRight') next();
    if (e.key === 'ArrowLeft') prev();
  }, [next, prev]);

  return { current, goTo, next, prev, paused, setPaused, onKeyDown,
    containerProps: {
      role: 'region', 'aria-roledescription': '轮播图',
      onMouseEnter: () => setPaused(true), onMouseLeave: () => setPaused(false),
      onKeyDown,
      tabIndex: 0,
    } };
}
```

**评分点**：
- 循环取模（负数处理）与自动播放三重暂停（hover/hidden/交互后延迟）
- goTo 的统一入口（键盘/指示器/按钮共用）
- aria-roledescription 与键盘导航
- 交互后延迟恢复的体验设计
