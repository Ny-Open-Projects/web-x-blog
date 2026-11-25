---
title: [VIZ-122] ECharts 的 tooltip 是如何实现的？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-122：ECharts 的 tooltip 是如何实现的？
**答**：tooltip 不画在 canvas 里，而是**独立 DOM div**。链路：① 事件层捕获 pointermove → zrender 命中检测找到图元 → 触发 series highlight；② 数据查询——`trigger: 'item'` 取单图元数据，`'axis'` 按坐标系轴索引换算取跨系列对齐数据；③ 渲染——`formatter` 生成 HTML 写入 div，绝对定位 + 贴边自动翻转（position 回调可完全接管）；④ 性能——transitionDuration 动画、appendToBody、大数据配 axisPointer snap 与节流；⑤ 跨图表同步即各实例 axisPointer link 共享十字线。

```javascript
// tooltip：formatter 定制 + 轴触发 + 位置接管 + 跨图同步
chart.setOption({
  tooltip: {
    trigger: 'axis',
    axisPointer: { type: 'cross', snap: true },
    transitionDuration: 0.1,
    formatter: params => `<b>${params[0].axisValue}</b>` + params.map(p =>
      `<div>${p.marker}${p.seriesName}: ${fmt(p.value)}</div>`).join(''),
    position: (point, params, dom, rect, size) => ({
      // 边界翻转：右半屏出左侧 tooltip
      pos: [point[0] + 12, Math.max(0, point[1] - size.contentSize[1] / 2)],
    }),
  },
  axisPointer: { link: [{ xAxisIndex: 'all' }] },  // 多实例联动共享十字线
});
```
