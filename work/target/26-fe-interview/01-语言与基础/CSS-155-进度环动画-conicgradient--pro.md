---
title: [CSS-155] 进度环动画（conic-gradient + @property）怎么实现？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-155：进度环动画（conic-gradient + @property）怎么实现？

**答**：
- 环 = conic-gradient 双色扇形 + 同心圆内盖（伪元素画白圆挖洞）。
- `--p` 注册为 `<percentage>` 后可过渡，JS 只需改一个变量，角度、文字全部联动。
- 内径大小由内盖尺寸控制；描边风格可改用双层 conic + mask 更灵活。
- 兼容：不支持 @property 的内核直接呈现最终角度（跳变但不报错），属安全降级。

```css
@property --p {
  syntax: "<percentage>";
  initial-value: 0%;
  inherits: false;
}
.ring {
  position: relative;
  width: 96px;
  height: 96px;
  border-radius: 50%;
  background: conic-gradient(#096 var(--p), #e8e8e8 0);
  display: grid;
  place-items: center;
  transition: --p 1s ease-out;
}
/* 同心白圆挖出环 */
.ring::before {
  content: "";
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: #fff;
}
.ring .val {
  position: absolute;
  font-size: 20px;
}
/* JS：ring.style.setProperty('--p', '80%') 平滑滚到 80% */
.ring.is-80 { --p: 80%; }
```
