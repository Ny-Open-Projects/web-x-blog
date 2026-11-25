---
title: [FRP-345] 框架运行时剖析：组件实例标识与 DevTools 协议
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 可观测]
type: 面试题
---

## FRP-345：框架运行时剖析：组件实例标识与 DevTools 协议

**答**：
- DevTools 的工作原理：框架暴露「实例树 + 状态快照」的内部协议（React DevTools backend hook / Vue devtools hook）——window.__REACT_DEVTOOLS_GLOBAL_HOOK__
- 实例标识：React 的 fiber id、Vue 的 uid——监控/埋点可借用（组件级耗时按 id 聚合）
- 自建 DevTools 面板：消费 hook 协议（树 + 状态 + 性能）——业务监控面板与官方 DevTools 同源数据
- 生产可用性：devtools hook 在生产构建中部分可用（Profiler API 是官方生产探针）——自建面板依赖 profiler 而非 hook（生产安全）
- 深水点：多框架实例的 DevTools 冲突（两个 React root 各自 hook 注册）——hook 面板按 renderer id 区分

```text
DevTools 协议:
  window.__REACT_DEVTOOLS_GLOBAL_HOOK__ → renderer 注册 (fiber 树/状态)
  window.__VUE_DEVTOOLS_GLOBAL_HOOK__  → app 注册 (组件树)
自建面板: 生产用 Profiler API (官方), dev 用 hook (全量)
多 root: 按 renderer id 区分面板
```
