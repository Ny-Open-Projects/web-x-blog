---
title: [NODE-157] OpenAPI→类型→校验"一条链"如何打通？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-157：OpenAPI→类型→校验"一条链"如何打通？
**答**：
- 单一事实源：**OpenAPI 文档先行**，类型与运行时校验都从它生成——前后端契约、SDK、mock 全部同源。
- 链路：`openapi.yaml` → `openapi-typescript` 生成 TS 类型（编译期）→ `express-openapi-validator`/zod schema 运行时校验请求响应 → 前端 SDK 同源生成。
- 价值闭环：改契约 → 前端类型即时报错（编译期拦截）+ 服务端校验拦截（运行时兜底），契约漂移无处藏身。
- CI 门禁：breaking change 检测（oasdiff），破坏性变更必须升 major 并评审。

```yaml
# openapi.yaml —— 契约先行
openapi: 3.1.0
info: { title: order-api, version: 1.2.0 }
paths:
  /orders/{id}:
    get:
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, pattern: "^[0-9]+$" }
      responses:
        "200":
          content:
            application/json:
              schema:
                type: object
                required: [id, status]
                properties:
                  id: { type: string }
                  status: { type: string, enum: [PENDING, PAID, SHIPPED] }
```

```bash
# 类型与校验同源生成
npx openapi-typescript openapi.yaml -o src/types/api.ts
# 服务端：express-openapi-validator 按同一文档校验请求/响应
# 前端 SDK：openapi-typescript-codegen 生成带类型的 client
# CI 门禁：oasdiff breaking openapi.yaml origin/main/openapi.yaml
```
