---
title: [VIZ-035] 如何把设计 Token 接入 ECharts 主题体系？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-035：如何把设计 Token 接入 ECharts 主题体系？
**答**：`echarts.registerTheme(name, themeObj)` 注册全局主题，`init(el, name)` 时绑定；主题覆盖色板、字体、各轴/组件默认样式。关键工程决策：**主题不支持热切换**——换肤要么 dispose 重建，要么（推荐）把颜色抽成设计 Token/CSS 变量，option 里引用 Token 生成的值，setOption merge 更新。这样多主题、暗色模式、品牌定制都收敛到 Token 一处维护，图表侧永远不写死 hex。

```javascript
// 设计 Token -> ECharts 主题，一次注册多处使用
const tokens = {
  color: { primary: '#3b82f6', text: '#334155', split: '#e2e8f0' },
  palette: ['#3b82f6', '#f59e0b', '#10b981', '#8b5cf6'],
};
echarts.registerTheme('brand', {
  color: tokens.palette,
  textStyle: { fontFamily: 'PingFang SC, sans-serif' },
  title: { textStyle: { color: tokens.color.text } },
  categoryAxis: { axisLine: { lineStyle: { color: tokens.color.split } } },
});
const chart = echarts.init(el, 'brand'); // init 时绑定主题，主题不支持热切换
// 换肤策略 A：dispose 重建（简单但有闪屏）；策略 B：Token 生成 option 后 setOption merge（推荐）
function themedOption(t) {
  return { color: t.palette, textStyle: { color: t.color.text } };
}
```
