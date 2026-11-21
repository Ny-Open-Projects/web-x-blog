---
title: [VIZ-033] 如何用 renderItem 自定义 series？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-033：如何用 renderItem 自定义 series？
**答**：`type: 'custom'` 系列把绘制权交给 renderItem 回调：入参 `api` 提供 `value(维度)` 取数据、`coord([x, y])` 数据坐标转像素、`style()` 继承 itemStyle；返回一个 ZRender 图形描述（rect/sector/group/polygon 等）。它解决了"option 描述不了的图形"——K 线、区间带、风罗盘、自定义标牌。要点：返回的 shape 必须是像素坐标；数据变化时会自动重调 renderItem；配合 `encode` 声明维度用途，tooltip 与坐标轴才能正确联动。

```javascript
series: [{
  type: 'custom',
  encode: { x: 0, y: [1, 2] },        // 维度 0 做 x，维度 1/2 做 y 区间
  renderItem: (params, api) => {
    // api.coord：数据坐标 -> 像素坐标；api.value：取原始值
    const start = api.coord([api.value(0), api.value(1)]);
    const end = api.coord([api.value(0), api.value(2)]);
    return {
      type: 'rect',
      shape: {
        x: start[0] - 10,
        y: Math.min(start[1], end[1]),
        width: 20,
        height: Math.abs(start[1] - end[1]),
      },
      style: api.style(),             // 继承 itemStyle / 调色板颜色
    };
  },
  data: [[0, 10, 30], [1, 20, 45]],   // [类目, 低值, 高值]，可画区间条/K 线
}],
```
