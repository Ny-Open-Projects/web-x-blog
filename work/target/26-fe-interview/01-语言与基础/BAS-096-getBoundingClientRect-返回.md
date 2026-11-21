---
title: [BAS-096] getBoundingClientRect 返回的各值是什么含义？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-096：getBoundingClientRect 返回的各值是什么含义？
**答**：
- 返回元素相对**视口**的位置与尺寸：top/left 是上、左边缘到视口的距离，right/bottom 是右、下边缘距离，width/height 含 border。
- 值随滚动实时变化：页面下滚时 top 变小甚至为负；加 window.scrollX/scrollY 才换算成文档坐标。
- 常用于吸顶判断、拖拽、碰撞与曝光检测；注意 width 是经 transform 缩放后的实际渲染尺寸。

```javascript
const rect = document.querySelector('#target').getBoundingClientRect();
const docX = rect.left + window.scrollX;  // 换算成文档坐标
const docY = rect.top + window.scrollY;
const inView = rect.top < window.innerHeight && rect.bottom > 0; // 是否在视口内
console.log(docX, docY, inView);
```
