---
title: [RBL-361] Rust 构建工具的内存管理要点（为什么它稳）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-361：Rust 构建工具的内存管理要点

**答**:
- 与 JS 工具的本质差异：无 GC 停顿（所有权系统确定性释放）——大项目构建的「内存增长→GC 频繁→变慢→OOM」链条在 Rust 工具中不存在
- 内存策略：AST/模块图用 arena/池化分配（同生命周期对象集中管理，分配快且释放整批）、增量数据用 mmap/序列化落盘（内存常驻小）
- 观测差异：JS 侧 heapUsed 曲线锯齿 vs Rust 侧 RSS 平稳——watch 长跑稳定性是 Rust 工具的隐性优势
- 工程含义：watch 进程不需要「自愈重启」兜底（JS 工具常见）——长期开发体验更稳

```text
内存对比：JS（GC 锯齿 + OOM 风险） vs Rust（所有权释放 + arena 池化，RSS 平稳）
工程含义：watch 长跑免自愈重启
```
