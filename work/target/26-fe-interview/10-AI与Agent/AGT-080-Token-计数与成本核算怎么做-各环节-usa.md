---
title: [AGT-080] Token 计数与成本核算怎么做（各环节 usage 统计上报）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-080：Token 计数与成本核算怎么做（各环节 usage 统计上报）？
**答**：
- 每个环节上报 usage：LLM 返回的 `prompt_tokens`/`completion_tokens` 是权威值；流式场景在最后一个 chunk 取（部分厂商需 `stream_options.include_usage`），没有就本地估算兜底。
- 单价表驱动核算：模型 × 输入/输出单价（注意缓存折扣），落到 request 级再聚合出用户/会话/功能维度账单。
- 计数与计费解耦：计数服务只管准确记录，计费规则变化不改业务代码。
- 本地估算（约字符数/4）用于预算预检与限流，结算以服务端 usage 为准。

```typescript
import { z } from 'zod';

// 成本核算：单价表 + usage 落库
const PRICE: Record<string, { input: number; output: number }> = {
  // 单位：美元 / 百万 token
  'gpt-4o': { input: 2.5, output: 10 },
  'gpt-4o-mini': { input: 0.15, output: 0.6 },
};

interface UsageRecord {
  requestId: string; userId: string; model: string;
  promptTokens: number; completionTokens: number; costUsd: number;
}

export function billUsage(u: Omit<UsageRecord, 'costUsd'>): UsageRecord {
  const p = PRICE[u.model] ?? { input: 10, output: 30 }; // 未知模型按最贵计，防漏计
  const costUsd = (u.promptTokens * p.input + u.completionTokens * p.output) / 1_000_000;
  const record = { ...u, costUsd: Number(costUsd.toFixed(6)) };
  db.insert('usage_records', record);                    // 异步落库，按维度聚合出账单
  return record;
}

// 从流式响应提取 usage：OpenAI 兼容接口最后一个 chunk 携带
export function extractStreamUsage(events: SSEEvent[]) {
  for (let i = events.length - 1; i >= 0; i--) {
    if (events[i].data === '[DONE]') continue;
    const usage = JSON.parse(events[i].data)?.usage;
    if (usage) return { promptTokens: usage.prompt_tokens, completionTokens: usage.completion_tokens };
  }
  return null; // 上游不回 usage 时以本地估算兜底
}

export const estimateTokens = (text: string) => Math.ceil(text.length / 4);
```
