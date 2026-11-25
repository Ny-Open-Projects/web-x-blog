---
title: [916] RAG 服务缓存怎么分层设计才不串味
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 缓存]
type: 面试题
---

## 916：RAG 服务缓存怎么分层设计才不串味

**答**：
- 三层：query 归一化缓存（改写后的规范 query → 检索结果）、语义缓存（query 向量近邻命中 → 直接复用答案，阈值 0.95 以上才敢用）、会话内缓存（多轮对话同一主题的检索结果复用）。
- 语义缓存是事故高发区：两个「语义相近」的 query 答案可能天差地别（「A 方案优缺点」vs「A 方案回滚」），所以阈值要严 + 拒答类结果不进缓存。
- 失效策略：知识库文档更新事件触发按 chunk 反查受影响缓存条目删除，而不是全量 TTL 赌运气。
- 追问钩子：多租户下语义缓存最大的风险？——跨租户命中，缓存 key 必须拼租户 ID，且向量空间按租户独立时语义缓存直接禁用。

```ts
async function cachedAnswer(tenant, q) {
  const norm = normalize(q);
  const key = 't:' + tenant + ':qa:' + hash(norm);
  const hit = await redis.get(key);
  if (hit) return JSON.parse(hit);
  const { text, level } = await pipeline(tenant, norm);
  if (level !== 'reject') {                                  // 拒答不缓存
    await redis.set(key, JSON.stringify({ text, level }), 'EX', 3600);
  }
  return { text, level };
}
```

