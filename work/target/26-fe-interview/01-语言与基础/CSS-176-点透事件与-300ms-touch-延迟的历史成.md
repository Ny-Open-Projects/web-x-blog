---
title: [CSS-176] 点透事件与 300ms touch 延迟的历史成因和现代方案？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-176：点透事件与 300ms touch 延迟的历史成因和现代方案？

**答**：
- 历史成因：浏览器用 300ms 等待判断是否双击缩放，touchend 后 300ms 才合成 click。
- 点透：上层元素 touchend 后被 JS 移除/隐藏，300ms 后合成的 click 落到下层新元素上，误触发下层点击。
- 现代方案：声明 `meta viewport width=device-width` 或 `touch-action: manipulation` 后延迟被移除，交互统一用 click 即可（无需 fastclick 类 polyfill）。
- 遗留代码里若仍有 touchend 模拟点击：遮罩关闭延迟 300ms 再移除 DOM，或在 touchend 里 `preventDefault()` 阻止合成 click。

```css
/* 一行消除 300ms 延迟：允许单指平移缩放，但排除双击缩放判定 */
.page {
  touch-action: manipulation;
}
.carousel {
  /* 滑动场景精确声明：仅水平滑动交给浏览器 */
  touch-action: pan-y;
}
```

```javascript
// 遗留代码兜底：touchend 模拟点击时阻断合成 click，避免点透
overlay.addEventListener('touchend', e => {
  e.preventDefault();          // 阻止 300ms 后的合成 click
  closeOverlay();              // 自己执行关闭逻辑
});
// 或者：关闭动作延迟到 click 事件后再移除 DOM
mask.addEventListener('click', () => {
  mask.style.visibility = 'hidden';
  setTimeout(() => mask.remove(), 350);  // 越过合成 click 窗口
});
```
