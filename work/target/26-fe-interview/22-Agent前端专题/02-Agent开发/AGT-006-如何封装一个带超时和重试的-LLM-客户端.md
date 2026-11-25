---
title: [AGT-006] 如何封装一个带超时和重试的 LLM 客户端？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-006：如何封装一个带超时和重试的 LLM 客户端？
**答**：
- 超时用 `AbortController` + `setTimeout` 实现，LLM 接口慢是常态，裸 fetch 会挂死请求。
- 只重试可恢复错误：429 限流与 5xx；4xx 参数错误重试没有意义。
- 429 优先读 `Retry-After` 响应头，否则用指数退避（2^n 秒）加抖动，避免重试风暴。
- 重试次数有限（一般 3 次），最终失败要把错误抛给上层做用户可见的降级。

```typescript
// 超时 + 指数退避重试的 LLM 客户端
async function chatWithRetry(
  messages: ChatMessage[],
  { retries = 3, timeoutMs = 30_000 }: { retries?: number; timeoutMs?: number } = {},
): Promise<string> {
  let lastError: unknown;
  for (let attempt = 1; attempt <= retries; attempt++) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const res = await fetch(`${OPENAI_BASE_URL}/chat/completions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        },
        body: JSON.stringify({ model: 'gpt-4o-mini', messages }),
        signal: controller.signal,
      });
      // 429 与 5xx 可重试，其余状态码直接抛出
      if ((res.status === 429 || res.status >= 500) && attempt < retries) {
        const retryAfter = Number(res.headers.get('retry-after')) * 1000;
        await new Promise((r) => setTimeout(r, retryAfter || 2 ** attempt * 1000));
        continue;
      }
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      return data.choices[0].message.content as string;
    } catch (err) {
      lastError = err;
    } finally {
      clearTimeout(timer);
    }
  }
  throw lastError;
}
```
