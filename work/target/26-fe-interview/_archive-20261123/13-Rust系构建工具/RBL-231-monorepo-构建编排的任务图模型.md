---
title: [RBL-231] monorepo 构建编排的任务图模型怎么建
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-231：monorepo 构建编排的任务图模型怎么建

**答**:
- 任务图：节点 = (包, 任务)（如 core#build / app#build），边 = 依赖关系（app#build dependsOn core#build）；图由 workspace 依赖声明自动推导
- 调度原则：拓扑序执行（依赖先行）+ 可并行分支并发（无依赖关系的包同时 build）；关键路径决定总时长——缩短靠并行度与任务粒度
- dependsOn 三种语义：'^build'（依赖包的 build 先跑）、'build'（同包内序）、输出传递（依赖包的 dist 作为输入）
- 工具映射：Turborepo turbo.json / Nx project.json 的 target 声明都是这个模型的配置化表达

```json
// turbo.json
{
  "tasks": {
    "build": { "dependsOn": ["^build"], "outputs": ["dist/**"] },
    "test": { "dependsOn": ["build"] },
    "lint": {}                                      // 无依赖可全并行
  }
}
```
