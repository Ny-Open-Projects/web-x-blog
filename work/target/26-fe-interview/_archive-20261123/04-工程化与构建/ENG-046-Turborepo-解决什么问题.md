---
title: [ENG-046] Turborepo 解决什么问题？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-046：Turborepo 解决什么问题？
**答**：
- 编排 monorepo 内的任务依赖关系：build 前先构建它依赖的包，多个无依赖包并行执行。
- 本地与远程缓存：输入（文件+环境）不变的任务直接复用产物，CI 提速显著。
- turbo.json 的 dependsOn: ['^build'] 表示"先构建我的上游依赖"，outputs 声明缓存哪些产物。
- 配合 GitHub Actions 的远程缓存，团队共享构建结果。

```javascript
// turbo.json
{
  "tasks": {
    "build": {
      // ^build 表示先构建当前包依赖的上游包
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "test": {
      "dependsOn": ["build"]
    }
  }
}

// 根目录执行 pnpm turbo build：全仓库按依赖拓扑并行构建
```

---

## 第十章 微前端（ENG-047 ~ ENG-048）
