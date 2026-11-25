---
title: [RBL-251] monorepo 并行构建的并发度与资源控制
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-251：monorepo 并行构建的并发度与资源控制

**答**:
- 并发度默认 = CPU 核数；但构建是 IO+CPU 混合，重类型检查任务会内存爆炸——按「资源画像」分级：CPU 密集任务并发 = 核数，内存密集（tsc/webpack）并发 = 内存预算 / 单任务峰值
- 资源画像数据：历史上每任务峰值内存/耗时（CI 采集），驱动调度器权重（Nx 的任务执行细节、Turborepo 的 concurrency 配置）
- 队列调度：关键路径优先（最长路径先启动减少总时长）；内存紧张时降并发而不是 OOM 重跑（重跑成本更高）
- 分层限流：同时只允许 2 个 webpack 类构建 + 4 个轻任务（lint/test）——粗粒度分组比精细调度更稳

```json
// turbo.json 或 Nx 配置示意
{ "concurrency": 8 }
// 环境变量分级
{ "tasks": { "build": { "concurrency": 4 }, "lint": { "concurrency": 8 } } }
```
