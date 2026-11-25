---
title: [NODE-265] GraphQL 缓存策略与 APQ？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-265：GraphQL 缓存策略与 APQ？
**答**:
- 自动持久化查询（APQ）：客户端只发 query hash → 服务端查白名单（预注册的 query）——减 payload + 白名单即安全策略（防任意 query）。
- resolver 级缓存：key = (返回类型+id) → 实体缓存（NODE-275 Apollo 规范化同款），DataLoader 缓存是请求内、APC 是跨请求。
- HTTP 层：query 哈希稳定时可用 CDN/边缘缓存（Cache-Control + APQ 组合）。
- 失效：实体变更 → 反向索引失效（NODE-275 同款）或短 TTL。

```javascript
// APQ 流程
app.post('/graphql', async (req, res) => {
  const hash = req.body.extensions?.persistedQuery?.hash;
  if (hash) {
    const query = await registry.get(hash);             // 白名单查 query 全文
    if (!query) return res.status(404).json({ errors: [{ message: 'PersistedQueryNotFound' }] });  // 客户端回退发全文
    req.body.query = query;
  }
  return graphqlHandler(req, res);
});
// 注册：CI 把前端用到的 query 全文按 hash 入注册表 → 未知 query 直接拒绝（防滥用）
```
