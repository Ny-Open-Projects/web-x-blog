---
title: [PER-964] 合成层（Compositing Layer）提升的条件与层爆炸治理
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-964：合成层（Compositing Layer）提升的条件与层爆炸治理

**答**：
- 提升条件：3D transform、will-change: transform/opacity、fixed 定位、video/canvas、硬件加速滤镜、在动画中的元素等；浏览器也可能因层合并策略主动提升。
- 成本：每层占独立显存（宽×高×4 字节），大层+多层导致内存暴涨与上传耗时增加，"层爆炸"反而掉帧。
- 治理：检查 Layers 面板层大小与数量；避免对大块内容 will-change；用 transform: translateZ(0) 仅对小块使用；动画结束后移除 will-change。
- 深水点：层的"绘制区域"会随阴影/溢出扩大——一个 overflow 元素可能让整层膨胀数倍。

```javascript
// 层内存估算器
function layerMemoryMB(layers) {
  return layers.reduce((s, l) =>
    s + (l.width * l.height * 4 * (l.devicePixelRatio ** 2)) / 1024 / 1024, 0);
}
// layers: [{ width: 1080, height: 1920, devicePixelRatio: 3 }]
console.log(layerMemoryMB([{ width: 1080, height: 1920, devicePixelRatio: 3 }]));
// -> ~71MB，一张全屏 3x 层就吃掉 71MB 显存
// 治理：动画结束 remove will-change，缩小提升范围
```
