---
title: [AGT-040] LLM 应用上线要做哪些工程化保障？Key 安全、限流成本、可观测性、LangChain 与自研如何取舍？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-040：LLM 应用上线要做哪些工程化保障？Key 安全、限流成本、可观测性、LangChain 与自研如何取舍？
**答**：
- Key 安全：Key 只存服务端环境变量/密钥管理服务，前端永远走后端代理；日志中脱敏，绝不提交 `.env`。
- 限流与成本：用户级限流（每分钟 N 次）、按对话/用户记账 token 消耗、设置每日预算与超额降级（换小模型或拒答）。
- 可观测性：每个请求打结构化日志（耗时、token、finish_reason、错误），接入 Langfuse / OpenTelemetry 做链路追踪与成本看板。
- 框架取舍：LangChain/LlamaIndex 适合快速验证复杂编排（RAG、多链路），但抽象重、调试难；前端团队自研轻量循环（本文这种）更可控，通常"简单场景自研 + 复杂 RAG 用库"。

```typescript
// 后端代理：Key 只在服务端，限流、成本记账、结构化日志三件套
import { Router } from 'express';

const router = Router();

const RATE_LIMIT = 20; // 每用户每分钟
const userQuota = new Map<string, { count: number; resetAt: number }>();

function checkRate(userId: string): boolean {
  const now = Date.now();
  const q = userQuota.get(userId);
  if (!q || now > q.resetAt) {
    userQuota.set(userId, { count: 1, resetAt: now + 60_000 });
    return true;
  }
  q.count += 1;
  return q.count <= RATE_LIMIT;
}

router.post('/api/chat', async (req, res) => {
  const userId = req.user!.id; // 假设前置了鉴权中间件
  if (!checkRate(userId)) return res.status(429).json({ error: '请求过于频繁' });

  const start = Date.now();
  try {
    const upstream = await chatStreamProxy(req.body.messages); // 内部持有 Key，透传 SSE
    res.setHeader('Content-Type', 'text/event-stream');
    upstream.pipe(res);
    upstream.on('end', () => {
      // 结构化日志：后续接 Langfuse 或 OpenTelemetry 做追踪与成本看板
      console.log(JSON.stringify({
        event: 'chat_completed',
        userId,
        ms: Date.now() - start,
        promptTokens: upstream.usage?.prompt_tokens ?? 0,
      }));
    });
  } catch (err) {
    console.error(JSON.stringify({ event: 'chat_failed', userId, err: String(err) }));
    res.status(502).json({ error: '上游服务异常' });
  }
});
```

> AGT-041 起为进阶篇（80 题）。本篇共享辅助函数集中声明如下，正文各题直接复用（Zod 假定已 `import { z } from 'zod'`）：

```typescript
// 共享辅助函数签名
interface ChatMessage { role: 'system' | 'user' | 'assistant'; content: string }
interface SSEEvent { event?: string; id?: string; data: string; retry?: number }
declare function upStream(body: Record<string, unknown>, signal?: AbortSignal): Promise<Response>; // 服务端发起流式补全，Key 只在服务端
declare function chatOnce(messages: ChatMessage[], model?: string): Promise<string>;               // 非流式单轮补全
declare function structuredLLM<T>(messages: ChatMessage[], schema: z.ZodType<T>, maxRetry?: number): Promise<T>; // AGT-048 实现
declare function embed(text: string): Promise<number[]>;   // 文本向量化
declare function cosine(a: number[], b: number[]): number; // 余弦相似度
declare function countTokens(text: string): number;        // 近似 token 估算
declare function withTimeout<T>(p: Promise<T>, ms: number): Promise<T>;
declare function sleep(ms: number): Promise<void>;
declare function stableHash(s: string): number;
declare function splitByToken(text: string, max: number): string[];
declare const log: { info: (m: unknown) => void; warn: (m: unknown) => void; error: (m: unknown) => void };
```

---

## 十二、流式与传输深水区
