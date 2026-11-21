---
title: [MFW-073] RSC 页面的取数瀑布（waterfall）怎么发现和治理？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-073：RSC 页面的取数瀑布（waterfall）怎么发现和治理？
**答**：
- 典型成因：父组件 await 完才渲染子组件、子组件里再 await——串行链路把延迟累加成 `T1+T2+T3`；正确形态是**在渲染函数外先创建 Promise**，子组件只消费。
- 三种治理手段：① 同层并行 `Promise.all`；② 惰性传递（先发 promise 再 await/use 消化）；③ `React.cache` 去重同参调用 + Data Cache 跨请求复用。
- 发现手段：Next DevTools 的 trace 视图、OpenTelemetry span 里看取数 span 的串行排列、或 `performance` 上报 TTFB 与各 API 耗时对比。
- 注意权衡：并行不是免费的——Promise.all 一损俱损，非关键路径用 `allSettled` 或拆 Suspense 边界单独兜底。

```tsx
// ❌ 瀑布：商品 -> 评论 -> 用户信息，串行 3 段
async function BadPage({ id }: { id: string }) {
  const product = await getProduct(id);
  const reviews = await getReviews(id);
  const author = await getUser(reviews[0].userId);
  return <>{product.name}{author.name}</>;
}

// ✅ 治理后
async function GoodPage({ id }: { id: string }) {
  // 首个必须的请求先发；其余 promise 提前创建，交给子组件 use()
  const productPromise = getProduct(id);
  const reviewsPromise = getReviews(id); // 与 product 并行
  const product = await productPromise;

  const topReviewPromise = reviewsPromise.then((rs) => rs[0]).then((r) => getUser(r.userId));

  return (
    <>
      <h1>{product.name}</h1>
      <Suspense fallback={<Skeleton />}>
        <TopAuthor promise={topReviewPromise} />
      </Suspense>
    </>
  );
}

function TopAuthor({ promise }: { promise: Promise<User> }) {
  return <UserCard user={use(promise)} />;
}
```
