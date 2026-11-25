---
title: [RBL-341] Turborepo 边界场景：环境变量与动态内容
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-341：Turborepo 边界场景：环境变量与动态内容

**答**:
- 环境变量三大坑：全局 env（不进指纹 → 缓存命中但产物含旧 env）、构建期生成的动态内容（时间戳/随机 id → 同输入不同输出，缓存校验必失败）、API_URL 类部署变量（应留给运行时而非构建期）
- 治理：env 全部显式声明（globalDependencies/turbo env 声明）、构建产物禁动态内容（指纹纳入）、部署变量运行时注入（SRI/DefinePlugin 只管构建期）
- 幽灵场景：`date` 命令进产物（banner）→ 每次构建产物必变 → 缓存永不命中——build 里禁 date/random
- 验证：同输入双跑产物 diff（应 byte 相同）——动态内容检测器

```json
{ "globalEnv": ["NODE_ENV"], "tasks": { "build": { "env": ["API_URL_BUILD_TIME"] } } }
// 双跑验证：turbo build --force && diff 两次产物 → 应一致
```
