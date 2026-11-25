---
title: [WEB-174] Performance 面板的火焰图怎么读？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-174：Performance 面板的火焰图怎么读？
**答**：
- 主线程泳道自上而下是调用栈：宽度等于占用时间，颜色区分类型（脚本/样式/绘制），找最宽的块就是瓶颈。
- 长任务有红色三角标记；红色斜纹表示强制同步布局；Recalculate Style 与 Layout 要分开看。
- Network 泳道与主线程对照：接口快但页面卡，说明卡在拿到数据后的处理。
- Bottom-Up 视图按自耗时间排序直接看"谁最费"；录制前开 CPU 降速复现低端机。

```javascript
// 用 console API 圈定录制区间，避免长录制淹没关键路径
console.profile('list-render');
renderList(5000);              // 疑似卡顿的代码路径
console.profileEnd('list-render');
// 在 Performance 面板里按 list-render 区间定位：
// 优先找长脚本任务，以及 Recalculate Style 后紧跟 Layout 的强制同步布局
```
