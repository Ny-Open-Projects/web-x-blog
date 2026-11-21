---
title: [VIZ-124] 图例 legend 的滚动与交互实现原理？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-124：图例 legend 的滚动与交互实现原理？
**答**：legend 是 LegendComponent：① 布局——按 orient 排布 icon+text，`type: 'scroll'` 时放不下的分页：维护 pageIndex，两侧渲染翻页箭头并带翻页动画；② 交互——点击触发 `legendToggleSelect` action，内部维护 selectedMap，渲染时按选中态过滤/置灰，对外抛 `legendselectchanged` 事件；③ 文本溢出——formatter 截断 + tooltip 显示全名；④ 自定义——rich 文本与 itemStyle 覆盖，或关掉内置 legend 用 DOM 自绘再 dispatchAction 联动（大屏/SSR 场景常用）。

```javascript
// 滚动图例 + 自绘图例联动两种方案
chart.setOption({
  legend: {
    type: 'scroll', orient: 'horizontal',
    pageIconSize: 10, pageButtonItemGap: 6,
    formatter: name => name.length > 8 ? name.slice(0, 8) + '…' : name,
  },
});
chart.on('legendselectchanged', ({ name, selected }) => syncExternalLegend(name, selected));
// 方案二：DOM 自绘图例，走 action 通道联动（SSR/大屏场景）
legendDom.addEventListener('click', e => {
  const name = e.target.dataset.name;
  if (name) chart.dispatchAction({ type: 'legendToggleSelect', name });
});
```
