---
title: [MFW-846] 流式渲染中慢查询造成 Suspense 边界队头阻塞，怎么解耦
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-846：流式渲染中慢查询造成 Suspense 边界队头阻塞，怎么解耦

**答**：
- 结论：同一 Suspense 边界内多个并行请求，最慢的那个决定 flush 时机（队头阻塞）；把慢查询拆到独立边界，让快内容先 flush。
- 落地：按「数据就绪时间/业务重要性」划边界，关键路径最小边界，慢查询用独立边界 + 轻量 fallback。
- 追问钩子：边界拆太细有什么代价？——HTML 分片数与客户端补丁增多，需要权衡。

```javascript
// ❌ 单边界：慢评论拖住整个商品页
<Suspense fallback={<FullSkeleton/>}>
  <Product/>      // 快
  <Comments/>     // 慢 2s → 整块等它
</Suspense>

// ✅ 多边界：快内容先 flush
<Suspense fallback={<ProductSkeleton/>}><Product/></Suspense>
<Suspense fallback={<CommentSkeleton/>}><Comments/></Suspense>
<Suspense fallback={<RecSkeleton/>}><Recommendations/></Suspense>
// 商品详情先到，评论/推荐各自后到，互不阻塞
```
