---
title: [VIZ-140] 指标卡与同环比（YoY / MoM）的实现？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-140：指标卡与同环比（YoY / MoM）的实现？
**答**：指标卡三要素：**主指标值 + 同比/环比徽标 + 迷你趋势 sparkline**。口径必须写成纯函数避免扯皮：环比 = (本期 - 上期) / 上期，同比 = (本期 - 去年同期) / 去年同期；分母为 0 或上期缺失显示 "--" 而不是 Infinity/NaN。视觉：涨跌色语义可配置（国内红涨绿跌），▲/▼ 符号；数值走 Intl 紧凑记法；sparkline 是 40x16 的无轴迷你折线。指标卡是最高频复用组件，口径计算务必独立可测。

```javascript
// 同环比纯函数 + 指标卡渲染
function growth(cur, prev) {
  if (prev == null || prev === 0 || !Number.isFinite(cur)) return null; // 不可比显示 null
  return (cur - prev) / prev;   // 0.234 表示 +23.4%
}
function kpiCard({ label, value, cur, prev, prevYear, spark }) {
  const fmt = v => new Intl.NumberFormat('zh-CN',
    { notation: 'compact', maximumFractionDigits: 1 }).format(v);
  const badge = g => g == null ? '<span class="muted">--</span>'
    : `<span class="${g >= 0 ? 'up' : 'down'}">${g >= 0 ? '▲' : '▼'}${Math.abs(g * 100).toFixed(1)}%</span>`;
  return `<div class="kpi">
    <div class="kpi-label">${label}</div>
    <div class="kpi-value">${fmt(value)}</div>
    <div class="kpi-meta">同比${badge(growth(cur, prevYear))} 环比${badge(growth(cur, prev))}</div>
    <svg viewBox="0 0 40 16">${sparkline(spark)}</svg>   <!-- 迷你趋势线 -->
  </div>`;
}
function sparkline(data) {
  const min = Math.min(...data), max = Math.max(...data), n = data.length;
  return `<path d="${data.map((v, i) =>
    `${i ? 'L' : 'M'}${(i / (n - 1) * 40).toFixed(1)} ` +
    `${(16 - (v - min) / (max - min || 1) * 14 - 1).toFixed(1)}`).join('')}"/>`;
}
```
