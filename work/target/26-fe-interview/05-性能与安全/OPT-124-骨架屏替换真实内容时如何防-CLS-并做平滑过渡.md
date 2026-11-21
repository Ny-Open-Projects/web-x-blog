---
title: [OPT-124] 骨架屏替换真实内容时如何防 CLS 并做平滑过渡？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-124：骨架屏替换真实内容时如何防 CLS 并做平滑过渡？

**答**：
- CLS 根因：骨架块高度与真实内容不一致，替换瞬间布局跳动。方案是"尺寸契约"：骨架块用与真实内容相同的 aspect-ratio / 固定高度。
- 头图/卡片类给容器写死宽高比，文字区给 min-height 上限兜底（超长截断或折叠）。
- 过渡用 opacity/translate 短动画（150~250ms），只动 composite 属性，不引发重排。
- 内容到达后先填充 DOM 再切可见性，避免"先卸骨架再等渲染"的闪白。

```html
<!-- 一一对应：骨架屏与真实内容共用尺寸契约 + 无缝过渡 -->
<style>
  .card { contain: layout paint; }
  /* 尺寸契约：骨架与内容同一 aspect-ratio，替换零位移 */
  .card-media { aspect-ratio: 16 / 9; width: 100%; background: #eee; }
  .card-title { min-height: 24px; max-height: 48px; overflow: hidden; } /* 1~2 行兜底 */
  .skeleton { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 50% { opacity: .55; } }
  /* 内容过渡：只做 opacity，不动布局属性 */
  .card-content { opacity: 0; transition: opacity .2s ease; }
  .card-content.ready { opacity: 1; }
  .card.ready .skeleton { display: none; }
</style>
<div class="card" id="card">
  <div class="card-media skeleton"></div>
  <div class="card-title skeleton"></div>
  <div class="card-content" hidden>
    <div class="card-media"><img src="hero.webp" width="640" height="360" alt=""></div>
    <div class="card-title">真实标题文本</div>
  </div>
</div>
<script>
  // 先填充、标记 ready 切透明度，最后卸骨架：三步避免闪白与跳动
  fetch('/api/card/1').then(r => r.json()).then(data => {
    const card = document.getElementById('card');
    const content = card.querySelector('.card-content');
    content.hidden = false;
    requestAnimationFrame(() => requestAnimationFrame(() => {
      card.classList.add('ready'); content.classList.add('ready');
    }));
  });
</script>
```
