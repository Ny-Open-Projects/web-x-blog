---
title: [CSS-018] 为什么给父元素加 transform 后子元素的 fixed 定位会失效？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-018：为什么给父元素加 transform 后子元素的 fixed 定位会失效？

**答**：
- transform/perspective/filter 等属性会让该元素成为后代 fixed/absolute 元素的包含块。
- 于是 fixed 不再相对视口，而是相对这个带 transform 的祖先。
- 这也是弹窗组件挪到 body 下渲染（portal）的原因之一：避免祖先的 transform 污染。
- 反向利用：全屏遮罩只想覆盖某个卡片时，可以故意在卡片上加 transform。

```css
/* 失效场景 */
.modal-host {
  transform: scale(1); /* 即使值不变也生效 */
}
.modal-host .modal-mask {
  position: fixed;
  inset: 0;            /* 期望盖住视口，实际只盖住 modal-host */
  background: rgba(0,0,0,.5);
}

/* 主动利用：遮罩只覆盖卡片 */
.card { transform: translateZ(0); }
.card .card-mask { position: fixed; inset: 0; }
```

## 四、Flex 布局
