---
title: [WCN-117] WCN 与 Monorepo 构建体系怎么组织？（tokens/core/adapters/docs 四包联动）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-117：WCN 与 Monorepo 构建体系怎么组织？

**答**：
- 包结构：`tokens`（设计变量 → 产 CSS 变量/JSON）、`core`（WC 实现，依赖 tokens 类型）、`adapters`（react/vue 包装，依赖 core 的 manifest）、`docs`（Storybook/playwright）、`cli`（脚手架与 manifest 校验）。
- 构建链：tokens 构建产物 → core 打包（esbuild/rolldown，ESM+DTS）→ adapters 从 core 的 custom-elements.json 代码生成包装器与类型 → docs 引用全部。
- 工具链：pnpm workspace + Turborepo/Nx 缓存；`changesets` 管版本发布；manifest diff 进 CI（breaking 检测）。
- 产物规格：core 每组件单入口 + define 入口 + 仅类入口；adapters 产物带 tree-shakable 标记；全部 ESM。
- 联调：Storybook 直接跑 core（无框架），adapters 的宿主 demo 页作为集成测试目标。

```yaml
# turbo.json 关键流水线
{ "tasks": {
  "build": { "dependsOn": ["^build"], "outputs": ["dist/**", "custom-elements.json"] },
  "test": { "dependsOn": ["build"] },
  "lint:manifest": { "dependsOn": ["^build"] }   # manifest 破坏性变更检查
} }
```

```text
packages/
  tokens/    → dist/tokens.css, tokens.json
  core/      → src/button.js, dist/button.js, custom-elements.json
  adapters/  → src/gen/react.ts (由 core manifest 生成), dist/react.js
  docs/      → .storybook/, e2e/
```
