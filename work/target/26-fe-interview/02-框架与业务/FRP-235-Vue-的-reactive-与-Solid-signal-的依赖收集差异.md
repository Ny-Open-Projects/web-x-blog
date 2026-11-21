---
title: [FRP-235] Vue 的 Proxy 依赖收集与 Solid 的显式 signal 有何本质差异？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-235：Vue Proxy 依赖收集 vs Solid 显式 signal？
**答**：
- Vue：Proxy 拦截读写，运行时动态收集——「读什么收集什么」，用户无感；代价是 Proxy 开销、深层遍历、解构丢失响应。
- Solid：显式 signal 计数器——依赖在 signal.get() 时记录，粒度精确到单个信号；无 Proxy 开销，但 API 显式（count()）。
- 深层对象：Vue reactive 全代理；Solid 需 createStore 的代理层（同样走 Proxy）——两者在深层结构上都用 Proxy。
- 性能：单字段高频更新 Solid 略优（无拦截开销）；复杂树形 Vue 与 Solid 相当。
- 殊途同归：Vue Vapor 在模板编译后也生成显式订阅——两派在产物层趋同。
