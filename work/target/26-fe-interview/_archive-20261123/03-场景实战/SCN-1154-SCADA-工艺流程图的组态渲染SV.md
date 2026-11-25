---
title: [SCN-1154] SCADA 工艺流程图的组态渲染（SVG 图元绑定）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1154：SCADA 工艺流程图的组态渲染（SVG 图元绑定）

**答**：
- 组态：工艺图由图元（管道/阀门/泵罐）组成，图元绑定点位（tag），状态驱动样式（阀门开闭色）。
- 实现：SVG 图元 + 状态映射表（tag 值 → 颜色/形状），动画（流动管道 dash 动画）。
- 性能：图元 < 2000 个 SVG 可用；更新按 tag 变化 patch（非全量重绘）。

```javascript
// 组态图元
const VALVE_STYLE = { open: 'fill:#1890ff', closed: 'fill:#999', fault: 'fill:#f5222d' };
function renderValve(el, tagValue) {
  const state = tagValue > 0.5 ? 'open' : tagValue < 0 ? 'fault' : 'closed';
  el.setAttribute('style', VALVE_STYLE[state]);
  el.setAttribute('data-state', state);
}
// 管道流动：stroke-dasharray + animate（有介质流动时才播放动画）
```
