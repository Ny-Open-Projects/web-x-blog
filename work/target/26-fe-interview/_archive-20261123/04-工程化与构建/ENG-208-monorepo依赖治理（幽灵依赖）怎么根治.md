---
title: [ENG-208] monorepo 的幽灵依赖（phantom deps）怎么根治？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-208：幽灵依赖怎么根治？
**答**：
- 根因：npm/yarn 扁平化 hoisting 让未声明依赖「意外可用」；pnpm 默认严格隔离（.pnpm 目录）从机制上消除——选型即治理。
- 检测手段：pnpm 的 `strict-peer-dependencies` + ESLint no-extraneous-dependencies（import 未声明包报错）+ CI 干净环境安装验证（全新机器 build 失败即有幽灵依赖）。
- 治理路径：检测清单 → 批量补声明（脚本自动补进 package.json）→ 门禁拦截新增——存量补齐增量拦截。
- peer dependencies 策略：库包把宿主框架声明为 peerDep（避免双 React），monorepo 内用 catalog 统一 peer 版本。
- 追问钩子：为什么「新机器能 build」是幽灵依赖的金标准检测——本地 node_modules 有历史安装残留（曾经依赖过），只有干净环境的解析才反映真实依赖声明。

```jsonc
// .eslintrc —— import 边界
{ "rules": { "import/no-extraneous-dependencies": ["error", {
  "peerDependencies": false, "devDependencies": ["**/*.test.*"] }] } }
```
```bash
# CI 幽灵依赖检测：干净环境 + frozen lockfile
pnpm install --frozen-lockfile --force && pnpm -r build  # 失败即幽灵依赖
```
