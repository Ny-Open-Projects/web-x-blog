---
title: [1040] 部门重组后权限大改，RAG 检索权限怎么跟着变
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 权限]
type: 面试题
---

## 1040：部门重组后权限大改，RAG 检索权限怎么跟着变

**答**：
- 权限变更影响「过滤条件」与「数据标记」两侧：查询侧用户身份解析（部门树变化即时生效）；数据侧 chunk 的 acl 字段要批量重写（异步任务）。
- 时序风险：acl 重写完成前，可能出现「新人查到旧部门文档」（漏更新）或「调岗员工查不到应有文档」（过严）；处理：变更期间对受影响租户启用「双条件并集」（新旧 acl 任一匹配即可见），重写完成后再收紧——宁可暂时宽松不漏杀。
- 变更量级预估先行：受影响 chunk 数决定走「原地批量更新」还是「重建分片」，百万级以上用别名切换式重建。
- 追问钩子：怎么验证 acl 变更正确？——抽样对照：变更后随机抽样 chunk，按新旧权限矩阵各查一遍，比对「预期可见集合」，偏差率超阈值自动回滚。

```ts
async function aclMigration(change) {
  const affected = await index.countByAcl(change.from);
  if (affected > 1_000_000) return rebuildShardRoute(change);  // 大变更走重建
  router.setUnionMode(change, { during: 'migration' });        // 过渡期宽松并集
  await batchRewriteAcl(change, { concurrency: 100 });
  const drift = await sampleVerify(change);                    // 抽样对照
  if (drift > 0.001) return rollbackAcl(change);
  router.clearUnionMode(change);                               // 收紧
}
```
