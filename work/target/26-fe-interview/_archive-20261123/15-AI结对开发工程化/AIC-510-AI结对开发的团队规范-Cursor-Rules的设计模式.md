---
title: [AIC-510] Cursor Rules 的设计模式
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-510：Cursor Rules 的设计模式

**答**:
- Cursor Rules 的分层设计：1) **全局规则**（`.cursorrules` 或 `.cursor/rules/`——项目级编码规范："TypeScript strict"、"React 函数组件"、"不用 any"——所有 AI 交互共享）；2) **目录级规则**（`.cursor/rules/auth.md`——特定目录的约束："auth 目录的文件必须使用 JWT 而非 session cookie"——只在 auth/ 下生效）；3) **文件级规则**（文件头部注释 `// @ai-rule: 不修改此文件——生成代码放新文件`——文件级指令；规则的继承与覆盖（全局 → 目录级 → 文件级，逐级覆盖）。
- Rules 的内容模式：1) **约束型**（"不要用 any"、"必须用 zod 校验"——禁止性规则）；2) **偏好型**（"prefer function components"、"use drizzle over prisma"——偏好性规则）；3) **架构型**（"数据获取只在 server components"——架构级约束）；4) **模板型**（"新 API route 必须包含 error handler 和 zod 验证"——脚手架规则）；规则的语言 = 自然语言（LLM 可理解）——「规则的精确性」= AI 遵守度。
- 追问钩子：为什么「目录级规则」比「全局规则」更有效？——全局规则 = 一刀切（"用 server components" 对 client 组件文件不适用）；目录级 = 上下文精确（auth 目录的 JWT 规则只在 auth 下生效——不会污染其他目录）；「规则的上下文匹配」：Cursor 的 rules 加载机制 = 当前文件的目录匹配相关 rules——只注入相关的 rules（token 节省 + 遵守度提高）——与 RBL-502 的上下文裁剪同构（规则也是上下文的一部分）。

```markdown
<!-- .cursor/rules/global.md -->
- Use TypeScript strict mode (no `any`)
- Prefer function components with hooks
- Use zod for input validation
- Data fetching only in server components or route handlers

<!-- .cursor/rules/auth.md --- globs: src/auth/** -->
- Auth directory must use JWT tokens (not session cookies)
- All auth endpoints must have rate limiting
- Never store plain-text passwords

<!-- .cursor/rules/api.md --- globs: app/api/** -->
- New API routes must include:
  1. zod input validation
  2. try-catch with proper status codes
  3. Rate limiting middleware
  4. Return type annotations

<!-- File-level: 在需要保护的文件头 -->
// @ai-rule: DO NOT modify this file. Generate new files instead.
// This file contains battle-tested logic.
```
