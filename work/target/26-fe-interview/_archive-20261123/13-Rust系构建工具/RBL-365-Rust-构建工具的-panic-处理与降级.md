---
title: [RBL-365] Rust 构建工具的 panic 处理与降级策略
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-365：Rust 构建工具的 panic 处理与降级策略

**答**:
- panic 语义：Rust panic ≠ JS throw（unwinding 到边界）——NAPI 层把 panic 转成 JS 异常（catch_panic 包装），但跨 FFI 边界的 panic 需要 abort 安全（panic = abort 配置的权衡）
- 用户侧处理：panic 信息（backtrace + 触发输入）→ 生成 issue 模板（工具方收 bug 的入口）；RUST_BACKTRACE=1 环境变量指导
- 降级设计：Native 崩溃 → JS 层捕获 → 提示切换 JS 实现（如 builtin loader 不可用时 fallback JS loader）——关键路径双实现兜底
- 与 JS 工具对比：JS 工具崩溃常是内存 OOM（进程死），Rust 工具崩溃多是逻辑 bug（罕见）——稳定性差异的来源

```text
panic 链：Rust panic → NAPI catch → JS Error + backtrace + issue 模板
降级：关键路径双实现（native 崩 → JS fallback）
```
