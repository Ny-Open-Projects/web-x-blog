---
title: [ZSM-169] 流式渲染（Suspense streaming/PPR）下状态层有什么新问题？缓存注水和流式顺序怎么对齐？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-169：流式渲染（Suspense streaming/PPR）下状态层有什么新问题？缓存注水和流式顺序怎么对齐？
**答**：
- 流式意味着「页面不是一次注水完成」：骨架先到、各 Suspense 块的数据陆续注入。Query/SWR 的 dehydrate/fallback 必须按块随流注入，不能假设「首屏 HTML = 全量缓存」。
- 新问题一：hydrate 前客户端组件已挂载并可能发起请求（双取）——要用「fallback 灌好 key」或拦截首取（`enabled` 等注水完成）；新问题二：流式顺序不确定，乐观更新可能在数据到达前发生，落地时要按 clientId 合并而不是直接覆盖。
- PPR（部分预渲染）下静态壳与动态洞分离：静态部分无需缓存，动态洞用 fetch 缓存/RSC cache + 客户端交互缓存两层，要明确「洞内数据的失效口径」。
- 面试要点：能说清「dehydrate 的时机从『页面级』变成『块级』」这一变化即可体现理解。

```javascript
// Next App Router：每个流式块独立注水
export default async function Page() {
  return (
    <>
      <Suspense fallback={<FeedSkeleton/>}>
        <FeedSection/>        {/* 内部 client 组件用 useQuery；key 由 fallback 层的 prefetch 填充 */}
      </Suspense>
      <Suspense fallback={<StatsSkeleton/>}>
        <StatsSection/>
      </Suspense>
    </>
  )
}

// 块级注水模式：server 组件取数后传 fallback
async function FeedSection() {
  const feed = await getFeed()
  return (
    <SWRConfig value={{ fallback: { '/api/feed': feed } }}>
      <FeedClient/>           {/* 首渲染命中 fallback，不双取 */}
    </SWRConfig>
  )
}
```
