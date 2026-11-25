---
title: [MFW-256] 元框架环境变量三层模型
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-256：环境变量三层模型

**答**:
- 三层：构建期内联（NEXT_PUBLIC_* / VITE_*——进产物，泄露即公开）、服务端运行时（process.env @ — server-only）、部署模板注入（__CONFIG__ 外置——一套产物多环境 MFW-397）
- 泄漏审计：NEXT_PUBLIC 前缀即公开契约——扫描产物确认「以为 server-only 实则被打进 client 的值」（grep 构建）
- 类型安全：env schema 校验（t3-env 类）启动 fail-fast（缺失/类型错直接崩——配置错误早暴露）
- 轮换面：构建期内联的值变更必重构建——易变配置走运行时层（划分标准：变更频率 × 敏感度二维表）

```javascript
// t3-env 启动校验
const serverEnv = createEnv({
  server: { DATABASE_URL: z.string().url(), API_KEY: z.string().min(10) },
  client: { NEXT_PUBLIC_API_URL: z.string().url() },
  runtimeEnv: process.env,
  skipValidation: process.env.SKIP_ENV_CHECK === '1',   // 仅测试跳过
})
// 审计：grep NEXT_PUBLIC dist/ | 核对白名单
```
