---
title: [904] TanStack Query 的请求瀑布（waterfall）怎么治理
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 性能]
type: 面试题
---

## 904：TanStack Query 的请求瀑布（waterfall）怎么治理

**答**：
- 瀑布来源：父组件先 query 子组件再 query（组件树串行）、依赖 query（B 的参数来自 A）、loader 缺失（挂载后才发请求）——三种瀑布在大型应用叠加能把首屏拖到 3s+。
- 治理三板斧：提升（子组件 query 提升到父级用 combine 或一次性 fetch）、预取（路由 loader 里 ensureQueryData——挂载前缓存已热）、合并（参数可合并的拆分 query 合成一个端点）。
- 依赖 query 的正确姿势：enabled: !!a.data 是必要的，但把 A 改成「返回多实体的聚合接口」消除依赖更彻底——先问架构能不能消除依赖，再谈优化依赖。
- 追问钩子：useQueries 动态列表什么时候用？——同构并行查询（如 N 个商品详情），且配合 placeholderData 防止并行结果逐个到达的跳变。

```ts
// 路由级预取消除挂载瀑布
const router = createRouter({
  loader: async () => {
    await qc.ensureQueryData({ queryKey: userKeys.detail(id), queryFn: ... });
  },
});
// 依赖查询：enabled 门控
const a = useQuery({ queryKey: ['a', id], queryFn });
const b = useQuery({ queryKey: ['b', a.data?.x],
  queryFn: () => fetchB(a.data!.x), enabled: !!a.data });
```

