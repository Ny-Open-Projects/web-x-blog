---
title: [VIZ-135] 可视化的国际化怎么做？多语言标注与 RTL
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-135：可视化的国际化怎么做？多语言标注与 RTL
**答**：四块：① **文案**——图例/轴标签/tooltip 走 i18n 函数；② **数字与时间**——`Intl.NumberFormat`（千分位/货币/紧凑记法）与 `Intl.DateTimeFormat`（月名/周起始日）按 locale 格式化，禁止手写；③ **RTL**——阿拉伯语等从右向左：坐标轴 inverse 反转、图例与 tooltip 位置镜像、容器 `direction: rtl`、Canvas 文字用 `ctx.direction`；④ **长度与语义**——德语长词撑爆标签要截断换行，涨跌颜色语义 locale 化（国内红涨绿跌）。国际化要在设计阶段进入色板与布局评审，不能后补。

```javascript
// i18n 可视化工具集：数字/时间/文案/RTL
const i18n = {
  'zh-CN': { legendTotal: '合计', yAxisUnit: '万元' },
  'en-US': { legendTotal: 'Total', yAxisUnit: 'k USD' },
  'ar-SA': { legendTotal: 'المجموع', yAxisUnit: 'ألف' },
};
function buildOption(lang, rows) {
  const t = i18n[lang], rtl = lang === 'ar-SA';
  const numFmt = new Intl.NumberFormat(lang, { notation: 'compact', maximumFractionDigits: 1 });
  const timeFmt = new Intl.DateTimeFormat(lang, { month: 'short' });
  return {
    xAxis: { type: 'category', inverse: rtl,                 // RTL 轴反转
      data: rows.map(r => timeFmt.format(new Date(r.t))) },
    yAxis: { name: t.yAxisUnit, inverse: rtl },
    legend: { left: rtl ? 'right' : 'left' },                // 图例镜像
    tooltip: { formatter: p => `${t.legendTotal}: ${numFmt.format(sum(p))}` },
  };
}
container.style.direction = rtl ? 'rtl' : 'ltr';  // DOM 容器方向；Canvas 内用 ctx.direction
```
