---
title: [DP-239] 源码识别：ECharts/ZRender 源码中的事件代理与拾取？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-239：源码识别：ECharts/ZRender 源码中的事件代理与拾取？
**答**:
- 事件代理（核心）：canvas 只有一个 DOM，库在容器上监听一次，内部按坐标**拾取**（hit-test）映射到图形元素再派发 chart.on('click')——单一监听器 + 内部路由，DOM 事件代理的 canvas 版。
- 拾取策略：几何拾取（数学判定点是否在形状内）vs 像素拾取（isPointInPath/颜色缓存），大数据量走网格索引（空间划分 DP 前置）。
- 观察者：拾取后派发的事件系统（handler.on）与 chart 层事件（series 级聚合）是两级发布订阅。
- 识别要点：tooltip 的联动（axisPointer）就是"拾取 → 状态 → 观察者广播"三步链。

```javascript
// ZRender 事件路由（源码级简化）
canvas.addEventListener('click', e => {
  const [x, y] = toLocal(e);
  const hit = pickStrategy.find(x, y, displayList);   // 拾取策略
  if (hit) hit.trigger('click', e);                   // 元素级派发
  chartEmitter.emit('click', { seriesId: hit?.seriesId, data: hit?.dataItem });  // chart 级广播
});
const geometryPick = {                                 // 几何策略
  find(x, y, list) { return list.find(el => el.containsPoint(x, y)); },
};
const pixelPick = {                                    // 像素策略（复杂路径更稳）
  find(x, y, list) {
    for (const el of list.reverse()) {                 // 顶层优先
      if (ctx.isPointInPath(el.path2d, x, y)) return el;
    }
  },
};
// 大数据量：先网格索引粗筛 → 精确拾取（空间换时间）
```
