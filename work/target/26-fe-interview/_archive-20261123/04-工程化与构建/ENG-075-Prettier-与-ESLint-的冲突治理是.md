---
title: [ENG-075] Prettier 与 ESLint 的冲突治理是怎么演进的？现在推荐怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-075：Prettier 与 ESLint 的冲突治理是怎么演进的？现在推荐怎么做？
**答**：
- 第一阶段：eslint-config-prettier 关掉所有与 Prettier 重复的格式规则，两工具分工。
- 第二阶段：eslint-plugin-prettier 把 Prettier 作为一条 lint 规则跑，好处是统一出口，代价是慢且报错信息差。
- 现在（推荐）：格式完全交给 Prettier（编辑器保存即格式化 + CI 跑 prettier --check），ESLint 只管代码质量。
- 关键是职责分离：格式问题不用 lint 报错，质量规则（no-unused-vars、eqeqeq）Prettier 也不插手。

```javascript
// eslint.config.mjs：职责分离的推荐结构
import eslintConfigPrettier from 'eslint-config-prettier';

export default [
  ...qualityConfigs,        // ESLint 只保留质量规则：no-unused-vars、eqeqeq 等
  eslintConfigPrettier,     // 放最后：兜底关闭一切与 Prettier 冲突的格式规则
  // 不再使用 eslint-plugin-prettier，格式问题由独立的 prettier --check 把关
];
```

```bash
# CI 中格式与质量分开校验
pnpm prettier --check .
pnpm eslint .
```
