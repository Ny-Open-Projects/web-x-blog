---
title: [AGT-048] 结构化输出如何严格校验？模型输出不符合 schema 怎么自动修复？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-048：结构化输出如何严格校验？模型输出不符合 schema 怎么自动修复？
**答**：
- 三层保障：请求侧 `response_format`/JSON Schema 约束、响应侧 Zod 运行时校验、失败侧自动修复重试——只信第一层会翻车（模型仍可能输出围栏、多余文字）。
- 确定性预修复优先于 LLM 修复：剥 markdown 代码围栏、截取首尾花括号，零成本救回大部分「格式歪了但内容对」的输出。
- 修复重试 = 把「原输出 + 具体校验错误」作为上下文让模型修正；错误信息带字段路径，比笼统「重新输出」收敛快，通常 1-2 次即可。
- 连续失败要快速失败并告警，不要无限重试放大成本与延迟。

```typescript
import { z } from 'zod';

const ResumeSchema = z.object({
  name: z.string(),
  years: z.number(),
  skills: z.array(z.string()).min(1),
});

// 第一层：确定性预修复——剥代码围栏、截取 JSON 主体
const F = '\u0060'.repeat(3);   // 围栏用码点构造，避免源码内出现字面围栏
function extractJson(text: string): string {
  const fenced = text.match(new RegExp(F + '(?:json)?\\s*([\\s\\S]*?)' + F));
  const raw = fenced ? fenced[1] : text;
  const start = raw.search(/[[{]/);
  const end = Math.max(raw.lastIndexOf('}'), raw.lastIndexOf(']'));
  return start >= 0 && end > start ? raw.slice(start, end + 1) : raw;
}

// 第二、三层：schema 校验 + 带错误信息的修复重试
export async function structuredLLM<T>(messages: ChatMessage[], schema: z.ZodType<T>, maxRetry = 2): Promise<T> {
  let convo = [...messages];
  let lastErr = '';
  for (let i = 0; i <= maxRetry; i++) {
    const raw = await chatOnce(convo);
    try {
      const candidate = JSON.parse(extractJson(raw));
      const parsed = schema.safeParse(candidate);
      if (parsed.success) return parsed.data;
      lastErr = parsed.error.issues.map((iss) => `${iss.path.join('.')}: ${iss.message}`).join('; ');
    } catch (e) {
      lastErr = `不是合法 JSON：${String(e)}`;
    }
    // 修复上下文：原输出 + 定位到字段路径的错误
    convo = [...convo,
      { role: 'assistant', content: raw },
      { role: 'user', content: `上面的输出未通过校验：${lastErr}。只输出修正后的 JSON，不要解释。` },
    ];
  }
  throw new Error(`结构化输出连续 ${maxRetry + 1} 次校验失败：${lastErr}`);
}
```
