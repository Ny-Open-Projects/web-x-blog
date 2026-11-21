---
title: [RBL-156] Nx 的任务图与缓存机制，和 Turborepo 怎么选
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-156：Nx 的任务图与缓存机制，和 Turborepo 怎么选

**答**：
- 共同内核思想：都做"任务级 hash → 缓存 → 跳过"，Nx 叫 computation caching，Turborepo 叫 remote caching；两者都支持分布式缓存与依赖图调度。
- Nx 差异点：任务图更完整（nx graph 可视化、task pipeline 用 targetDefaults 配置）、插件体系覆盖框架级生成器（nx generate）、支持 distributed task execution（多台 CI 机器分片同一 pipeline）；Turborepo 更轻、配置更少、与 Vercel 集成深。
- 选型经验：5 个包以内的中小 monorepo 用 Turborepo 成本最低；包数多、有代码生成器需求、需要 CI 分片编排的大型仓库选 Nx。
- 两者的缓存 key 都强调"显式声明输入"：Nx 用 namedInputs（production 默认排除 test 文件），Turborepo 用 inputs glob——漏声明是产物陈旧的第一事故源。
- 追问钩子：Rust 系构建工具（Rspack/Rolldown）与任务编排器是正交的——一个管单包构建快，一个管多包不重复构建，真实方案常是 Nx/Turbo + Rspack 组合。

```json
// nx.json 核心：namedInputs 定义"什么变化才算输入变了"
{
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": ["default", "!{projectRoot}/**/*.spec.*", "!{projectRoot}/tsconfig.spec.json"],
    "sharedGlobals": ["{workspaceRoot}/pnpm-lock.yaml", "{workspaceRoot}/.nvmrc"]
  },
  "targetDefaults": {
    "build": { "dependsOn": ["^build"], "inputs": ["production", "^production"],
               "cache": true, "outputs": ["{projectRoot}/dist"] }
  }
}
```
