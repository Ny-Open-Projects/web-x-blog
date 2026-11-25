---
title: [1168] 用户报「搜不到」，怎么给工程师一个能复现的环境
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 调试]
type: 面试题
---

## 1168：用户报「搜不到」，怎么给工程师一个能复现的环境

**答**：
- 复现三要素：当时的 query（含改写前后）、当时的索引版本、当时的配置（top-k/过滤/rerank）——缺一个都可能「我这边能搜到」。
- 工具化：查询快照自动落库（每次检索记录完整输入输出），「复现链接」一键重放（锁定索引版本与配置），工程师 30 秒内看到用户看到的。
- 权限差异是隐形变量：用户权限过滤不同结果不同，复现必须带「用户的权限上下文」（脱敏后的过滤条件），否则复现必失败。
- 追问钩子：复现不了怎么办？——说明问题在「环境差异」（数据版本、权限、灰度分流），复现工具要显示「当前与当时的 diff」（索引版本差、配置差），把差异本身作为线索。

```ts
async function snapshotQuery(ctx, result) {
  await snapshots.put({ q: ctx.raw, rewritten: ctx.rewritten,
    idxVer: await alias.version(), cfg: ctx.cfg,
    acl: redact(ctx.acl), top: result.hits.slice(0, 5) });
  return snapshotLink(ctx.taskId);              // 附在用户反馈里
}
async function reproduce(link) {
  const s = await snapshots.get(link);
  return withEnv({ idxVer: s.idxVer, cfg: s.cfg, acl: s.acl })
    .search(s.q);                               // 锁定环境重放
}
```
