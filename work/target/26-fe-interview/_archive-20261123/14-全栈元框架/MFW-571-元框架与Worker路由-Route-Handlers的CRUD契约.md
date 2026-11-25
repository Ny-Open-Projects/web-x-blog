---
title: [MFW-571] Route Handlers 的 CRUD 契约：REST 语义与框架路由的映射
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-571：Route Handlers 的 CRUD 契约

**答**:
- Route Handler 的方法语义：app/api/products/route.ts 导出 GET/POST/PATCH/DELETE——Web 标准 Request/Response（Remix 哲学 RBL-534 的 Next 版）；「REST 到框架的映射」：collection（/api/products：GET 列表 POST 创建）vs item（/api/products/[id]：GET 单个 PATCH 更新 DELETE 删除）。
- 状态码的语义纪律：200（读成功）/201（创建）/204（删除成功无体）/400（校验）/401（未认证）/403（无权限）/404（不存在）/409（冲突）/422（语义错误）——「REST 状态码 ≠ 简单的 200/500」（错误分级 RBL-513 的 API 版）。
- Route Handler 与 Server Action 的分工：Handler = 资源 API（外部消费/RN/第三方/缓存友好——GET 可 CDN）；Action = UI 变更（组件内聚/渐进增强）；「资源 API 与 UI 动作」的分离。
- 追问钩子：为什么「GET 可缓存」是 Handler 相对 Action 的关键差异？——GET Handler 产出可进 CDN/Data Cache（Next 的 GET 路由可 route segment config 缓存——`export const revalidate = 60`）；Action POST 永不缓存；「读路径走缓存、写路径走实时」——REST 方法语义不只是风格，是缓存协议的基础（HTTP 语义 = 缓存语义：GET 幂等可缓存、POST 不幂等不可缓存 RBL-508 的 HTTP 原理层）。

```typescript
// collection route：app/api/products/route.ts
export async function GET(req: Request) {
  const q = new URL(req.url).searchParams;
  const list = await repo.list({ page: +q.get('page') ?? 1, q: q.get('q') });
  return NextResponse.json(list, {
    headers: { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' },   // GET 可缓存
  });
}
export async function POST(req: Request) {
  const body = await req.json();
  const parsed = CreateProduct.safeParse(body);
  if (!parsed.success)
    return NextResponse.json({ errors: parsed.error.flatten() }, { status: 422 });
  const created = await repo.create(parsed.data);
  return NextResponse.json(created, { status: 201 });
}
// item route：app/api/products/[id]/route.ts
export async function DELETE(_: Request, { params }) {
  const ok = await repo.delete(params.id);
  return ok ? new Response(null, { status: 204 }) : NextResponse.json({ e: 'nf' }, { status: 404 });
}
```
