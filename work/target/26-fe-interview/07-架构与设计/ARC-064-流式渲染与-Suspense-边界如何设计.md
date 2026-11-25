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

**追问**：

1. Suspense 边界里的数据在流式过程中报错，已经发出去的 HTML 怎么办？ → 框架会把该边界替换为 fallback，靠内联脚本在前端完成，所以错误兜底块必须能独立渲染，不依赖还没到的数据。
2. 边界划得太细导致骨架频繁闪烁，能不能延迟显示 fallback？ → 合并慢区块共用边界，或用框架的延迟 reveal 与最短展示时长，宁可晚一点出骨架也别闪。
3. 流式 SSR 下爬虫拿到的是半截 HTML，SEO 怎么保证？ → 关键内容放 shell 里同步输出，或给爬虫走完整渲染的快照通道，别让核心信息挂在最后一个 Suspense 里。
