---
title: [MFW-071] Server Component 里直连数据库的最佳实践是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-071：Server Component 里直连数据库的最佳实践是什么？
**答**：
- RSC 直连 DB 是架构红利：少一层 API、少一次序列化，但要把**数据访问收敛到独立层**（`lib/data/*`），不要让 page 组件里散落 ORM 调用，否则缓存、权限、监控无从收口。
- 连接池纪律：Serverless/多实例部署下每个实例都建池会打爆 DB——用池化上限（如 pg pool max=5）或 HTTP 协议 serverless 驱动；全局单例池防热重建。
- 权限在数据层强制：函数带 session 参数、行级过滤（tenant/userId），不依赖「页面没渲染出来」做安全。
- 查询纪律：select 精确列、分页必带游标/offset 上限、N+1 用 join 或 in 批量；配合 unstable_cache/tags 复用结果。

```ts
// lib/data/products.ts —— 收敛的数据访问层
import { unstable_cache } from 'next/cache';
import { cache } from 'react'; // Request Memoization：一次渲染内同参去重

// 全局单例池，防止 dev 热更新/多 route 各建各的池
const globalForPg = globalThis as unknown as { pool?: Pool };
export const pool = globalForPg.pool ?? new Pool({ connectionString: ..., max: 5 });
globalForPg.pool = pool;

// 渲染内去重：多个组件同时取同一商品只查一次
export const getProduct = cache(async (id: string) => {
  const { rows } = await pool.query(
    'SELECT id, name, price, stock FROM products WHERE id = $1', // 精确列
    [id],
  );
  return rows[0] ?? null;
});

// 跨请求缓存：热销列表 5 分钟 + tag 失效
export const getHotProducts = unstable_cache(
  async (limit = 20) =>
    (await pool.query('SELECT id, name, price FROM products ORDER BY sales DESC LIMIT $1', [limit])).rows,
  ['hot-products'],
  { tags: ['products'], revalidate: 300 },
);

// 权限内聚：必须显式传 session，不查别人的订单
export async function getOrdersFor(session: Session, page = 0) {
  return pool.query('SELECT * FROM orders WHERE user_id = $1 LIMIT 20 OFFSET $2',
    [session.userId, page * 20]);
}
```
