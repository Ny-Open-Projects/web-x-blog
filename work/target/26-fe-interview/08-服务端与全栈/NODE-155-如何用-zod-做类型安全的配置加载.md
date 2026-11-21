---
title: [NODE-155] 如何用 zod 做类型安全的配置加载？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-155：如何用 zod 做类型安全的配置加载？
**答**：
- 痛点：`process.env.X` 全是 string | undefined，散落读取 = 运行时才炸；zod 让**启动即校验 + 全程类型推导**。
- 模式：一份 schema 描述全部环境变量 → `parse` 失败 fail fast（绝不带病启动）→ 导出强类型 env 对象，唯一入口。
- 常用技巧：`z.coerce.number()` 处理字符串数字、`default` 给可选项、`refine` 做跨字段约束（如 prod 必填某密钥）。
- 配置中心联动：远端配置热更时同样先过 schema（NODE-150），非法配置拒绝生效。

```typescript
import { z } from 'zod';

const Env = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().int().min(1024).default(3000), // 字符串环境变量 → 数字
  DATABASE_URL: z.string().url(),
  REDIS_URL: z.string().url(),
  JWT_PUBLIC_KEY: z.string().min(100),
  LOG_LEVEL: z.enum(['fatal', 'error', 'warn', 'info', 'debug']).default('info'),
}).refine((e) => e.NODE_ENV !== 'production' || e.JWT_PUBLIC_KEY.length > 100, {
  message: '生产环境必须配置 JWT_PUBLIC_KEY',
});

// 启动即校验：缺配置直接崩，CI 阶段也能提前发现
export const env = Env.parse(process.env);
env.PORT; // 类型：number，全程推导
// 铁律：新增配置必须先改 schema；禁止业务代码直接读 process.env.X
```
