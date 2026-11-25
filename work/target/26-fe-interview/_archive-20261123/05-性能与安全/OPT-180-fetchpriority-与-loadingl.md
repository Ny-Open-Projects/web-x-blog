---
title: [OPT-180] `fetchpriority` 与 `loading=lazy/eager` 的组合矩阵怎么定？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-180：`fetchpriority` 与 `loading=lazy/eager` 的组合矩阵怎么定？

**答**：
- 两个属性管不同的事：`loading` 管**是否现在加载**（lazy 推迟、eager 立即），`fetchpriority` 管**多路争抢时的优先级**（high/low/auto）。组合使用才是完整策略。
- 矩阵：LCP 首图 `eager + fetchpriority=high` + preload；首屏非 LCP 图 `eager + low`；首屏外图片 `lazy + auto`；轮播预加载下一张 `lazy + low`。
- 默认值陷阱：`<img>` 默认 priority 是 auto（High），一屏内多张大图会互抢；`loading=lazy` 且在首屏边缘的图会被意外推迟导致 LCP 受损——首屏边界用 eager 明确表达。
- 验证：Chrome DevTools Network 面板开 Priority 列，对照 LCP 元素是否拿到 Highest。

```html
<!-- 一一对应：图片加载策略组合矩阵 -->
<!-- 1. LCP 首图：立即 + 最高优先级 + preload 三保险 -->
<link rel="preload" as="image" href="/hero.webp" fetchpriority="high">
<img src="/hero.webp" width="1280" height="720" alt=""
     fetchpriority="high" decoding="async">  <!-- 首屏默认即 eager，无需显式写 -->

<!-- 2. 首屏内次要图片：立即加载但让路（logo/角标/次banner） -->
<img src="/logo.webp" width="120" height="40" alt="" fetchpriority="low">

<!-- 3. 首屏外图片：lazy + auto（默认优先级即可，反正不加载） -->
<img src="/article-1.webp" width="640" height="360" alt="" loading="lazy"
     decoding="async">

<!-- 4. 轮播组件：当前帧 eager+low，下一帧 lazy+low 预热，其余不加载 -->
<div class="carousel">
  <img src="/slide-1.webp" width="1200" height="500" fetchpriority="low" alt="">
  <img src="/slide-2.webp" width="1200" height="500" loading="lazy" fetchpriority="low" alt="">
</div>

<!-- 5. 反模式提醒 -->
<!-- X: <img loading="lazy" fetchpriority="high"> —— lazy 与 high 矛盾，浏览器以 lazy 为准 -->
<!-- X: 首屏 LCP 图 loading="lazy" —— 若 LCP 图恰好在视口边缘会被推迟，LCP 反而劣化 -->
<script>
  // 动态插入首屏外图片时同步设置，保持矩阵一致
  function appendImg(parent, src, opts = {}) {
    const img = new Image(opts.w, opts.h);
    img.src = src;
    img.loading = opts.inViewport ? 'eager' : 'lazy';
    img.fetchPriority = opts.priority || 'auto';
    img.alt = opts.alt || '';
    parent.appendChild(img);
  }
</script>
```
