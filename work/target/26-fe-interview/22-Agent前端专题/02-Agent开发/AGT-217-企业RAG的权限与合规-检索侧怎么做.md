---
title: [AGT-217] 企业 RAG 的权限与合规——检索侧的安全设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-217：企业内部知识库 RAG，权限与合规在检索侧怎么设计？

**答**:
- 权限必须在检索侧强制执行，不能靠生成侧"叮嘱"：块级 ACL（文档/部门/密级标签在索引时写入元数据），查询时由系统（不是 LLM）注入用户权限过滤——权限过滤是硬约束（AGT-151 的检索剪枝）。
- 泄露通道要全堵：缓存按用户/权限分桶（不能跨用户命中）、日志脱敏（检索 query 与召回内容可能含敏感信息）、导出与引用的二次校验（答案引用的块必须是该用户可见的）、跨租户索引物理或逻辑隔离。
- 合规动作：索引前内容审查（个人信息脱敏/违规内容拦截）、答案输出走内容安全审核、审计日志记录"谁在何时查了什么、命中了什么"（满足事后追溯）。
- 边界场景：用户搜索"无权限文档的摘要"也是泄露——拒答话术统一为"您暂无权限访问相关内容"，不透露存在性细节。

```javascript
async function secureRetrieve(query, user) {
  // 1. 系统注入权限过滤（覆盖一切 LLM 生成的 filter）
  const filter = { acl: { $in: user.visibleTags } };
  // 2. 缓存按权限分桶
  const cacheKey = hash(query + JSON.stringify(user.visibleTags));
  const docs = await vectorSearch(query, { filter, k: 10 });
  await audit.log({ user: user.id, query: mask(query), hit: docs.length });
  // 3. 召回块二次校验（防御索引 ACL 缺失）
  return docs.filter(d => user.visibleTags.includes(d.acl));
}
```
