---
title: [H5-147] Web Animations API 的 element.animate 全参数与适用场景？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-147：Web Animations API 的 element.animate 全参数与适用场景？
**答**：
- `animate(keyframes, options)`：keyframes 支持多属性与 `offset` 偏移；options 有 duration/delay/easing/fill/iterations/direction/composite/composite 偏移等。
- 返回 `Animation` 对象，是相对 CSS 的核心增量：`pause/play/reverse/finish/cancel`、`playbackRate`、精确的 `finished/onfinish` 回调、`commitStyles()` 把最终值固化到内联样式。
- `fill: 'forwards'` 长期占住样式会堆积（动画对象不释放），结束后 commitStyles + cancel 是标准收尾。
- 只有 transform/opacity/filter 走合成器线程；width/top 仍触发重排。适用场景：动态生成、精确回调、组合编排、可中断的交互动画。

```javascript
const el = document.querySelector('.card');

const anim = el.animate(
  [
    { transform: 'translateY(20px) scale(.95)', opacity: 0 },
    { transform: 'translateY(0) scale(1)', opacity: 1 },
  ],
  {
    duration: 300,
    delay: 100,
    easing: 'cubic-bezier(.22,1,.36,1)',
    fill: 'backwards',        // delay 期间应用第一帧样式，防闪烁
    iterations: 1,
    direction: 'normal',
    composite: 'replace',     // 'add'/'accumulate' 可与已有 transform 叠加
  }
);

// Animation 对象：可编程控制，这是相对 CSS transition 的核心增量
anim.pause();
anim.playbackRate = 1.5;
anim.onfinish = () => console.log('结束于', anim.currentTime);   // 精确回调
anim.reverse();               // 倒放，做"取消"动效
// anim.cancel();            // 立即移除效果

// fill: forwards 会长期占住样式，动画对象不释放 —— 结束后固化并取消
function animateAndCommit(el, keyframes, opts) {
  const a = el.animate(keyframes, { ...opts, fill: 'forwards' });
  return a.finished.then(() => {
    a.commitStyles();          // 把最终值写入内联 style
    a.cancel();                // 释放动画对象
  });
}

// keyframes 支持 offset 精确控制中间态
el.animate(
  [
    { transform: 'scale(1)', offset: 0 },
    { transform: 'scale(1.15)', offset: 0.6 },    // 前 60% 放大
    { transform: 'scale(1)', offset: 1 },
  ],
  { duration: 400 }
);
// 注意：只有 transform/opacity/filter 走合成器；width/top 仍会触发重排
```
