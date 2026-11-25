---
title: [ENG-003] lockfile 的作用是什么？CI 中应该怎么装依赖？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-003：lockfile 的作用是什么？CI 中应该怎么装依赖？
**答**：
- lockfile 锁定整棵依赖树的精确版本与完整性 hash，保证任何机器上装出完全相同的结果。
- 提交 lockfile 到仓库是团队共识：没有它，传递依赖的次版本更新可能让不同环境行为不一致。
- CI 中必须用"严格模式"安装：npm ci / pnpm install --frozen-lockfile / yarn --immutable。
- lockfile 与 package.json 不一致时严格模式直接报错，防止版本漂移。

```bash
# 严格按 lockfile 安装，CI 中必须使用
npm ci
pnpm install --frozen-lockfile
yarn install --immutable

# lockfile 变更必须作为代码变更的一部分提交
git status --short package-lock.json pnpm-lock.yaml
```
