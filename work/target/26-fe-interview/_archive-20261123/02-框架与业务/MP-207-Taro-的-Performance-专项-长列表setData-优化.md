---
title: [MP-207] Taro 项目的长列表与 setData 性能专项怎么做？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-207：Taro 长列表与 setData 性能专项？
**答**：
- 长列表：Taro 的虚拟列表组件（Virtuoso 思路）——只渲染视口条目 + 定高/动高适配；react 虚拟化与小程序渲染层的桥接（占位撑高）。
- setData 纪律：高频更新（输入/滚动）节流合并；大对象避免全量替换（路径 patch）；大列表分页加载而非一次注入。
- 渲染层：减少深层嵌套（模板递归深度）、列表项抽自定义组件（隔离 diff 边界）。
- 工具：Taro DevTools 的 setData 面板看数据量分布；getPerformance 接口拿 setData 耗时。
- 预算：单次 setData < 256KB、页面首屏 setData 次数 < 5。
