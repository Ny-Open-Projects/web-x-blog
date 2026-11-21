---
title: [ENG-193] 从 webpack 迁移 vite 的工程管理面怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-193：从 webpack 迁移 vite 的工程管理面怎么做？
**答**：
- 管理面与单仓改造分开：策略是并行期双构建（vite 为主 webpack 兜底）→ 特性对齐清单 → 全量切换 → 移除 webpack。
- 对齐清单驱动：环境变量机制差异、CSS Modules 命名、publicPath、HMR 边界、每个 webpack 插件的 vite 替代映射表。
- 风险最大三点：CommonJS 与动态 require 依赖、mock 与 proxy 规则迁移、依赖 loader 的第三方库。
- 验收指标量化：本地启动与热更提速数据、双构建产物 diff 报告、E2E 全量通过，达标才允许切默认构建。

```javascript
// scripts/migration-parity-check.mjs —— webpack 与 vite 双构建产物对齐检查
import { execSync } from 'node:child_process'
import { compare } from './bundle-diff.mjs'

// 1. 双构建并行期产物
execSync('npx webpack --mode production --output-path dist-wp', { stdio: 'inherit' })
execSync('npx vite build --outDir dist-vite', { stdio: 'inherit' })

// 2. 产物 diff 模块清单 chunk 结构 总体积
const diff = await compare({ a: 'dist-wp', b: 'dist-vite' })
console.log('总体积变化:', diff.totalDelta)
console.log('仅 webpack 产物包含的模块:', diff.onlyInA.slice(0, 20))

// 3. 卡口 模块缺失或体积暴涨超 10% 阻断切换
if (diff.onlyInA.length > 0 || diff.totalDeltaRatio > 0.1) {
  console.error('对齐未通过 禁止切换默认构建')
  process.exit(1)
}
```
