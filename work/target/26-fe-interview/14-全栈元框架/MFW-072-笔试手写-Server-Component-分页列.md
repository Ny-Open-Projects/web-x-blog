---
title: [MFW-072] 笔试：手写一个 RSC 分页列表页（游标分页 + searchParams）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-072：笔试：手写一个 RSC 分页列表页（游标分页 + searchParams）
**题目**：实现商品列表页 `/products?cursor=xxx&q=手机`：① 游标分页（不用 offset，防深分页性能塌陷）；② 关键词过滤走索引；③ 下一页用 Link 带 query，服务端渲染拿数据；④ 空态与非法 cursor 要兜底。

```tsx
// app/products/page.tsx
import Link from 'next/link';

const PAGE_SIZE = 20;

export default async function ProductsPage({
  searchParams,
}: { searchParams: Promise<{ cursor?: string; q?: string }> }) {
  const { cursor, q = '' } = await searchParams; // Next 15: searchParams 是 Promise

  // 游标 = 上一页最后一行的 (sales, id)，稳定排序键防翻页重排
  const rows = await listProducts({
    q,
    cursor: cursor ? decodeCursor(cursor) : null,
    limit: PAGE_SIZE + 1, // 多取 1 条判断 hasNext
  });

  const hasNext = rows.length > PAGE_SIZE;
  const items = rows.slice(0, PAGE_SIZE);
  const nextCursor = hasNext ? encodeCursor(rows[PAGE_SIZE - 1]) : null;

  if (!items.length) return <EmptyState q={q} />;

  return (
    <>
      <ul>
        {items.map((p) => (
          <li key={p.id}>{p.name} · ¥{p.price}</li>
        ))}
      </ul>
      {nextCursor && (
        // query 变化触发新的服务端渲染；q 用隐藏域随行
        <Link href={`/products?q=${encodeURIComponent(q)}&cursor=${nextCursor}`}>
          下一页
        </Link>
      )}
    </>
  );
}
```

```ts
// lib/data/list-products.ts
type Cursor = { sales: number; id: string };

export function encodeCursor(row: { sales: number; id: string }): string {
  return Buffer.from(JSON.stringify({ s: row.sales, id: row.id })).toString('base64url');
}
export function decodeCursor(cursor: string): Cursor | null {
  try { // 非法 cursor 兜底：回第一页而不是 500
    const o = JSON.parse(Buffer.from(cursor, 'base64url').toString());
    return typeof o.s === 'number' && typeof o.id === 'string' ? { sales: o.s, id: o.id } : null;
  } catch { return null; }
}

export async function listProducts({ q, cursor, limit }: {
  q: string; cursor: Cursor | null; limit: number;
}) {
  const where = [];
  const args: unknown[] = [];
  if (q) { args.push(`%${q}%`); where.push(`name ILIKE $${args.length}`); }
  if (cursor) { // keyset 条件：sales < cur.s OR (sales = cur.s AND id < cur.id)
    args.push(cursor.sales, cursor.id);
    where.push(`(sales, id) < ($${args.length - 1}, $${args.length})`);
  }
  args.push(limit);
  return (await pool.query(
    `SELECT id, name, price, sales FROM products
     ${where.length ? 'WHERE ' + where.join(' AND ') : ''}
     ORDER BY sales DESC, id DESC LIMIT $${args.length}`, args)).rows;
}
```

**评分点**：
1. 用 keyset（`(sales, id) < (...)`）而非 OFFSET，说得出深分页性能动机。
2. `limit + 1` 判 hasNext，不额外 COUNT 全表。
3. cursor 解析有 try/catch 兜底，非法游标回第一页而非报错。
4. searchParams 按 Next 15 异步处理；q 参数 encodeURIComponent。
5. 排序键稳定（sales DESC, id DESC），翻页不重排不漏行。
