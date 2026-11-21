---
title: [VIZ-034] ECharts 的事件与交互体系如何使用？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-034：ECharts 的事件与交互体系如何使用？
**答**：两层事件：**chart 级**（`chart.on('click', params)`）是语义事件，带 seriesIndex/dataIndex/value，支持 query 过滤（`'series.line'`）；**ZRender 级**（`chart.getZr().on('click')`）是像素级事件，点击空白区也能拿到坐标，配合 `convertFromPixel` 可做自定义区域选择。程序驱动交互用 `dispatchAction`（highlight/showTip/dataZoom），这是"外部状态同步到图表"的唯一正道。高频事件（mousemove/graphRoam）必须节流。

```javascript
chart.on('click', 'series.line', params => {           // query 过滤：只听 line 系列
  console.log(params.name, params.value, params.dataIndex);
});
chart.getZr().on('click', p => {                       // ZRender 级：点空白也拿坐标
  const pixel = [p.offsetX, p.offsetY];
  const data = chart.convertFromPixel('grid', pixel);  // 像素 -> 数据坐标
  console.log('落在数据点', data);
});
// 程序驱动：外部按钮高亮某点 / 打开 tooltip
chart.dispatchAction({ type: 'showTip', seriesIndex: 0, dataIndex: 3 });
chart.dispatchAction({ type: 'highlight', seriesIndex: 0, dataIndex: 3 });
// 注意：dispatchAction 也会触发 on 事件，联动代码要做来源标记防循环
```
