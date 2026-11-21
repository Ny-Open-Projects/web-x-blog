---
title: [RBL-362] Rust 构建工具的并行模型（rayon 与任务池）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-362：Rust 构建工具的并行模型

**答**:
- 两层并行：数据并行（rayon：模块转换/压缩等可分片计算按核数并行——work-stealing 调度）与任务并行（tokio/task pool：IO 任务/进程管理异步调度）
- 与 JS 并行差异：JS 多进程（通信/序列化成本）vs Rust 多线程（共享内存零拷贝）——同机并行效率数量级差异
- 并行正确性：Rust 所有权/借用检查从语言层杜绝数据竞争——并行 bug（竞态）在编译期暴露而非运行时偶发
- 工程含义：核数扩展接近线性（scaling 好）——大 fixture 上 Rust 工具的优势放大（这正是 fixture 分级测试的意义）

```text
并行两层：rayon 数据并行（转换/压缩）+ tokio 异步（IO/进程）
差异：JS 多进程序列化 vs Rust 多线程零拷贝；竞态编译期杜绝
```
