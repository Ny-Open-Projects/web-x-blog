---
title: [ARC-022] Turborepo 的 task pipeline 与远程缓存如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-022：Turborepo 的 task pipeline 与远程缓存如何设计？
**答**：
- `turbo.json` 声明任务依赖关系：`build` 依赖上游包的 `build`（`^build`），`lint`/`test` 可并行，保证拓扑序正确。
- 远程缓存以"任务输入哈希"为键：输入不变直接命中缓存，CI 时间从分钟级降到秒级。
- 必须显式声明 inputs/outputs，否则缓存会"假命中"，这是 Turborepo 事故的第一来源。

```json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],          // 先构建依赖的上游包
      "inputs": ["src/**", "package.json", "tsconfig.json"],
      "outputs": ["dist/**"]            // 声明产物目录才能被缓存复用
    },
    "test": {
      "dependsOn": ["build"],           // 测试前先有构建产物
      "outputs": ["coverage/**"]
    },
    "lint": { "outputs": [] },          // 无产物，纯并行
    "dev": { "cache": false, "persistent": true }  // 长驻进程不缓存
  }
}
```
