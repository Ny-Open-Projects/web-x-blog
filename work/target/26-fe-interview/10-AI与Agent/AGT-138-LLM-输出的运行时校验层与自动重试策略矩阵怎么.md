---
title: [AGT-138] LLM 输出的运行时校验层与自动重试策略矩阵怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-138：LLM 输出的运行时校验层与自动重试策略矩阵怎么设计？
**答**：
- 校验层位置：每次模型输出先过 Zod schema，再过业务规则（引用是否存在、金额是否越界）——schema 是格式关，业务规则是语义关，两关都过才进下游。
- 重试策略矩阵（按失败类型分派，而不是无脑重试 3 次）：JSON 解析失败 → 带错误信息重试并附上坏输出；schema 字段缺失 → 追加「字段 X 缺失」的修正提示；语义校验失败 → 换 prompt 策略（加 few-shot）而不是简单重试；连续失败 → 降级模型或走人工。
- 重试要有界且带退避，并把每次失败写入 trace——重试矩阵本身是可观测对象。
- 高频考点：把「校验错误 + 原输出」回喂给模型做定向修复（self-heal），成功率远高于原样重发。

```typescript
// 输出校验 + 按失败类型分派的重试矩阵
import { z } from 'zod';

type Repair = (attempt: number, error: string, badOutput: string) => string; // 返回追加给模型的修正提示

export class OutputGate<T> {
  private attempts: { pass: 0 | 1 | 2 | 3; repair: Repair }[] = [
    { pass: 0, repair: (_a, err, bad) => `你上次的输出未通过校验：${err}\n错误原文：${bad.slice(0, 300)}\n请严格按 schema 重新输出，不要解释。` },
    { pass: 1, repair: () => '再次失败。以下是符合格式的示例，照此结构输出：\n{"answer": "...", "citations": [1]}' },
    { pass: 2, repair: () => '最后一次机会：只输出 JSON，禁止 markdown 代码块与任何额外文字。' },
  ];

  constructor(private schema: z.ZodType<T>, private business?: (v: T) => string | null) {}

  async validate(raw: string): Promise<{ ok: true; value: T } | { ok: false; error: string; stage: 'json' | 'schema' | 'business' }> {
    let json: unknown;
    try { json = JSON.parse(raw.replace(/^```(?:json)?|```$/g, '').trim()); }
    catch { return { ok: false, error: 'JSON 解析失败', stage: 'json' }; }
    const parsed = this.schema.safeParse(json);
    if (!parsed.success) return { ok: false, error: parsed.error.issues.map((i) => `${i.path.join('.')}: ${i.message}`).join('; '), stage: 'schema' };
    const biz = this.business?.(parsed.data) ?? null;
    if (biz) return { ok: false, error: biz, stage: 'business' };
    return { ok: true, value: parsed.data };
  }

  async runWithRetry(call: (extraHint: string) => Promise<string>): Promise<T> {
    let hint = '';
    for (let i = 0; i <= this.attempts.length; i++) {
      const raw = await call(hint);
      const result = this.validate(raw);
      if (result.ok) return result.value;
      if (i === this.attempts.length) throw new Error(`校验重试耗尽：${result.error}`); // 之后走降级/人工
      hint = this.attempts[i].repair(i, result.error, raw);
    }
    throw new Error('unreachable');
  }
}

// 用法：字段缺失修提示、语义失败换策略
const gate = new OutputGate(
  z.object({ answer: z.string(), citations: z.array(z.number()) }),
  (v) => v.citations.some((c) => c < 1 || c > 10) ? '引用编号超出候选范围' : null,
);
```
