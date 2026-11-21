---
title: [RBL-141] Oxlint 与 ESLint 的差异？如何渐进式迁移
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-141：Oxlint 与 ESLint 的差异？如何渐进式迁移

**答**：
- 性能：oxlint 全 Rust 实现，万文件级仓库 lint 从分钟级到秒级（官方基准 50~100 倍），零配置即可跑（内置几百条规则）。
- 规则来源：对齐 ESLint、typescript-eslint、react/react-hooks、unicorn、jest 等常见规则集，命名基本一致（如 no-console、exhaustive-deps）。
- 差异/限制：不支持 ESLint 的大部分自定义 JS 插件 API；autofix 覆盖子集；复杂 project service（type-aware 规则）历史上靠 ts-eslint 语义信息模拟，覆盖面在增长。
- 迁移策略：oxlint 先跑"快规则"挡门（pre-commit / CI 快检），ESLint 保留 type-aware 规则与自定义插件，配置里关掉已被 oxlint 接管的规则避免重复报错。
- 追问钩子：oxlint 支持 .oxlintrc.json 与 ESLint flat config 风格继承，双跑期间用 CI 统计两边的规则命中 diff 再逐步收敛。

```json
// .oxlintrc.json —— 渐进迁移配置
{
  "extends": ["plugin:@oxlint/typescript", "plugin:@oxlint/react", "plugin:@oxlint/react-hooks"],
  "plugins": ["typescript", "unicorn", "react"],
  "categories": { "correctness": "error" },
  "rules": {
    "no-console": "warn",
    "eqeqeq": "error",
    "no-unused-vars": "error"
  },
  "ignorePatterns": ["dist/**", "coverage/**", "*.min.js"]
}
// package.json scripts：
// "lint": "oxlint && eslint . --rulesdir custom-rules"  // oxlint 快检 + ESLint 收尾
```
