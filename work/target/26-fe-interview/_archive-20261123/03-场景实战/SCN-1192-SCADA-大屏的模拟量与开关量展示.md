---
title: [SCN-1192] SCADA 大屏的模拟量与开关量展示规范
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1192：SCADA 大屏的模拟量与开关量展示规范

**答**：
- 规范：模拟量（数值+单位+小数位规范）、开关量（状态文字+颜色）——展示规范统一。
- 精度：仪表精度对应小数位（不显示无效精度）。
- 单位：国际单位规范（kW/kWh 区分）。

```javascript
// 展示规范
const DISPLAY_SPEC = {
  analog: { decimals: (precision) => precision, unit: true },
  digital: { states: { 0: { text: '停止', color: 'gray' }, 1: { text: '运行', color: 'green' } } },
};
function formatTag(tag) {
  return tag.type === 'analog'
    ? `${tag.value.toFixed(DISPLAY_SPEC.analog.decimals(tag.precision))} ${tag.unit}`
    : DISPLAY_SPEC.digital.states[tag.value]?.text ?? '未知';
}
```
