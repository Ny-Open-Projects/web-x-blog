---
title: [MFW-724] Router 预取的并发限制
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-724：Router 预取并发限制

**答**:
- Router 预取的并发管理：1) **默认行为**（视口内 Link 自动 prefetch——长列表 500 Link = 500 并发请求——带宽爆炸 RBL-543）；2) **并发限制的层次**：框架内建（Next 的内部队列——同时 N 个 prefetch）vs 应用层（IntersectionObserver 的 rootMargin 控制——触发范围缩减）；3) **优先级排序**（视口中心优先 > 边缘（IntersectionObserver 的 rootMargin 收缩——中心 300px 内优先 prefetch）。
- 预取的取消：导航离开视口 → 取消未完成的 prefetch（AbortController——不再浪费带宽 RBL-769 的取消传播）；「prefetch 的生命周期」：进入视口 → prefetch → 导航复用 or 离开视口 → cancel。
- 与 Route Cache 的交互：prefetch 结果写入 Router Cache（RBL-511）——缓存的容量约束（LRU 淘汰——大量 prefetch 后旧缓存被淘汰——预取的缓存收益取决于访问模式）。
- 追问钩子：为什么「长列表的 prefetch 风暴」比「逐条 prefetch」更难治理？——长列表 = 视口内 50 个 Link（IntersectionObserver 全触发）；每个 prefetch = RSC payload 请求（50 × 20KB = 1MB）+ 带宽竞争（与用户交互请求抢带宽 RBL-895）；解法的层次：IntersectionObserver rootMargin 收缩（触发范围缩小）→ 并发限制（框架级——同时 3 个）→ 优先级（视口中心优先）→ hover 预取（鼠标意图——最精确的信号）；多层防线的组合。

```tsx
// 长列表的预取治理
function usePrefetchControl({ maxConcurrent = 3, rootMargin = '200px' } = {}) {
  const active = useRef(new Set());
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      const href = entry.target.getAttribute('href');
      if (entry.isIntersecting) {
        // 视口内：入队 prefetch
        prefetchQueue.push(href);
      } else {
        // 离开视口：取消 prefetch
        active.current.get(href)?.abort();
        active.current.delete(href);
      }
    }
    pump();
  }, { rootMargin });
  function pump() {
    while (active.current.size < maxConcurrent && prefetchQueue.length) {
      const href = prefetchQueue.shift();
      const controller = new AbortController();
      active.current.set(href, controller);
      router.prefetch(href, { signal: controller.signal })
        .finally(() => { active.current.delete(href); pump(); });
    }
  }
  return { observer, disconnect: () => observer.disconnect() };
}
// hover 预取（意图信号——最精确）
<Link href={href} prefetch={false}                    // 关闭自动预取
  onMouseEnter={() => router.prefetch(href)}>         // hover 才预取
```
