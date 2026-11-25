---
title: [R19-221] Server Action 怎么测试？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-221：Server Action 怎么测试？
**答**：
- 单测：action 的核心逻辑抽成纯函数（validate/createOrder），直接 vitest 覆盖；action 本身做薄壳（鉴权 + 参数提取 + 调用核心）。
- 集成：Next 的 test 环境里直接调用 action 函数（mock request 上下文/cookies），断言返回结构与 DB 状态（内存 DB）。
- 端到端：Playwright 提交表单 → 断言跳转与数据落库（含无 JS 模式 `javaScriptEnabled: false` 验证渐进增强）。
- mock 边界：cookies/headers 在测试中用框架提供的 mock 工具（next/headers mock）。
- 关键回归点：权限拒绝路径、幂等重复提交、校验错误回显。
