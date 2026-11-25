---
title: [NODE-055] getServerSideProps 的执行环境与优化？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-055：getServerSideProps 的执行环境与优化？
**答**：
- 执行环境：**每次请求时在服务端（Node）执行**，永远不进入客户端 bundle（函数体不会被打包进浏览器 JS，但 `import` 的模块会进服务端依赖）；拿不到 `window`，可访问 `req`/`res`（cookie、header）。
- 与 `getStaticProps` 的选择：内容不变用 Static（构建时生成 + ISR 增量再生），个性化/实时数据才用 ServerSide——**默认该用 Static，SSR 是成本**。
- 优化：并行 `Promise.all` 拉数据、控制总超时、复用 BFF 聚合缓存、避免在 GSSP 里做重计算、敏感头不透传给下游。

```javascript
// pages/product/[id].js
export async function getServerSideProps({ params, req, res }) {
  const uid = parseSid(req.headers.cookie);          // 服务端：可读 cookie/headers
  const start = Date.now();

  // 1. 并行拉取 + 单项超时（复用 BFF gather 模式）
  const [product, reviews] = await Promise.allSettled([
    fetchJSON(`${BFF}/product/${params.id}`, 800),
    fetchJSON(`${BFF}/reviews?gid=${params.id}&limit=5`, 500),
  ]);
  if (product.status === 'rejected') return { notFound: true };  // 404 而非 500

  // 2. 匿名可缓存时，直接告诉 CDN/浏览器缓存整页
  if (!uid) {
    res.setHeader('cache-control', 'public, s-maxage=60, stale-while-revalidate=300');
  }

  return {
    props: {                                          // JSON 序列化后注入页面
      product: product.value,
      reviews: reviews.status === 'fulfilled' ? reviews.value : [],
      ssrCost: Date.now() - start,
    },
  };
}
```

```javascript
// 优化对比：能 Static 的不要 ServerSide
// pages/docs/[slug].js —— 文档内容构建期可确定 → SSG + ISR
export async function getStaticProps({ params }) {
  const doc = await getDoc(params.slug);
  return {
    props: { doc },
    revalidate: 300,             // ISR：300s 后台再生，兼得静态性能与新鲜度
  };
}
// 准则：Static(免费) > ISR(便宜) > ServerSide(每次渲染) > CSR(白屏后渲染)
```
