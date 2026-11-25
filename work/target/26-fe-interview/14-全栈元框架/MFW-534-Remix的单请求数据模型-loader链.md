---
title: [MFW-534] Remix 的 loader 链：单请求模型与并行数据加载
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-534：Remix loader 链：单请求与并行加载

**答**:
- Remix 的单请求模型：**一次 HTTP 请求**完成（loader 链服务端执行 + 文档渲染）——client 导航时 fetch 到同 URL（?_data= 参数拿 loader JSON）——「URL 即 API」的设计（数据端点与文档端点同一）。
- loader 链并行：嵌套路由的所有 loader **并行执行**（不等待父级——与 SvelteKit parent() 串行对比：Remix 默认并行，依赖靠 params/URL 共享不靠 parent 传递）——「并行默认」的取舍：快但父子依赖要绕（URL 参数传递或模块级共享）。
- Web 标准主义：loader 用 Request/Response/Web Fetch API（无框架对象）——可移植（Node/Bun/edge 同代码 RBL-530 Nitro 的同构哲学）。
- 数据流：loader → useLoaderData（序列化：turbo-stream——Promise/流式支持：loader 可返回 Promise 延迟流式）。
- 追问钩子：为什么 Remix 坚持「URL 即 API」而不做 Server Actions 的独立端点？——单一数据流（loader 数据 + HTML 同请求）让「网络瀑布」极简（一个请求 = 全部数据）；缓存可寻址（loader 结果 = URL 的缓存——CDN 可缓存 loader JSON）；代价是「变更语义」（mutation）要走 action POST（同 URL）——「读写的 URL 语义化」vs「动作的语义化」（Action 的意图明确）：Remix 是 REST 哲学的极致，Action 是 RPC 哲学的实用——反映两代框架的 API 风格演进。

```javascript
// loader 链并行（嵌套路由）
// app/routes/product.$id.tsx
export const loader = async ({ params }) => {
  const product = await db.products.find(params.id);    // 并行执行（不 await 父 loader）
  return json({ product });
};
// app/routes/product.$id.reviews.tsx（子路由）
export const loader = async ({ params }) => {
  const reviews = await db.reviews.byProduct(params.id); // 与父 loader 并行！
  return json({ reviews });
};
// client 导航：fetch('/product/1/reviews?_data=routes%2Fproduct%2E%24id%2Ereviews')
// URL 即数据端点（CDN 可缓存）
// turbo-stream：loader 返回 Promise 流式
export const loader = async () => json({
  critical: await getFast(),
  slow: getSlow(),                                       // Promise：流式延迟传输
});
```
