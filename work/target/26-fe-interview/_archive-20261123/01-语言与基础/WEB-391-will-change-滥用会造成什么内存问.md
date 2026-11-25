---
title: [WEB-391] will-change 滥用会造成什么内存问题？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-391：will-change 滥用会造成什么内存问题？
**答**：
- will-change 提前创建合成层并常驻：每层要分配纹理显存（层尺寸的像素数×4字节），大层/多层叠加内存暴涨。
- 正确用法：只给真正要动画的元素、动画前提升动画后移除（或用 transform 触发临时提升）；禁止给几百个列表项都加。
- 替代思路：动画尽量用 transform/opacity（自动提升）、大列表用 content-visibility 跳过屏外渲染。

```javascript
// 1000 个卡片都加 will-change: transform → 1000 个常驻层
const cost = (w, h, layers) => (w * h * 4 * layers / 1024 / 1024).toFixed(1) + ' MB';
console.log(cost(300, 200, 1000)); // ~234 MB 显存
// 正确: 动画开始前加，结束移除
el.addEventListener('transitionend', () => el.style.willChange = 'auto');
console.log('will-change 是"预告"，不是"常驻优化"');
```
