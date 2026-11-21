---
title: [MP-255] WXS 性能实践：列表时间格式化案例的完整设计？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-255：WXS 时间格式化案例？
**答**：
- 场景：1000 条消息列表显示「x 分钟前」——逻辑层算好传字符串会占 setData 体积且过时；WXS 渲染层实时计算。
- 实现：fmt.wxs 导出 formatTime(ts, now)——相对时间/绝对时间分支；WXML 内 `<wxs module="fmt">` 引入，插值调用。
- 性能点：WXS 函数要幂等轻量（不能调 Date.now 以外的重 API——实际上 wxs 无 wx API）；now 从 data 传入或固定值。
- 对比方案：逻辑层预计算字符串（setData 大）vs WXS 实时（传输小，CPU 在渲染层）——列表场景 WXS 胜。
- 边界：WXS 语法是 JS 子集（无 ES6+ 全特性）、iOS/Android 引擎不同——只写安全子集。
