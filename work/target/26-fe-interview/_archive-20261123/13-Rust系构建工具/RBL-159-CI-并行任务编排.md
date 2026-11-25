---
title: [RBL-159] CI 里的并行任务编排：并发度与依赖怎么平衡
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-159：CI 里的并行任务编排：并发度与依赖怎么平衡

**答**：
- 两层并行：包间并行（依赖图无关联的包同时构建）+ 单包内并行（Rspack 内部已多线程）；编排器只管第一层。
- 并发度设置：turbo run --concurrency 默认 = CPU 核数；CI 机器核少时开太多并发只会互相抢 IO/内存——2C 机器建议 concurrency=2~3，并考虑把内存型任务（Rspack build）与 IO 型（lint）分开档。
- 依赖约束：dependsOn 保证拓扑序（^build = 上游 build 先完成）；并行安全前提是"任务只读上游产物、只写自己目录"，写出 workspace 根的共享文件会竞态。
- 编排反模式：用 && 手工串联本可并行的独立任务；在编排器外又套一层 shell 并行导致日志交错难排查。
- 追问钩子：并发还受"共享缓存写入"约束——多个任务同时写本地缓存目录需工具自身有锁（turbo/nx 内部处理，自研 runner 要注意）。

```json
// turbo.json —— 显式编排示例
{
  "tasks": {
    "lint": {},                       // 无依赖：所有包 lint 立即并行
    "typecheck": { "dependsOn": ["^build"] },
    "build": { "dependsOn": ["^build", "^lint"] },  // 上游 build+lint 完才轮到自己
    "deploy": { "dependsOn": ["build", "test"], "cache": false } // 部署不缓存
  }
}
// CI 调用：
// turbo run lint typecheck --concurrency=3    # 快任务先并行铺开
// turbo run build test --concurrency=2       # 重任务低并发防 OOM
```
