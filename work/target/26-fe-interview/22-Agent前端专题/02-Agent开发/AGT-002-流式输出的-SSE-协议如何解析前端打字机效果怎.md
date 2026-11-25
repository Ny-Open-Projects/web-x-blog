---
title: [AGT-002] 流式输出的 SSE 协议如何解析？前端打字机效果怎么落地？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-002：流式输出的 SSE 协议如何解析？前端打字机效果怎么落地？
**答**：
- 请求带 `stream: true`，响应体是 `text/event-stream`，用 `ReadableStream` 逐块读取。
- SSE 按 `data:` 前缀逐行传 JSON 增量，`choices[0].delta.content` 是本次新增文本，`[DONE]` 表示结束。
- TCP 分包与 SSE 分行不对齐：必须用 buffer 缓存不完整行，等下一块拼齐再解析。
- 前端把每个 delta 追加到末尾消息即可得到打字机效果；`decoder.decode(value, { stream: true })` 避免中文多字节被截断出乱码。

```typescript
// 逐块解析流式响应，把每个增量回调给渲染层
export async function streamChat(
  messages: ChatMessage[],
  onDelta: (text: string) => void,
): Promise<void> {
  const res = await fetch(`${OPENAI_BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
    },
    body: JSON.stringify({ model: 'gpt-4o-mini', messages, stream: true }),
  });
  const reader = res.body!.getReader();
  const decoder = new TextDecoder();
  let buffer = '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });

    // SSE 按行组织，最后一段可能不完整，留到下一轮拼接
    const lines = buffer.split('\n');
    buffer = lines.pop() ?? '';
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed.startsWith('data:')) continue;
      const payload = trimmed.slice(5).trim();
      if (payload === '[DONE]') return;
      const delta = JSON.parse(payload).choices[0]?.delta?.content;
      if (delta) onDelta(delta);
    }
  }
}
```
