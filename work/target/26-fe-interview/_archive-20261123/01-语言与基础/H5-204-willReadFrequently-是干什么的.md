---
title: [H5-204] Canvas 的 willReadFrequently 是干什么的
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-204：Canvas 的 willReadFrequently 是干什么的

**答**：
- `getContext('2d', { willReadFrequently: true })` 告诉浏览器「我会频繁 getImageData」，浏览器改用 CPU 后备存储而非 GPU 纹理
- 不开的话：每次 getImageData 都要从 GPU 显存回读（readback），跨总线拷贝非常慢
- 判断标准：读取/像素处理类场景（取色器、滤镜、像素游戏）开；纯绘制类不要开（CPU 绘制反而慢）
- 这是「提示不是命令」，浏览器可以忽略；性能差异可达数十倍
- 同类提示还有 `desynchronized: true`（低延迟绘制，游戏用）

```javascript
// 像素处理场景：开启后 getImageData 快一个量级
const ctx = canvas.getContext('2d', { willReadFrequently: true });
function pickColor(x, y) {
  const d = ctx.getImageData(x, y, 1, 1).data;
  return `rgb(${d[0]},${d[1]},${d[2]})`;
}
```
