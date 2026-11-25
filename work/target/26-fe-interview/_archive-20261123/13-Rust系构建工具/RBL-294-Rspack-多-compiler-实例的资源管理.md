---
title: [RBL-294] Rspack 多 compiler 实例的资源管理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-294：Rspack 多 compiler 实例的资源管理

**答**:
- 场景：多入口多目标（web+node SSR 同时构建）需要多 compiler——每个实例独立模块图与缓存，内存是 N 倍关系
- 资源策略：串行化大实例（内存优先）或并行（时间优先）——按实例内存画像分桶；共享只读数据（browserslist/配置解析）尽量复用
- 生命周期：watch 场景所有实例统一重启策略（一个 OOM 全体重启）；关闭时统一 dispose 释放 Native 资源（忘 close 是 Native 泄漏高发点）
- 架构替代：能用一个 compiler 的多 entry 解决就不开多实例（共享依赖只打包一次）；确需多实例用子进程隔离（崩溃面隔离）

```javascript
// 实例生命周期
const compilers = rspack(configs)   // 多配置
process.on('exit', () => compilers.forEach((c) => c.close(() => {})))   // 释放 Native 资源
```
