---
title: [AGT-009] 如何让模型稳定输出 JSON？JSON mode 的正确用法是什么？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-009：如何让模型稳定输出 JSON？JSON mode 的正确用法是什么？
**答**：
- 请求加 `response_format: { type: 'json_object' }` 强制输出合法 JSON（OpenAI 兼容接口普遍支持，更强的是 `json_schema` 约束）。
- 开了 JSON mode 仍需在提示词里描述字段名、类型和"不要输出多余内容"，否则字段不可控。
- 解析前不要假设成功：用 `JSON.parse` 包 try 或先做 schema 校验（见 AGT-012）。
- 抽取、分类、路由等机器消费的场景一律走结构化输出，不要解析自由文本。

```typescript
// JSON mode：response_format 保证语法合法，提示词负责保证语义正确
async function extractMeta(text: string): Promise<{ title: string; tags: string[] }> {
  const res = await fetch(`${OPENAI_BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini',
      response_format: { type: 'json_object' },
      messages: [
        {
          role: 'system',
          content: '从用户输入中抽取信息，输出 JSON，字段：title（字符串）、tags（字符串数组）。不要输出 JSON 以外的任何内容。',
        },
        { role: 'user', content: text },
      ],
    }),
  });
  const data = await res.json();
  return JSON.parse(data.choices[0].message.content);
}
```
