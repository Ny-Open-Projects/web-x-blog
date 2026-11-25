---
title: [MFW-520] Streaming SSR 的 TTFB 工程：shell 最小化与关键路径优先
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-520：Streaming SSR 的 TTFB 工程：shell 最小化与优先级

**答**:
- TTFB 的决定项：shell（同步渲染部分）完成时刻——shell 包含的内容越少 TTFB 越快；「shell 最小化」= 骨架 + 静态结构进 shell，数据依赖全部 Suspense 化（异步洞）。
- 关键路径优先策略：1) 组件树层次即优先级（外层 Suspense 先 resolve 先发——把 LCP 内容放最外层边界）；2) 数据获取的并行化（loader 瀑布检测 RBL-930）；3) 首屏数据的「shell 内联」（极小且必须的数据进 shell——如标题）。
- TTFB 与 LCP 的分离：TTFB 快（shell 即发）≠ LCP 快（LCP 元素可能在流末尾）——「LCP 元素的边界层级」设计：LCP 内容的 Suspense 应在树浅层。
- 追问钩子：为什么「把所有内容都 Suspense 化」不是最优 TTFB 策略？——shell 太小 = 传输的骨架无意义（爬虫只见骨架：SEO 劣化）+ 客户端补丁量大（交互延迟）；最优 shell = 「静态结构 + 关键数据」——shell 的信息量权衡：SEO 需要 LCP 内容在首包（爬虫视角）——流式 SEO 的实测结论是内容在流内即可（Google 渲染流），但「越早越好」仍是稳妥默认。

```javascript
// shell 最小化的分层
export default async function ProductPage({ params }) {
  // 同步（进 shell）：布局、标题结构
  return (
    <>
      <Header />                                         {/* 静态，进 shell */}
      <h1><Suspense fallback="商品标题…"><Title id={params.id} /></Suspense></h1>
      {/* LCP 元素：树浅层，最优先 resolve */}
      <Suspense fallback={<GallerySkeleton />}>
        <Gallery id={params.id} />                       {/* 首图：关键路径 */}
      </Suspense>
      <Suspense fallback={null}>
        <Reviews id={params.id} />                       {/* 次要内容：深层的洞 */}
      </Suspense>
    </>
  );
}
// loader 并行检测（RBL-930）
async function Title({ id }) {
  const [product, meta] = await Promise.all([            // 并行：防瀑布
    getProduct(id), getMeta(id),
  ]);
  return product.name;
}
```
