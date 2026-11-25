---
title: [AGT-147] 语义检索缓存（query 相似度命中直接返回）怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-147：语义检索缓存（query 相似度命中直接返回）怎么设计？
**答**：
- 原理：在「结果缓存」之上加一层「语义缓存」——新 query 与已缓存 query 的 embedding 相似度超阈值（如余弦 > 0.95）就复用缓存答案，对 FAQ/客服类场景命中率可观。
- 阈值与召回的双向权衡：阈值高 → 命中少但安全；阈值低 → 答非所问的风险上升。区分场景配阈值，且答案要带时效标签（带价格/库存的答案禁止长缓存）。
- 命中策略分级：完全命中（同 embedding 或同指纹）直接返回；近命中（高相似）返回缓存但附加「相似问题」提示并异步刷新；低相似才真正走 RAG 链路。
- 失效三通道：TTL 过期、知识库版本号变更（缓存 key 绑定知识库版本）、负反馈触发（用户点踩即逐出该条目）。

```typescript
// 语义缓存：分级命中 + 知识库版本绑定 + 负反馈逐出
import OpenAI from 'openai';
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

interface CacheEntry { query: string; embedding: number[]; answer: string; kbVersion: number; expiresAt: number; }

export class SemanticCache {
  private entries: CacheEntry[] = [];
  constructor(private kbVersion: () => number, private cosThreshold = 0.95, private ttlMs = 3600_000) {}

  private async embed(text: string) {
    const r = await openai.embeddings.create({ model: 'text-embedding-3-small', input: text });
    return r.data[0].embedding;
  }
  private cos(a: number[], b: number[]) {
    const dot = a.reduce((s, v, i) => s + v * b[i], 0);
    return dot / (Math.hypot(...a) * Math.hypot(...b));
  }

  async lookup(query: string): Promise<{ hit: 'exact' | 'near' | 'miss'; answer?: string }> {
    const now = Date.now(), v = this.kbVersion();
    const qv = await this.embed(query);
    const best = this.entries
      .filter((e) => e.kbVersion === v && e.expiresAt > now)          // 版本绑定 + TTL 双失效
      .map((e) => ({ e, sim: this.cos(qv, e.embedding) }))
      .sort((a, b) => b.sim - a.sim)[0];
    if (!best) return { hit: 'miss' };
    if (best.sim >= this.cosThreshold) return { hit: 'exact', answer: best.e.answer };
    if (best.sim >= 0.88) return { hit: 'near', answer: best.e.answer }; // 近命中：返回但前端标注「相似问题」
    return { hit: 'miss' };
  }

  async put(query: string, answer: string) {
    this.entries.push({ query, embedding: await this.embed(query), answer,
      kbVersion: this.kbVersion(), expiresAt: Date.now() + this.ttlMs });
  }

  evict(query: string) { // 负反馈触发逐出
    this.entries = this.entries.filter((e) => e.query !== query);
  }
}
```

---

## 二十六、Agent UI 工程深水区
