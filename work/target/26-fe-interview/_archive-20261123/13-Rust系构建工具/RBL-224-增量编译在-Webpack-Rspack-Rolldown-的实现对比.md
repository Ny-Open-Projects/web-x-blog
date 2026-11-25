---
title: [RBL-224] 增量编译在 webpack/Rspack/Rolldown 里的实现差异
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-224：增量编译在 webpack/Rspack/Rolldown 里的实现差异

**答**:
- webpack：watch 模式内存在增量（模块图常驻），但无跨进程持久化（构建结束丢图）；持久缓存（filesystem.cache）是「产物级持久化」非「图持久化」
- Rspack：Rust 侧模块图 + 持久缓存，watch 增量重建更快；跨进程靠缓存复水（快但仍有复水成本）
- Rolldown：目标持久化模块图（进程间共享），增量粒度更细（chunk 级跳过渲染）
- 面试框架：三者的差异本质是「增量状态的存活时长」——watch 内（秒级）→ 持久缓存（天级）→ 持久图（进程重启级）

```text
webpack:  watch 内存增量 | cache 产物持久化
rspack:   Rust 图 + 产物持久化（复水）
rolldown: 目标 = 持久化模块图（重启级增量）
```
