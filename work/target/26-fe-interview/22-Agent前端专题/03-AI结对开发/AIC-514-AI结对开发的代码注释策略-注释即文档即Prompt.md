---
title: [AIC-514] AI 代码注释策略：注释即 Prompt
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-514：注释即 Prompt

**答**:
- 注释的双重角色：1) **人读的文档**（传统注释——解释代码意图 RBL-590）；2) **AI 读的 Prompt**（AI 用注释作为上下文——注释影响 AI 的后续生成（Cursor/Copilot 读取光标前的注释作为生成依据）；「注释即 Prompt」= 写注释就是在指导 AI。
- AI 友好的注释模式：1) **意图注释**（`// TODO: 这里需要校验用户权限`——AI 看到会生成权限校验代码）；2) **约束注释**（`// IMPORTANT: 不要在这里使用 setState（性能问题）`——AI 避免反模式）；3) **接口注释**（JSDoc 的 @param/@returns——AI 理解函数契约（TypeScript 类型 + JSDoc = 双重约束）；4) **跳过注释**（`// @ai-skip`——AI 不应该修改此区域。
- 追问钩子：为什么「注释即 Prompt」是 AI 结对中最被低估的技巧？——大多数开发者把注释当文档（给人看的）；但在 AI 结对中，注释是「光标前最近的上下文」（AI 的补全质量与光标前的注释质量正相关——注释越精确 AI 生成越准）；「注释的策略性使用」：在需要 AI 生成代码的位置写精确注释 → AI 补全质量提升——这是零成本的 Prompt 工程（不需要打开 Chat——直接在代码中写注释）。

```typescript
// AI 友好的注释示例
// ✅ 意图注释（AI 读取后生成正确代码）
// Validate the request body against the schema and return 422 on failure
function validateRequest(body: unknown) {
  // AI 会生成 zod 校验代码
}

// ❌ 无用注释（AI 无法从中获益）
// This function validates
function validateRequest(body: unknown) { }

// ✅ 约束注释（AI 避免反模式）
// IMPORTANT: This component is server-rendered.
// Do NOT use useState, useEffect, or browser APIs here.
export default async function ServerPage() { }

// ✅ 接口注释（JSDoc = AI 的类型约束）
/**
 * Fetch products with pagination.
 * @param cursor - Opaque cursor from previous response
 * @returns Items for this page and cursor for next page
 * @throws {RateLimitError} When exceeding 10 req/min
 */
async function fetchProducts(cursor?: string): Promise<{ items: Product[]; nextCursor?: string }> { }
```
