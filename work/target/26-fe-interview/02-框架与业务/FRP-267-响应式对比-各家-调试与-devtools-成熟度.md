---
title: [FRP-267] 各家调试与 devtools 成熟度对比？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-267：各家 devtools 成熟度？
**答**：
- React：DevTools 最成熟（Profiler/组件状态编辑/Suspense 可视化），生态工具链最深。
- Vue：devtools 组件树/Pinia 时间线/组合式函数追踪，中文社区活跃。
- Solid：solid-devtools 信号依赖图独一份，但生态工具整体较少。
- Svelte：devtools 有块级状态检查，Runes 后逐步补齐。
- 结论：调试生态 = 主流度函数，选型时把「团队排障效率」算进总账。
