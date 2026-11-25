---
title: [ENG-201] monorepo 治理深水区：仓库规模到千包后最先崩的是什么？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-201：monorepo 千包规模最先崩什么？
**答**：
- 最先崩的是「依赖解析与锁文件」：包数量增长后 install 时间与 lockfile 冲突频率指数上升，pnpm workspace + 强制 catalog 统一版本是第一道治理。
- 其次是「构建图失真」：包间隐式依赖（没声明但 import 了）让增量构建缓存失效——强制显式声明 + CI 依赖图校验（循环依赖报错）。
- 第三是「所有权模糊」：谁都能改任何包 → 质量塌陷；CODEOWNERS 按目录绑定审批 + 包级变更影响面自动评审（改了 A 包自动找 A 的消费方 owner）。
- 最后是「CI 排队」：全量 pipeline 太长，按 affected graph 触发是唯一出路（Turborepo/Nx 远程缓存）。
- 追问钩子：为什么 catalog（统一版本表）比各包自定版本好——跨包同依赖不同版本是「幽灵双包」根源（instanceof 失败/重复打包）；catalog 把版本决策集中到一处，升级变一次 PR。

```yaml
# pnpm-workspace.yaml —— catalog 统一版本治理
packages: ['packages/*', 'apps/*']
catalog:
  react: ^19.0.0
  typescript: ^5.6.0
  vite: ^6.0.0
# package.json 引用: "react": "catalog:" —— 版本单源，升级一处生效
```
```jsonc
// turbo.json —— affected 构建图
{ "tasks": {
    "build": { "dependsOn": ["^build"], "outputs": ["dist/**"] },
    "test": { "dependsOn": ["build"] } } }
// CI: turbo run build test --filter=...[origin/main]  只构建受影响的包
```
