---
title: [ENG-107] Turborepo 的完整管道怎么配置？dependsOn、inputs、outputs 各管什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-107：Turborepo 的完整管道怎么配置？dependsOn、inputs、outputs 各管什么？
**答**：
- dependsOn 声明任务依赖：^build 表示先构建所有上游依赖包；test 依赖 build 保证测的是新产物。
- inputs 声明任务输入指纹：源码、tsconfig 变了才重建；漏声明会导致"改了代码却命中旧缓存"。
- outputs 声明任务产物：dist/**、coverage/**，命中缓存时直接恢复这些目录。
- dev 任务必须 cache: false + persistent: true，长驻进程不能也不该进缓存。

```json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["$TURBO_DEFAULT$", "src/**", "tsconfig.json", "package.json"],
      "outputs": ["dist/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"]
    },
    "lint": { "outputs": [] },
    "dev": { "cache": false, "persistent": true }
  }
}
```
