---
title: [1178] 多轮会话里，检索上下文（已检索过的）怎么管理
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 会话]
type: 面试题
---

## 1178：多轮会话里，检索上下文（已检索过的）怎么管理

**答**：
- 会话检索状态三件：已检 query 集（避免重复检索同义 query）、已用证据集（引用过的 chunk，跨轮一致性）、证据有效期（轮次推进后旧证据可能失效）。
- 复用策略：新 query 与已检 query 相似度高时直接复用检索结果（省时省钱），只在「语义新增」时触发新检索；但用户明确要求「再搜」时跳过复用。
- 跨轮一致：同一会话里同一事实的答案应一致——证据集共享 + 新证据与旧证据冲突时提示「信息已更新」，不悄悄翻供。
- 追问钩子：会话级状态和全局缓存冲突吗？——会话级按会话隔离（防串味），全局缓存按 query 归一共享；层级分明后不冲突：全局缓存管「首次检索」，会话状态管「复用与一致性」。

```ts
class SessionRetrieval {
  seen = new Map();     // normQuery -> hits
  used = new Set();     // 已引用 chunk
  async search(q, { force = false } = {}) {
    const norm = normalize(q);
    if (!force && this.seen.has(norm) && similar(this.seen, q) > 0.92) {
      return this.seen.get(norm);               // 复用已检结果
    }
    const hits = await pipeline(q);
    const conflicts = conflictWith(this.used, hits);
    if (conflicts.length) return { hits, note: '与此前信息存在更新' }; // 透明提示
    this.seen.set(norm, hits);
    return { hits };
  }
}
```
