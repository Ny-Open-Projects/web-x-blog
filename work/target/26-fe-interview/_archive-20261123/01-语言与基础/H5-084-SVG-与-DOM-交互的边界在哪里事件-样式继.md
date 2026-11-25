---
title: [H5-084] SVG 与 DOM 交互的边界在哪里？事件、样式继承有哪些坑？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-084：SVG 与 DOM 交互的边界在哪里？事件、样式继承有哪些坑？
**答**：
- 内联 SVG 是真 DOM：可 `addEventListener`、可被 CSS 选择、支持 `querySelector`；**外部 `<img src="x.svg">` 不是**——图内元素完全不可交互、不可改样式。
- 样式继承：SVG 展示属性（fill/stroke 等）是"表现属性"，CSS 优先级高于它们；但继承规则不同——fill/stroke 可继承，width/height/x/y 不继承。
- 事件目标：path/rect/circle 各自是事件目标，可做精确命中；想整图标统一处理就绑在 `<svg>` 或外层容器上。
- CSS 能进入 SVG 的前提是"内联或 `&lt;object&gt;` 同文档"；`<img>` 里的 SVG 只能用自己的内部 `<style>`。
- 动画注意：SMIL（`&lt;animate&gt;`）在 Chrome 曾宣布废弃又收回，工程上优先 CSS animation / Web Animations API 驱动 SVG 属性。

```html
<!-- 内联 SVG：完整交互能力 -->
<svg id="chart" viewBox="0 0 200 120" width="200">
  <style>                       <!-- 内部 style 只作用于本文档的内联 svg -->
    #chart rect { transition: fill .2s; }
    #chart rect:hover { fill: #f60; }          <!-- SVG 也支持 hover -->
  </style>
  <rect class="bar" data-month="7月" x="10"  y="60" width="30" height="60" fill="#36f"/>
  <rect class="bar" data-month="8月" x="60"  y="30" width="30" height="90" fill="#36f"/>
  <rect class="bar" data-month="9月" x="110" y="45" width="30" height="75" fill="#36f"/>
</svg>

<!-- 外部引用：只是一张图，内部元素摸不到 -->
<img src="/chart.svg" alt="九月份销售额图表">

<script>
  // 事件与 data-* 全部可用
  document.getElementById('chart').addEventListener('click', (e) => {
    const bar = e.target.closest('rect.bar');
    if (bar) console.log('点击了柱子：', bar.dataset.month);
  });

  // 表现属性 vs CSS：CSS 优先级更高，可覆盖 fill attribute
  const bar = document.querySelector('.bar');
  bar.setAttribute('fill', '#36f');            // attribute 形式
  bar.style.fill = '#0a0';                     // 内联 CSS 胜出
</script>
```

## 十六、二进制与文件进阶
