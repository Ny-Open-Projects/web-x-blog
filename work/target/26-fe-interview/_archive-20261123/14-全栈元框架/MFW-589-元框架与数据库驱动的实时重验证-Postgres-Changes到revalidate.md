---
title: [MFW-589] 数据库变更到缓存失效：Postgres Changes → revalidate 管线
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-589：Postgres Changes → revalidate 管线

**答**:
- DB 变更驱动的缓存失效：1) **CDC 管线**（Postgres logical replication / LISTEN-NOTIFY → 变更事件）；2) 事件 → tag 映射（RBL-577 触发源映射的 DB 版：表变更 → 实体 tag）；3) 失效执行（CDC 消费者 → Next 的 revalidate 端点——跨进程 RBL-569）。
- LISTEN-NOTIFY vs logical replication：NOTIFY（轻量：通知无数据——消费端回查 DB；事务内原子——事务提交才通知）；logical replication（带数据：WAL 级——完整变更行）；「通知驱动 vs 数据驱动」的选型：简单失效用 NOTIFY（只取 id 回查）、审计/多消费用 replication。
- 失效的延迟画像：变更 → NOTIFY（事务提交即时）→ 消费者拉取（轮询延迟/长连接即时）→ revalidate——端到端 <1s（实时失效）；「失效延迟的容忍」决定管线投入（秒级容忍用轮询、亚秒用长连接）。
- 追问钩子：为什么「DB 变更 → 缓存失效」要经过消息管线而不是「渲染时直接查 DB 绕过缓存」？——绕过缓存 = 每请求 DB 查询（成本 RBL-934 预算崩）；缓存 + 精确失效 = 缓存收益保留 + 新鲜度保证——「失效管线的复杂度」换取「缓存的命中率」：失效是缓存的必要配套（RBL-508 四缓存的失效面）；管线的每一步延迟决定用户看到旧数据的时间——新鲜度 SLO（RBL-904）的失效链路分解。

```typescript
// CDC 消费者（独立进程）
import { Client } from 'pg';
const listener = new Client({ connectionString: PG_URL });
await listener.connect();
await listener.query('LISTEN product_changes');
listener.on('notification', async (msg) => {
  const { productId, op } = JSON.parse(msg.payload);
  // 1) 映射：表变更 → tag（RBL-577 层级）
  const tags = [`product:${productId}`, 'products'];
  // 2) 跨进程失效：调 Next 的 revalidate 端点
  await fetch(`${NEXT_URL}/api/revalidate`, {
    method: 'POST',
    headers: { authorization: `Bearer ${REVALIDATE_SECRET}` },
    body: JSON.stringify({ tags }),
  });
});
// Next 侧：revalidate 端点（RBL-569）
// app/api/revalidate/route.ts
export async function POST(req: Request) {
  if (req.headers.get('authorization') !== `Bearer ${REVALIDATE_SECRET}`)
    return new Response('Unauthorized', { status: 401 });
  const { tags } = await req.json();
  tags.forEach(revalidateTag);
  return NextResponse.json({ revalidated: tags, at: Date.now() });
}
```
