---
title: [RBL-085] Turbopack 的持久化缓存是如何设计的？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-085：Turbopack 的持久化缓存是如何设计的？
**答**：
- 缓存单元：任务结果 + 依赖边（哪个任务读了哪些输入）一起序列化；输入的版本用内容 hash/元数据（mtime、size、配置）标记。
- 存储位置：node_modules/.cache 或 Next 指定缓存目录，跨进程与跨 CI 机器可复用。
- 失效：内容或配置变更 → 对应任务失效 → 惰性重算；缓存无全局版本号（局部失效），配置大改时会有较多任务失效。
- 与 Rspack 持久缓存对比：粒度不同（函数级 vs 模块级），Turbopack 的理论命中率更高但缓存体积与序列化成本更大；两者都要处理"缓存膨胀"——定期清理低频命中条目。
- CI 应用：缓存目录挂 artifact，效果与 Rspack 相同——首次慢、后续秒级。
- 追问钩子：持久缓存的正确性前提是"依赖追踪无遗漏"——环境变量、Node 版本、文件系统这种隐式输入必须纳入追踪，否则会产出脏结果。

```text
持久缓存结构（示意）
.cache/turbopack/
├── task-results/   # 任务结果 blob（内容寻址）
├── deps/           # 依赖边记录：task → inputs
└── meta/           # 环境指纹（node 版本、env、配置 hash）
失效链：file hash 变 → 任务失效 → 消费时重算 → 新 blob 覆盖
CI：挂缓存目录 → 冷启动秒级
```
