---
title: [FRP-301] 框架渲染模型光谱：VDOM、细粒度与编译时三路线
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## FRP-301：框架渲染模型光谱：VDOM、细粒度与编译时三路线

**答**：
- 三路线坐标：运行时 VDOM（React/Vue3 兼容）、细粒度响应式（Solid/Svelte5 runes/Vue Vapor）、编译时（Svelte4/Solid 编译器）——核心差异是「更新传播路径长度」
- VDOM 路线：状态变化 → 重渲染函数 → diff → patch；代价是 render+diff，收益是声明式模型统一（并发/SSR/跨端友好）
- 细粒度路线：状态变化 → 通知订阅该状态的 DOM 绑定直接更新——无 diff，但「快照语义」缺失（并发渲染难做）
- 编译时路线：编译期确定依赖与更新点（Svelte4）——运行时最轻，但动态性受限（运行时才知道的结构编译器管不了）
- 趋势汇合：Vue Vapor（细粒度编译）、React Compiler（VDOM+自动细粒度）、Solid 2.0——三条路线在互相吸收

```text
传播路径长度:
  VDOM:   state → render → diff → patch        (4步)
  细粒度: state → 直接更新绑定                   (1步)
  编译时: 编译期生成定向更新代码                  (0步运行时)
每条路线的复杂度花在不同位置: 运行时/编译期/心智
```
