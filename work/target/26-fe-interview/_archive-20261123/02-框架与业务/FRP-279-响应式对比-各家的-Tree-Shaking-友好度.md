---
title: [FRP-279] Tree-shaking 友好度：各家框架对比？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-279：Tree-shaking 友好度对比？
**答**：
- Svelte/Solid：helper 按需 import + 编译产物静态引用——摇树效率最高。
- Vue：runtime 按 helper 收集（编译期 helper 声明），特性开关（optionsAPI）可关——中等偏上；Vapor 进一步细化。
- React：runtime 不可分（核心一体），但 RSC 场景 server/client 分包天然裁剪。
- 通用前提：ESM 产物 + 无副作用标注（sideEffects: false）+ 避免动态访问。
- 面试表达：shaking 效率 = 「模块图静态性 × 编译期信息量」。
