---
title: [FRP-265] SSR 水合成本：各家框架对比？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-265：SSR 水合成本对比？
**答**：
- React：重建 fiber 树 + hydrate——成本最高但选择性水合/流式成熟。
- Vue：同构 render 函数 + hydrate，VDOM 重建；Vapor 模式 claim 路径更轻（实验）。
- Solid：认领 DOM + 建立订阅，无 vnode 重建——水合成本最低档；delegated events 支持水合前交互。
- Astro islands：静态部分零水合，岛按需——总执行量最小。
- 结论：水合成本 = 树重建成本 + 订阅建立成本，编译时框架两项都省。
