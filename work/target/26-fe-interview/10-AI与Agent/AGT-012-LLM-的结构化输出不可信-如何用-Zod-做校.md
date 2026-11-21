---
title: [AGT-012] LLM 的结构化输出不可信，如何用 Zod 做校验与自动修复？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-012：LLM 的结构化输出不可信，如何用 Zod 做校验与自动修复？
**答**：
- LLM 输出是"建议"不是"契约"：字段缺失、类型漂移、包一层 markdown 代码块都常见，必须运行时校验。
- 用 Zod 定义 schema，`safeParse` 校验失败后把错误信息回喂给模型重试一次，多数能自愈。
- 校验两次仍失败要抛错降级，绝不能把脏数据往下传。
- OpenAI 的 Structured Outputs（`json_schema` + `strict: true`）可从生成侧约束，但运行时校验仍应保留。

```typescript
import { z } from 'zod';

const PaperSchema = z.object({
  title: z.string().min(1),
  year: z.number().int(),
  authors: z.array(z.string()),
});

export type Paper = z.infer<typeof PaperSchema>;

function safeJsonParse(s: string): unknown {
  const match = s.match(/\{[\s\S]*\}/); // 容错：剥掉可能的 markdown 包裹
  return JSON.parse(match ? match[0] : s);
}

// 校验失败时把 Zod 错误回喂给模型，自动修复一次
export async function extractPaper(text: string): Promise<Paper> {
  const raw = await llmComplete(`从下文抽取论文信息，输出 JSON：${text}`);
  const first = PaperSchema.safeParse(safeJsonParse(raw));
  if (first.success) return first.data;

  const fixed = await llmComplete([
    '你上次的输出未通过校验，请修正后只输出 JSON。',
    `校验错误：${first.error.issues.map((i) => `${i.path.join('.')}: ${i.message}`).join('; ')}`,
    `上次输出：${raw}`,
  ].join('\n'));
  const retried = PaperSchema.safeParse(safeJsonParse(fixed));
  if (!retried.success) throw new Error('结构化输出两次校验失败');
  return retried.data;
}
```

---

## 三、Function Calling 与 Tool Use
