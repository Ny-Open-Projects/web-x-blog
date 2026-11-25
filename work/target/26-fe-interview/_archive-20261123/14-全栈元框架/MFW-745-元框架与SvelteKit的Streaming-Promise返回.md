---
title: [MFW-745] SvelteKit 的 Streaming Promise 返回
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-745：SvelteKit Streaming Promise

**答**:
- load 返回 Promise 的流式语义：1) **load 返回 Promise**（`return { slow: fetchSlow() }`——不 await：Promise 传给 page——SvelteKit 流式渲染（await parent 的数据先发；Promise 的数据后到）；2) **page 侧消费**（SvelteKit 的 streamed data：`data.slow` 是 Promise——page 用 `{#await}` 块消费（pending/value/reject 三态）；3) 与 RSC 的对比：RSC 的 use(promise) RBL-606；SvelteKit 的 {#await}——两者都是「Promise 传递到 client 消费」（RSC 的 Flight $@ vs SvelteKit 的 streamed promise）。
- 序列化协议：turbo-stream（RBL-534 提到的——Promise 序列化为流式 chunk：Promise resolve 时流式发送值）；「turbo-stream 的 Promise 处理」：Promise → 流式标记 → resolve 时发送值。
- 流式与 SEO 的组合：关键内容 await（首包完整）；次要内容 Promise（流式补——SEO 首包策略 RBL-528 的 SvelteKit 版）。
- 追问钩子：为什么 SvelteKit 的「load 返回 Promise」比「全部 await」更灵活？——全部 await = 所有数据到齐才渲染（TTFB = 最慢查询）；Promise = 快数据先发（TTFB = 最快查询）+ 慢数据流式；「数据的分层」：关键内容 await（同步）、次要内容 Promise（异步）——开发者显式控制哪些数据阻塞渲染（RBL-520 shell 最小化的 SvelteKit 版）。

```svelte
// +page.server.js
export const load = async ({ params }) => {
  const product = await getProduct(params.id);           // await：关键内容（首包）
  const reviews = getReviews(params.id);                  // 不 await：Promise 流式
  const recommendations = getRecommendations(params.id);  // Promise 流式
  return { product, streamed: { reviews, recommendations } };
};
// +page.svelte
<script>
  export let data;
</script>
<h1>{data.product.name}</h1>                              {/* 同步：首包 */}
{#await data.streamed.reviews}
  <ReviewsSkeleton />                                     <!-- pending -->
{:then reviews}
  {#each reviews as r}<Review {r} />{/each}               <!-- resolve -->
{:catch error}
  <p>加载失败</p>                                          <!-- reject -->
{/await}
{#await data.streamed.recommendations}
  {:then recs}
    <Recs {recs} />                                       <!-- 流式到达 -->
  {/await}
{/await}
// turbo-stream：Promise resolve 时流式发送值（RBL-534 的 Promise 序列化）
```
