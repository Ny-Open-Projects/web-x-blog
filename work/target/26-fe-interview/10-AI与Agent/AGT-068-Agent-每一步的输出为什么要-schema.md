---
title: [AGT-068] Agent 每一步的输出为什么要 schema 化？协议如何设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-068：Agent 每一步的输出为什么要 schema 化？协议如何设计？
**答**：
- 每步产出 schema 化（think/act/final 三类）：执行器不靠正则猜格式，UI 能把每步渲染成结构化卡片（思考/工具调用/结论分区）。
- 结构化协议让 trace、评测、回放成为可能：每步是数据而非一段自由文本。
- 用 discriminatedUnion 按 type 分派，字段校验交给 Zod（复用 AGT-048 的修复重试）。
- final 也要 schema：正文 + 置信度（可加引用），前端与下游系统才有稳定契约。

```typescript
import { z } from 'zod';

// Agent 每步输出的统一协议
const StepSchema = z.discriminatedUnion('type', [
  z.object({ type: z.literal('think'), thought: z.string() }),
  z.object({
    type: z.literal('act'),                       // 调用工具
    thought: z.string(),
    tool: z.string(),
    args: z.record(z.unknown()),
  }),
  z.object({
    type: z.literal('final'),                     // 最终答案
    thought: z.string(),
    answer: z.string(),
    confidence: z.number().min(0).max(1),
  }),
]);
type Step = z.infer<typeof StepSchema>;

async function nextStep(messages: ChatMessage[]): Promise<Step> {
  return structuredLLM(messages, StepSchema, 1);  // 模型输出被 schema 强约束
}

function dispatch(step: Step): Promise<string | null> {
  switch (step.type) {
    case 'act':   return runTool(step.tool, step.args); // 返回工具观察结果
    case 'final': return null;                          // null 表示任务结束
    default:      return Promise.resolve('');           // think 只推进上下文
  }
}
```
