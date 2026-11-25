---
title: [MFW-179] React Router v7 的 single fetch 改了什么？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-179：React Router v7 的 single fetch 改了什么？
**答**：
- Remix v2 的老模型：导航后用 `?_data=` 参数逐路由发**多个**请求数据，loader 按路由串行多次 HTTP；浏览器还能把 GET loader 当可缓存端点。
- single fetch（v7 默认）：一次导航只发**一个**请求（POST 到当前 URL，`Content-Type: turbo-stream`），返回所有 loader 数据的流式编码（turbo-stream，支持 Promise/Date/转义安全），框架在客户端按路由拆开复水。
- 好处：请求数从 N 个降到 1 个；loader 可以改为返回任意可序列化对象而不只是 JSON；流式输出让慢 loader 不阻塞整体导航。
- 代价与变化：端点变成 POST（对 CDN 缓存不友好——loader 端点不能简单 GET 缓存了），需要把「可缓存的纯数据」显式抽到 GET 端点或用 headers 约定；`Content-Type` 变化要求部署层不要按 GET 缓存策略一刀切。
- 迁移要点：老 `_data` 缓存头、`json()` helper 被废弃，loader 直接 return 对象；保持单次请求内 loader 并行（await Promise.all 而不是串行 await）。

```javascript
// RRv7 single fetch 模型下
export async function loader({ params }) {
  // 一次 POST 请求把所有路由 loader 数据流式返回
  const [product, reviews] = await Promise.all([
    getProduct(params.id),
    getReviews(params.id), // reviews 慢也不阻塞 product 先到（turbo-stream 流式）
  ]);
  return { product, reviews };
}
```