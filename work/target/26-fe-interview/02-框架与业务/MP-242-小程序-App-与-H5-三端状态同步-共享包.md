---
title: [MP-242] 小程序/App/H5 三端状态与业务逻辑同步怎么组织？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-242：三端业务逻辑同步？
**答**：
- 单仓三端（Taro/uni-app）：core 包（纯逻辑：API 层/校验/状态 store/工具）零框架依赖，三端薄适配（存储 API、网络 API、路由 API）。
- 接口层统一：同一后端 API + 同一 DTO 定义（zod schema 共享）——三端行为一致。
- 差异收敛层：platform adapter（storage/request/login）注入到 core，core 不感知端。
- 测试：core 单测三端共用；端适配层集成测试各端跑。
- 版本节奏：core 与三端业务同步发版（monorepo changesets）。
