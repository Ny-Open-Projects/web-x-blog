---
title: [NODE-078] 设计一个 AI 代理网关（统一 LLM 接入、流式转发、计费）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-078：设计一个 AI 代理网关（统一 LLM 接入、流式转发、计费）？
**答**：
- 需求：前端只对接网关一个地址，网关屏蔽 OpenAI/Anthropic/国产模型的协议差异（统一 messages 格式与 SSE 事件）、做 **API Key 管理、限流、token 计费、流式转发**。
- 流式转发核心：上游 LLM 返回 **SSE 流**，网关用流透传（`res.write(chunk)` 逐块转发），同时旁路解析 `usage` 事件做计费——**不能把整个响应 buffer 完再回**（用户要打字机效果）。
- 关键点：鉴权（网关签发的 key 而非各厂商 key）、按 key 限流与配额（Redis 计数）、超时与重试（流中断后重试需从断点续传或报错）、敏感词过滤（流式检测）、成本观测（每请求 tokens/耗时/模型）。

```javascript
const MODEL_CONFIG = {
  'gpt-4o':      { upstream: 'https://api.openai.com/v1/chat/completions',    pricePer1k: 0.03 },
  'glm-4':       { upstream: 'https://open.bigmodel.cn/api/paas/v4/chat/completions', pricePer1k: 0.01 },
};

// 流式 AI 代理：SSE 透传 + 计费
router.post('/ai/chat', async (ctx) => {
  const apiKey = ctx.get('x-api-key');
  const quota = await getQuota(apiKey);                        // Redis：余额与限流
  if (quota.remainingTokens <= 0) ctx.throw(429, '配额不足');

  const { model, messages, stream = true } = ctx.request.body;
  const conf = MODEL_CONFIG[model];
  if (!conf) ctx.throw(400, '不支持的模型');

  // 上游请求：SSE 流
  const upstream = await fetch(conf.upstream, {
    method: 'POST',
    headers: { authorization: `Bearer ${process.env[`${model}_KEY`]}`, 'content-type': 'application/json' },
    body: JSON.stringify({ model, messages, stream }),
  });
  if (!upstream.ok) ctx.throw(502, `upstream ${upstream.status}`);

  ctx.set({ 'content-type': 'text/event-stream', 'cache-control': 'no-cache', connection: 'keep-alive' });
  ctx.status = 200;

  const reader = upstream.body.getReader();
  const decoder = new TextDecoder();
  let usage = { prompt_tokens: 0, completion_tokens: 0 };
  const start = Date.now();

  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      const text = decoder.decode(value, { stream: true });
      ctx.res.write(text);                                     // 原样转发 SSE chunk
      // 旁路解析 usage（流式最后一个 chunk 携带）
      for (const line of text.split('\n')) {
        if (line.startsWith('data: ') && line.includes('usage')) {
          try { usage = JSON.parse(line.slice(6)).usage ?? usage; } catch {}
        }
      }
    }
  } finally {
    ctx.res.end();
    // 计费：按实际 token 扣减 + 记账（异步不阻塞响应）
    const cost = ((usage.prompt_tokens + usage.completion_tokens) / 1000) * conf.pricePer1k;
    await Promise.allSettled([
      redis.decrby(`quota:${apiKey}`, usage.prompt_tokens + usage.completion_tokens),
      db.query('INSERT INTO ai_usage (api_key, model, tokens, cost, duration) VALUES (?, ?, ?, ?, ?)',
        [apiKey, model, usage.prompt_tokens + usage.completion_tokens, cost, Date.now() - start]),
    ]);
  }
});
```
