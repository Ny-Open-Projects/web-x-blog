---
title: [AGT-098] SaaS 化的多租户如何做隔离（Key 管理 / 配额 / 数据隔离）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-098：SaaS 化的多租户如何做隔离（Key 管理 / 配额 / 数据隔离）？
**答**：
- 三个层面：凭证隔离（租户自带 Key BYOK 或平台统一 Key 记账）、配额隔离（每租户独立 token 预算与限流）、数据隔离（会话与向量库按租户分命名空间）。
- BYOK 模式：平台只转发不碰计费，但 Key 要 KMS 加密存储、展示脱敏（只露尾 4 位）。
- 数据隔离最易翻车点是向量库：入库写入租户元数据，检索强制带租户过滤，且在网关层统一注入防止遗漏。
- 噪声邻居治理：租户级并发上限与队列隔离，防止单租户大请求挤占共享容量。

```typescript
import { z } from 'zod';

// 租户上下文与隔离
interface Tenant {
  id: string; tier: 'free' | 'pro'; byok?: string;
  quotas: { dailyTokens: number; rpm: number };
}

async function tenantScopedRequest(tenant: Tenant, messages: ChatMessage[]) {
  // 1. 凭证：租户自带 Key（KMS 解密）优先，否则平台 Key + 计费到租户
  const apiKey = tenant.byok ? await kmsDecrypt(tenant.byok) : PLATFORM_KEY;

  // 2. 配额：Redis 原子累加，超预算直接拒绝
  const used = await redis.incrby(
    `quota:${tenant.id}:${new Date().toISOString().slice(0, 10)}`,
    countTokens(messages.map((m) => m.content).join('')),
  );
  if (used > tenant.quotas.dailyTokens) throw new QuotaExceededError(tenant.id);

  // 3. 数据隔离：检索强制带租户过滤
  const results = await vectorStore.search(
    await embed(messages.at(-1)!.content), 5, { filter: { tenantId: tenant.id } },
  );
  const answer = await chatWithKey(apiKey, buildRagMessages(messages, results));
  await db.insert('conversations', { tenantId: tenant.id, messages }); // 落库也带租户字段
  return answer;
}

// Key 展示永远脱敏
export const maskKey = (key: string) => `sk-...${key.slice(-4)}`;
```
