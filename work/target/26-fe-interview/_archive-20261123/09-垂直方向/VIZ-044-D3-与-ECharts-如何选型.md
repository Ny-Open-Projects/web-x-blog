---
title: [VIZ-044] D3 与 ECharts 如何选型？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-044：D3 与 ECharts 如何选型？
**答**：ECharts 是**配置驱动的成品图表库**：开箱即用、内置交互/主题/大数据方案、交付快、团队上手低，覆盖 90% 业务图表；D3 是**可视化原语集**：数据 join、比例尺、布局器、过渡全是零件，自由度无限但人力成本高，适合深度定制、学术可视化、自研图表库底座。决策要素：定制深度、数据量、维护人力、导出/SSR 要求。折中路线：业务用 ECharts + 个别定制图用 D3（或 ECharts custom series），自研平台用 D3/AntV 底层。

```javascript
function pickLib(requirement) {
  const matrix = {
    '标准业务图表+快速交付': 'ECharts',
    '深度定制+学术级可视化': 'D3',
    '3D/大规模粒子/游戏化': 'Three.js 或 WebGL 原生',
    '关系图+图分析': 'AntV G6',
    '地理大屏+飞线': 'ECharts geo 或 deck.gl',
    '移动端轻量 H5': 'AntV F2',
  };
  return matrix[requirement] ?? 'ECharts 默认';
}
// 决策要素：定制深度、数据量、团队维护成本、SSR/导出需求、包体积
// ECharts 是配置驱动的成品；D3 是可视化原语集，自由度与人力成本都最高
```

---

## 七、图表类型原理（VIZ-045 ~ VIZ-052）
