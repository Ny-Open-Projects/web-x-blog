---
title: [R19-444] 笔试：手写 useInView 与 useReducedMotion（动画辅助 hooks）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## R19-444：笔试：手写 useInView

**答**：实现：① `useInView(ref, { once, threshold, rootMargin })`：进入视口为 true（once: 只触发一次后停止观察）；② `useReducedMotion()`：prefers-reduced-motion 响应式；③ `useReveal(ref)`：组合——可见时才触发入场动画（返回 shouldAnimate），减动效用户直接显示；④ 触发后的回看不重播（once 语义）；⑤ 动画结束回调（animationend 后置 done）。写出实现。

```javascript
export function useInView(ref, { once = true, threshold = 0.3, rootMargin = '0px' } = {}) {
  const [inView, setInView] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const io = new IntersectionObserver(([e]) => {
      if (e.isIntersecting) {
        setInView(true);
        if (once) io.disconnect();                  // once: 触发即停
      } else if (!once) setInView(false);
    }, { threshold, rootMargin });
    io.observe(el);
    return () => io.disconnect();
  }, [once, threshold, rootMargin]);
  return inView;
}

export function useReducedMotion() {
  const [reduced, setReduced] = useState(() =>
    typeof window !== 'undefined' && matchMedia('(prefers-reduced-motion: reduce)').matches);
  useEffect(() => {
    const mq = matchMedia('(prefers-reduced-motion: reduce)');
    const fn = (e) => setReduced(e.matches);
    mq.addEventListener('change', fn);
    return () => mq.removeEventListener('change', fn);
  }, []);
  return reduced;
}

export function useReveal(ref) {
  const inView = useInView(ref);
  const reduced = useReducedMotion();
  const [done, setDone] = useState(false);
  const shouldAnimate = inView && !reduced && !done;
  return {
    shouldAnimate,
    animationProps: {
      className: shouldAnimate ? 'reveal-in' : (inView || reduced ? 'reveal-done' : 'reveal-hidden'),
      onAnimationEnd: () => setDone(true),
      'aria-hidden': !inView,
    },
  };
}
```

**评分点**：
- once 语义（disconnect 防回看重播）
- useReducedMotion 的响应式（系统设置变化）
- 组合 hook 的降级链（减动效直接显示）
- animationend 收尾状态（动画完成置 done）

## 变体与延伸（补充）

**变体与延伸**：

1. once 为 false 时反复触发 setState 有什么代价？ → 视口边缘抖动会造成高频 setState 与重渲染；通常加阈值滞回（进 0.3、出 0.1），或用 ref 记住上次状态、只在翻转时更新。
2. rootMargin 设成 '200px' 会带来什么副作用？ → 提前触发动画，用户可能看不到入场过程；而且滚动容器不是视口时 rootMargin 相对的是 root，必须显式传 root 元素。
3. 减动效用户为什么不能干脆不渲染？ → 要求是"无动画但内容可见"，只跳过过渡而不是跳过元素；shouldAnimate 置 false 后仍要渲染最终样式，否则等于把内容藏了。
