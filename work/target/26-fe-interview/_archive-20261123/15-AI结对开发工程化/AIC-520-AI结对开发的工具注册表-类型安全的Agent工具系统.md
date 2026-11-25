---
title: [AIC-520] Agent 工具注册表：类型安全的工具系统
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-520：Agent 工具注册表

**答**:
- Agent 工具系统的设计：1) **工具注册表**（每个工具 = { name, description, execute, schema }——schema 定义输入/输出类型（LLM 需要知道工具的签名才能调用）；2) **类型安全**（工具的 schema = zod schema——LLM 的 tool call 参数被 schema 校验（幻觉参数被拦截 RBL-507）；3) **工具的分类**：read（读文件/搜索代码——无副作用）/write（写文件/创建文件——有副作用）/execute（运行命令/测试——有副作用且耗时）；4) **权限分级**：read 工具 Agent 可自主调用；write 工具需要确认或日志；execute 工具需要 sandbox（RBL-519 的工具版）。
- 追问钩子：为什么「工具的 schema」是 Agent 可靠性的基石？——LLM 的 tool call = JSON 输出（LLM 可能生成错误的参数类型/缺失参数/幻觉参数名）；schema 校验 = 参数的运行时验证（zod.parse(args)——无效参数被拦截并返回错误给 LLM 让它重试）；「schema = LLM 与工具的接口契约」——没有 schema 的工具调用 = 信任 LLM 的 JSON 输出（幻觉参数直接执行 = 危险）——schema 是 Agent 工具系统的安全网。

```typescript
// 工具注册表（类型安全）
import { z } from 'zod';
interface Tool<S extends z.ZodSchema, R = unknown> {
  name: string;
  description: string;
  schema: S;
  permission: 'read' | 'write' | 'execute';
  execute: (args: z.infer<S>) => Promise<R>;
}
const tools: Tool<z.ZodSchema>[] = [
  {
    name: 'read-file', description: 'Read file contents',
    schema: z.object({ path: z.string() }),
    permission: 'read',
    execute: async ({ path }) => fs.readFileSync(path, 'utf-8'),
  },
  {
    name: 'write-file', description: 'Write file contents',
    schema: z.object({ path: z.string(), content: z.string() }),
    permission: 'write',
    execute: async ({ path, content }) => fs.writeFileSync(path, content),
  },
  {
    name: 'run-tests', description: 'Run test suite',
    schema: z.object({ pattern: z.string().optional() }),
    permission: 'execute',
    execute: async ({ pattern }) => execSync(`pnpm test ${pattern ?? ''}`).toString(),
  },
];
// Agent 的工具调用（schema 校验）
async function executeTool(name: string, args: unknown, registry: Tool<z.ZodSchema>[]) {
  const tool = registry.find(t => t.name === name);
  if (!tool) throw new Error(`Unknown tool: ${name}`);
  const parsed = tool.schema.safeParse(args);           // schema 校验
  if (!parsed.success)
    throw new Error(`Invalid args for ${name}: ${parsed.error.message}`);
  return await tool.execute(parsed.data);               // 校验后执行
}
```
