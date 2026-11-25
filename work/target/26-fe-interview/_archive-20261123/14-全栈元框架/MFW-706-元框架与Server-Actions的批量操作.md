---
title: [MFW-706] Server Actions 的批量操作
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-706：Server Actions 批量操作

**答**:
- 批量操作的 action 设计：1) **批量 API**（action 接受数组：`bulkDelete(ids: string[])`——单次 action 多条操作（减少网络往返——N 个 action 调用 → 1 个批量）；2) **部分成功语义**（批量中 3 成功 2 失败——返回 `{ results: [{ id, ok, error? }], summary }`——逐条结果 RBL-513）；3) **事务边界**（全成功或全失败（事务回滚）vs 部分提交（业务决定——批量删除通常全事务）。
- 乐观 UI 的批量：useOptimistic 的批量乐观（N 条同时乐观删除——UI 立即全部消失；失败回滚整批（事务回滚语义的 UI 版）或部分回滚（部分成功的 UI 对应）——「批量乐观与事务语义的 UI 对应」。
- 大批量的分片：10000 条批量 = 单次 action 的负载限制（body 大小/DB 事务大小）——分片（100 条/批 × 100 批——并发或串行）；「分片的事务边界」：每片一个事务（部分成功的分片——整体不保证）。
- 追问钩子：为什么「批量 action 的事务边界」要显式声明？——单条操作的事务边界清晰（一条 = 一个事务）；批量 = 多条在同一个事务（全回滚）还是各自事务（部分提交）——业务语义决定：库存扣减 = 全事务（一致性）；日志写入 = 各自事务（可用性）；「批量的事务边界」是架构决策（与 RBL-632 多包发布的事务语义同构：原子性 vs 可用性的权衡）。

```typescript
// 批量 action（事务内全回滚）
'use server';
export async function bulkDelete(ids: string[]) {
  return db.$transaction(async (tx) => {
    const results = [];
    for (const id of ids) {
      try {
        await tx.items.delete({ where: { id } });
        results.push({ id, ok: true });
      } catch (e) {
        throw e;                                         // 事务内抛错 = 全回滚
      }
    }
    revalidateTag('items');
    return { results, summary: { total: ids.length, ok: results.length } };
  });
}
// client 乐观批量
'use client';
function BulkDelete({ ids }) {
  const [optimisticItems, removeOptimistic] = useOptimistic(
    items, (cur, removeIds) => cur.filter(i => !removeIds.includes(i.id)));
  return <button onClick={async () => {
    removeOptimistic(ids);                               // 全部乐观移除
    const result = await bulkDelete(ids);                // 失败回滚（全部恢复）
    if (!result.summary.ok) showError(result.summary);
  }}>删除 {ids.length} 项</button>;
}
// 大批量分片
async function chunkedBulk(ids: string[], chunkSize = 100) {
  const results = [];
  for (let i = 0; i < ids.length; i += chunkSize)
    results.push(await bulkDelete(ids.slice(i, i + chunkSize)));
  return results;
}
```
