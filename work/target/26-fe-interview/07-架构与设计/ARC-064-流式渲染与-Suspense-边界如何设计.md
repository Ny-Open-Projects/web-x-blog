---
title: [ARC-064] 流式渲染与 Suspense 边界如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-064：流式渲染与 Suspense 边界如何设计？
**答**：
- 流式渲染：先发 shell（骨架 + 已就绪数据），慢数据源用 Suspense 包住后发，TTI 大幅提前。
- 边界划分原则：一个 Suspense 边界 = 一个独立加载语义的区块，粒度太细闪烁、太粗又回到白屏等待。
- 错误边界与 Suspense 成对出现：每个异步区块配 error fallback，避免一个慢/挂接口拖死整页。

```tsx
// 流式渲染架构：shell 先行 + 分区块后发
export default function ProductPage({ id }: { id: string }) {
  return (
    <Layout>                                          {/* 立即输出：导航/骨架 */}
      <Suspense fallback={<ProductSkeleton />}>       {/* 区块1：核心商品信息 */}
        <ProductHeader id={id} />                     {/* async RSC，慢就后发 */}
      </Suspense>
      <Suspense fallback={<RecommendSkeleton />}>     {/* 区块2：推荐流，独立降级 */}
        <ErrorBoundary fallback={<RecommendError />}>
          <Recommendations id={id} />                 {/* 挂了不影响主内容 */}
        </ErrorBoundary>
      </Suspense>
      <Reviews id={id} loading={<ReviewsSkeleton />} />  {/* 区块3：loading props 模式 */}
    </Layout>
  );
}
// 划分依据：数据源与加载时长差异、业务重要性、是否允许独立降级
```
