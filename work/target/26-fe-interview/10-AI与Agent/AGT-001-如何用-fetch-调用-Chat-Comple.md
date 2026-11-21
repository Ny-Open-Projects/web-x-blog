---
title: [AGT-001] 如何用 fetch 调用 Chat Completions API 完成一次完整对话？为什么前端不能直接持有 API Key？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-001：如何用 fetch 调用 Chat Completions API 完成一次完整对话？为什么前端不能直接持有 API Key？
**答**：
- 请求体核心是 `model` 与 `messages` 数组，`messages` 按顺序携带全部历史，模型本身无状态。
- 响应在 `choices[0].message.content`，同时返回 `usage` 可用于成本统计。
- 前端绝不放 Key：Key 写在前端等于公开，任何人可以刷你的额度，必须走后端代理转发。
- 生产上要检查 `res.ok`，4xx 是请求问题、429 是限流、5xx 才考虑重试。

```typescript
// server/api/chat.ts —— Key 只存在于服务端环境变量，前端请求走后端代理
const OPENAI_BASE_URL = process.env.OPENAI_BASE_URL ?? 'https://api.openai.com/v1';

interface ChatMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export async function chat(messages: ChatMessage[]): Promise<string> {
  const res = await fetch(`${OPENAI_BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini',
      messages,
      temperature: 0.7,
    }),
  });
  if (!res.ok) {
    throw new Error(`LLM 调用失败：${res.status} ${await res.text()}`);
  }
  const data = await res.json();
  return data.choices[0].message.content as string;
}

const reply = await chat([
  { role: 'system', content: '你是一个简洁的前端技术助手' },
  { role: 'user', content: '什么是事件循环' },
]);
```
