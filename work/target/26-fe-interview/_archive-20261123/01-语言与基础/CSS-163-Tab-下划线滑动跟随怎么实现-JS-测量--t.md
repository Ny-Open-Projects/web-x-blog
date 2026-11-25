---
title: [CSS-163] Tab 下划线滑动跟随怎么实现（JS 测量 + transform）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-163：Tab 下划线滑动跟随怎么实现（JS 测量 + transform）？

**答**：
- 下划线是独立定位元素，JS 读取当前 tab 的 `offsetLeft/offsetWidth`，用 transform 移动过去。
- 只动 transform（含宽度 scaleX 或直接 width），走合成/绘制，不触发重排。
- 需要响应字体加载、resize、切 tab 三个时机重算；用 rAF 节流。
- 初始渲染未布局完成时先隐藏下划线，首次测量后再显示，避免闪跳。

```html
<div class="tabs">
  <button class="tab is-active">首页</button>
  <button class="tab">发现</button>
  <button class="tab">我的</button>
  <span class="ink"></span>
</div>
<style>
  .tabs { position: relative; display: flex; gap: 24px; }
  .tab {
    padding: 12px 4px;
    border: none;
    background: none;
    font-size: 15px;
    color: #666;
  }
  .tab.is-active { color: #096; font-weight: 600; }
  .ink {
    position: absolute;
    bottom: 0; left: 0;
    height: 3px;
    width: 0;
    border-radius: 2px;
    background: #096;
    opacity: 0;                 /* 首测前隐藏防闪跳 */
    transition: transform .3s, width .3s;
  }
</style>
<script>
  const tabs = document.querySelectorAll('.tab');
  const ink = document.querySelector('.ink');
  function moveInk(target) {
    ink.style.width = target.offsetWidth + 'px';
    ink.style.transform = `translateX(${target.offsetLeft}px)`;
    ink.style.opacity = '1';
  }
  tabs.forEach(tab => tab.addEventListener('click', () => {
    document.querySelector('.tab.is-active')?.classList.remove('is-active');
    tab.classList.add('is-active');
    moveInk(tab);
  }));
  // 三个重算时机：字体就绪、窗口变化、首次进入
  document.fonts.ready.then(() => moveInk(document.querySelector('.tab.is-active')));
  window.addEventListener('resize', () =>
    requestAnimationFrame(() => moveInk(document.querySelector('.tab.is-active'))));
</script>
```
