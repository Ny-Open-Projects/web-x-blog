---
title: [VIZ-036] 如何实现多图联动（connect/group）？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-036：如何实现多图联动（connect/group）？
**答**：把多个实例设同一个 `chart.group`，再 `echarts.connect(groupName)`，组内自动同步：dataZoom、tooltip、legend、brush 等 action 广播到全组。适合"多个图表共享时间轴"的大盘场景。底层是实例间 action 事件转发，所以自定义 action 也能通过该机制扩展。注意：联动是双向的，A 触发 B、B 又触发 A 的循环由内部屏蔽，但自己再叠一层 dispatch 时要防环；dispose 时组引用会残留，销毁要置空 group。

```javascript
const charts = [echarts.init(el1), echarts.init(el2), echarts.init(el3)];
charts.forEach(c => { c.group = 'dashboard'; }); // 同 group 互相联动
echarts.connect('dashboard');
// 效果：任意图的 dataZoom / tooltip / legend / brush 操作同步到组内其它图
// 场景：多个指标图共享时间窗口，滑一个全部跟着滑
charts.forEach(c => c.on('datazoom', () => console.log('时间窗口已同步')));
// 销毁：dispose 后置空 group，避免组引用残留导致实例无法回收
charts.forEach(c => { c.dispose(); c.group = null; });
```
