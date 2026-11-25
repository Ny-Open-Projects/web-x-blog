---
title: [MFW-508] Next.js 缓存体系全景：Request/Data/Full Route/Router 四缓存
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-508：Next.js 缓存体系全景：四种缓存的关系与失效传播

**答**:
- 四缓存矩阵：1) **Request Memoization**（同请求内 fetch 去重——React cache()，生命周期单请求）；2) **Data Cache**（fetch 结果跨请求持久——ISG 数据层，键=URL+选项）；3) **Full Route Cache**（整条路由的 RSC payload + HTML 静态化——构建期预渲染）；4) **Router Cache**（客户端内存：已访问路由的 payload——导航瞬时回退）。关系：Full Route Cache 构建于 Data Cache 之上；revalidateTag/Path 逐层失效（Data 失效 → Full Route 重生成 → Router Cache 失效通知）。
- 失效传播的精确语义：revalidateTag(tag) → 下一次访问时 Data Cache 过期重取 → Full Route Cache 标脏（stale-while-revalidate：返回旧的 + 后台重生成）→ 客户端 Router Cache 因「同 tag 订阅」被失效（RSC payload 重新拉）。
- 常见事故：改了 DB 但页面不变——排查顺序：fetch 是否被缓存（GET 默认缓存/POST 不缓存）→ tag 是否正确打 → Full Route 是否静态化（dynamic API 使路由动态化则无 Full Route Cache）。
- 追问钩子：为什么四层缓存不合并成一层？——生命周期与失效粒度不同：请求级去重（毫秒）/数据级（分钟~天）/路由级（构建期~天）/客户端（会话）——每层的失效键与时机独立；合并 = 失效粒度绑定（改一条数据炸全站缓存）；分层缓存的经典架构（与 RBL-799 构建缓存三层同构：作用域与生命周期决定分层）。

```javascript
// 四缓存的失效传播链
// revalidateTag('products')
//   → Data Cache: tag='products' 的条目标脏
//   → Full Route Cache: 引用该 tag 的路由标脏（stale-while-revalidate）
//   → Router Cache: 客户端订阅被通知，payload 重新拉取
import { revalidateTag } from 'next/cache';
export async function updateProduct(id, data) {
  await db.products.update(id, data);
  revalidateTag('products');                             // 三层联动失效
}
// 读侧打标
async function getProducts() {
  return fetch('https://api/products', { next: { tags: ['products'], revalidate: 3600 } });
}
// 排查「页面不更新」的三步
// 1) fetch 默认缓存？→ next: { revalidate: 0 } 或 cache: 'no-store'
// 2) 路由是静态的？→ 用了 headers()/cookies() 会自动动态化
// 3) tag 对了吗？→ 写读两侧 tag 一致
```
