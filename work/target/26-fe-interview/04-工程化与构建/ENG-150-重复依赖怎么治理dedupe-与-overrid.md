---
title: [ENG-150] 重复依赖怎么治理？dedupe 与 overrides 实战怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-150：重复依赖怎么治理？dedupe 与 overrides 实战怎么做？
**答**：
- 重复依赖来源：不同包各自声明同一库的不同大版本、peer 未对齐、patch 漂移；后果是体积翻倍与双实例风险（如双 React hooks 报错）。
- 诊断优先：pnpm why lodash 找出重复路径与引入链，dedupe --check 拿到可收敛清单，确认后再动手。
- 收敛手段：overrides 强制统一版本（npm/pnpm/yarn 语法不同）、packageExtensions 补 peer 声明、必要时 fork 收窄旧版本包。
- 收敛后必须全量回归：强制 override 等于替第三方做兼容决策，测试兜底 + 版本写进 lockfile。

```json
{
  "name": "app",
  "pnpm": {
    "overrides": {
      "lodash": "4.17.21",
      "moment>zone.js": "0.14.10"
    },
    "packageExtensions": {
      "@some/old-lib@*": {
        "peerDependencies": { "react": "^18.0.0" }
      }
    }
  },
  "resolutions": {
    "@babel/traverse": "7.24.7"
  },
  "scripts": {
    "dedupe:check": "pnpm dedupe --check",
    "why:lodash": "pnpm why lodash"
  }
}
```
