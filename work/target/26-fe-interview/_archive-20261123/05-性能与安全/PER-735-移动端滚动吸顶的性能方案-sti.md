---
title: [PER-735] 移动端滚动吸顶的性能方案：sticky 与 JS fallback 的选择、吸顶切换抖动治理
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-735：移动端滚动吸顶的性能方案：sticky 与 JS fallback 的选择、吸顶切换抖动治理

**答**：
- 首选 `position: sticky`（零 JS、合成器友好）；iOS 老内核/复杂嵌套滚动容器失效时才用 JS fallback（scroll 监听 + 固定定位切换）。
- 抖动治理：吸顶/脱离临界点反复横跳——加 2px 缓冲带（> top+2 吸顶，< top-2 脱离）；JS 方案里切换 class 用 transform 而不是改 top（避免 layout）；吸顶元素用 will-change 提升仅在其吸顶期间。
- sticky 失效排查清单：父容器 overflow: hidden/auto（sticky 相对滚动容器失效）、祖先有 transform（改变包含块）、height: 100% 链断裂——sticky 不生效九成是这三个。
- 度量：吸顶切换时 rAF gap（fallback 方案是否掉帧）、sticky 与 JS 方案切换的用户感知差异。

```javascript

const stickyPerf = {
  choice: '首选 position: sticky（零 JS）；老内核嵌套滚动失效才 JS fallback',
  stickyFailures: ['父容器 overflow hidden/auto', '祖先 transform 改变包含块', 'height 100% 链断裂'],
  jitter: { buffer: '临界点 2px 缓冲带防横跳', transform: 'JS 切换用 transform 不改 top',
    willChange: '仅吸顶期间提升' },
};
// JS fallback（带缓冲带）
function stickyFallback(header, sentinel) {
  let stuck = false;
  const onScroll = () => {
    const top = sentinel.getBoundingClientRect().top;
    if (!stuck && top < -2) {                                   // 缓冲带 -2
      stuck = true;
      header.style.transform = `translateY(${sentinel.offsetTop - scrollY}px)`;
      header.style.willChange = 'transform';
    } else if (stuck && top > 2) {
      stuck = false;
      header.style.transform = '';
      header.style.willChange = 'auto';
    }
  };
  document.addEventListener('scroll', () => requestAnimationFrame(onScroll), { passive: true });
}
```
