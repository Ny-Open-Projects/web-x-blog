---
title: [ENG-116] 架构约束怎么自动检查？边界规则 lint 怎么写？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-116：架构约束怎么自动检查？边界规则 lint 怎么写？
**答**：
- 分层约束用 ESLint no-restricted-imports：按目录圈定"业务层禁引基础设施、基础层禁反向上层"。
- 跨包约束交给 dependency-cruiser（见 Monorepo 章节），ESLint 负责单应用内的分层与模块禁令。
- message 里必须写"应该怎么改"，规则才会被遵守而不是被 eslint-disable 淹没。
- 与惯例配套：路径别名（@/features、@/infra）是规则可写的前提，先统一目录语义再上约束。

```javascript
// eslint.config.mjs：分层架构约束（flat config 是一个数组，每项是一组配置）
export default [
  {
    files: ['src/features/**/*.{ts,tsx}'],
    rules: {
      'no-restricted-imports': ['error', {
        patterns: [
          { group: ['@/infra/*'], message: '业务层禁止直接依赖基础设施，请通过 usecases 层调用' },
          { group: ['@/app/*'], message: '业务层不得反向依赖应用入口' },
        ],
      }],
    },
  },
  {
    files: ['src/shared/**'],
    rules: {
      'no-restricted-imports': ['error', {
        patterns: [
          { group: ['@/features/*'], message: '基础层不得依赖业务模块' },
        ],
      }],
    },
  },
];
```
