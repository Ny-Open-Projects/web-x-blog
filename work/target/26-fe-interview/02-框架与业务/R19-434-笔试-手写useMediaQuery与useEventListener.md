---
title: [R19-434] 笔试：手写 useMediaQuery 与 useEventListener（React 版）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## R19-434：笔试：手写 useMediaQuery

**答**：实现：① `useEventListener(target, event, handler, options)`：SSR 安全（window 判断）、deps 变化重绑、cleanup；② `useMediaQuery(query)`：SSR 默认 false、matchMedia change 监听；③ `usePreferredDark()`：useMediaQuery 组合；④ `useResponsive()`：返回 { isMobile, isTablet, isDesktop }（断点集合）；⑤ hydration 一致性（SSR 渲染 false，水合后校正的说明）。写出实现。

```javascript
export function useEventListener(target, event, handler, options) {
  const ref = useRef(handler);
  ref.current = handler;                              // 永远最新 handler(不重绑)
  useEffect(() => {
    const el = typeof target === 'function' ? target() : target?.current ?? target;
    if (!el) return;                                  // SSR/未挂载安全
    const fn = (e) => ref.current(e);
    el.addEventListener(event, fn, options);
    return () => el.removeEventListener(event, fn, options);
  }, [target, event]);                                // handler 不进 deps
}

export function useMediaQuery(query) {
  const [matches, setMatches] = useState(false);      // 首帧恒 false 与 SSR 对齐, 真实值由 effect 校正
  useEffect(() => {
    const mq = window.matchMedia(query);
    setMatches(mq.matches);
    const fn = (e) => setMatches(e.matches);
    mq.addEventListener('change', fn);
    return () => mq.removeEventListener('change', fn);
  }, [query]);
  return matches;
}

export const usePreferredDark = () => useMediaQuery('(prefers-color-scheme: dark)');
export function useResponsive() {
  return {
    isMobile: useMediaQuery('(max-width: 767px)'),
    isTablet: useMediaQuery('(min-width: 768px) and (max-width: 1199px)'),
    isDesktop: useMediaQuery('(min-width: 1200px)'),
  };
}
// 注意: SSR 渲染 false → 水合后校正会触发一次额外渲染(可接受)或用 CSS 媒体查询替代 JS
```

**评分点**：
- handler 用 ref 免重绑（监听器稳定性）
- SSR 安全（typeof window 守卫）
- matchMedia change 监听与清理
- hydration 校正的一次额外渲染权衡

## 变体与延伸（补充）

**变体与延伸**：

1. handler 用 ref 免重绑，代价是什么？ → 事件触发时读到最新闭包，但赋值发生在 render 期，StrictMode 双调用下必须保证幂等；也不能在 render 里顺带做订阅等副作用。
2. 为什么 useMediaQuery 在 SSR 必须给 false？ → 服务端没有 matchMedia，若服务端猜 true 会与客户端首帧不一致直接水合失败；统一 false 再加一次水合后校正，是可控的额外渲染。
3. useResponsive 用三个 useMediaQuery 有什么隐患？ → 三次监听加三次 setState，可能连触发多轮渲染；更好的是单个 resize/matchMedia 监听加一次批量计算，或用容器查询把判断下沉到 CSS。
