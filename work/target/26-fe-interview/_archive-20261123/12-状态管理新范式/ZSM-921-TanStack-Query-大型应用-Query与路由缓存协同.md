---
title: [921] 路由 loader 数据与 Query 缓存怎么协同
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 路由]
type: 面试题
---

## 921：路由 loader 数据与 Query 缓存怎么协同

**答**：
- 单一缓存原则：数据只存 Query 缓存，路由 loader 只做 ensureQueryData（预取并等待）——loader 不自己存数据（双缓存 = 两份真相），组件里 useQuery 同 Key 读缓存（loader 已预取则零请求）。
- 路由失效：路由切换不等于缓存失效——缓存生命周期跟数据（staleTime/gcTime），不跟路由；只有离开作用域的临时数据才在路由卸载时定向 remove。
- loader 与组件竞态：loader 未完成导航未提交（框架阻塞渲染）——组件挂载时缓存必热；loader 失败要区分（预取失败不阻塞导航——catch 后组件内 useQuery 自己重试）。
- 追问钩子：为什么 loader 用 ensureQueryData 而不是 prefetchQuery？——ensure 会 await（阻塞导航直到数据就绪，适合关键数据），prefetch 发射后不管（适合非关键预取）；两者选择就是关键路径标注。

```ts
const route = createRoute({
  loader: async ({ params }) => {
    try {
      await qc.ensureQueryData({
        queryKey: userKeys.detail(params.id), queryFn: ... });
    } catch { /* 预取失败不阻塞 */ }
  },
  component: () => { const { data } = useUser(params.id); ... } // 命中缓存
});
```

