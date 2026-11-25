---
title: [MFW-533] Nuxt 的 useFetch/useAsyncData：缓存键与负载共享
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-533：Nuxt useAsyncData：缓存键与负载共享

**答**:
- useAsyncData 的键语义：显式 key（`useAsyncData('user-' + id, fn)`）= 缓存/去重的键——同 key 的多组件调用共享一次执行（SSR 负载共享：payload 只传一份）；useFetch(url) 的 key 自动从 url 生成（同 url 自动去重——RBL-529 cache() 的 Nuxt 版）。
- 与 Next cache() 的差异：Nuxt 的 key 是显式契约（开发者命名——可跨请求复用 payloadStore：`getCachedData` 自定义缓存策略如 localStorage）；React cache() 请求级隐式。「显式 key 的优势」：可精细控制（key 即 API——刷新/失效按 key 操作 `refreshNuxtData(key)`）；劣势：键管理负担（重复 key = 静默共享数据）。
- SSR payload 共享的细节：server 渲染期间执行一次 → 结果序列化进 payload → client 水合直接取（不重执行）——「执行一次、传输一次、水合复用」；client 导航时重新执行（或走 payload 缓存）。
- 追问钩子：为什么 Nuxt 选择「显式 key」而 React 选择「函数+参数隐式键」？——显式 key 是「数据资源的命名」（像 API 一样可寻址：刷新/失效/跨组件订阅都指向名字）；隐式键免命名负担但不可寻址（React 侧操作只能 revalidateTag/refresh 粗粒度）——「可寻址性 vs 免管理」是数据层 API 的经典权衡（与 RBL-508 四缓存的 tag 可寻址化方向一致：Next 也在向显式标签演进）。

```javascript
// useAsyncData 显式键
const { data: user, refresh } = await useAsyncData(
  `user-${id}`,                                         // 显式键：可寻址
  () => $fetch(`/api/user/${id}`),
  { server: true, lazy: false,                          // SSR 执行
    getCachedData: (key, nuxtApp) =>
      nuxtApp.payload.data[key] ?? clientCache.get(key) // 跨请求缓存策略
  });
// 同 key 的其他组件：共享（SSR 只执行一次）
// 另一组件
const { data } = await useAsyncData(`user-${id}`, () => $fetch(`/api/user/${id}`));
// 精确失效
refreshNuxtData(`user-${id}`);                          // 按 key 刷新——可寻址操作
// useFetch 的自动 key
const { data: list } = useFetch('/api/products');        // key 自动 = /api/products
```
