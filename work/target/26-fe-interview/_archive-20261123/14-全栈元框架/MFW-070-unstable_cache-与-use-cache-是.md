---
title: [MFW-070] unstable_cache 和未来的 use cache 分别解决什么问题？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-070：unstable_cache 和未来的 use cache 分别解决什么问题？
**答**：
- `unstable_cache`：把**任意函数的返回值**包进 Data Cache（fetch 缓存之外的补丁），适合缓存 DB 查询这类不走 fetch 的数据源；带 tags/revalidate，可被 revalidateTag 按需失效。
- `use cache`（Canary 演进中）：把缓存声明下沉到**组件/函数级指令**——在组件或函数顶部写 `'use cache'`，该作用域内所有取数自动缓存，颗粒度从「请求级 fetch」升级到「函数级作用域」，是缓存模型的第三代（Request Memoization → Data Cache → use cache）。
- 两者的定位差异：unstable_cache 是包装器（侵入小、显式），use cache 是编译指令（心智更接近「这个函数的结果是可缓存的」），且能缓存渲染输出而不只是数据。
- 共同纪律：可缓存的函数必须是**纯取数**，不能读 cookies/headers；失效策略要么挂 tag 要么设 revalidate，无失效手段的缓存是事故源。

```ts
// 1) unstable_cache：缓存 DB 查询
import { unstable_cache } from 'next/cache';

const getHotProducts = unstable_cache(
  async () => db.product.findMany({ where: { isHot: true } }),
  ['hot-products'],     // 缓存 key 基
  { tags: ['products'], revalidate: 300 },
);

// 2) revalidateTag('products') 可精准失效

// 3) use cache 指令形态（Canary）：
async function getRecommendations(userId: string) {
  'use cache';
  const recos = await recoService.forUser(userId);
  return recos;
  // 缓存时长与 tag 通过 cacheLife/cacheTags 声明
}
```
