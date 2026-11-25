---
title: [907] 企业内 RAG 多租户/多部门场景，检索权限怎么隔离
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 权限]
type: 面试题
---

## 907：企业内 RAG 多租户/多部门场景，检索权限怎么隔离

**答**：
- 权限过滤必须在检索层做（filter 参数下发到引擎），不能召回后再过滤：后过滤会破坏 top-k 语义——召回 10 条滤掉 8 条，剩 2 条根本不够回答。
- 索引时给每个 chunk 写 acl 字段（部门/用户组/密级），查询时把用户身份解析成过滤条件，与向量检索同请求生效。
- 跨租户缓存高危：embedding 缓存、rerank 结果缓存 key 必须包含租户 ID，否则 A 公司员工可能命中 B 公司缓存答案，这是安全事故级 bug。
- 追问钩子：管理员临时授权怎么生效？——ACL 变更触发对应 chunk 的局部重建，比全量重建快几个量级。

```ts
async function retrieveFor(user, q, topK = 5) {
  const filter = { bool: { should: [
    { term: { acl_dept: user.dept } },
    { terms: { acl_groups: user.groups } },
  ], must_not: [{ term: { acl_secret: true } }] }};
  // filter 与 KNN 同请求下发：先过滤后近邻，保证 topK 在权限内
  return es.knnSearch({ knn: { field: 'vec', query_vector: embed(q), k: topK, filter },
    cache_key: 't:' + user.tenant }); // 缓存 key 必含租户
}
```

