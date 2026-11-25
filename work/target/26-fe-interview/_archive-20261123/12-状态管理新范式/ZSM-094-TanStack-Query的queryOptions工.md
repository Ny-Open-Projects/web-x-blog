---
title: [ZSM-094] queryOptions 工厂是什么？它解决「key 和 queryFn 分离」的什么问题？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-094：queryOptions 工厂是什么？它解决「key 和 queryFn 分离」的什么问题？
**答**：
- queryOptions 把 queryKey/queryFn/staleTime 等打包成一个对象工厂，useQuery/prefetch/invalidate 全部消费同一份定义。
- 解决的问题：key 与 queryFn 分散两处容易拼错或演化不一致（key 改了 queryFn 忘改参数），失效时 key 拼错导致失效无效。
- 带类型收窄：TypeScript 下 queryOptions 保证 key 与 queryFn 的类型关联（v5 泛型推导）。
- 团队规范：每个资源域一个 queries 文件，导出 all/detail/list 工厂，禁止手写裸 key。

```javascript
import { queryOptions } from '@tanstack/react-query'

export const goodsQueries = {
  list: (kw: string) => queryOptions({
    queryKey: ['goods', { kw }],
    queryFn: () => api.goods({ kw }),
    staleTime: 30_000,
  }),
  detail: (id: string) => queryOptions({
    queryKey: ['goods', 'detail', id],
    queryFn: () => api.goodsDetail(id),
  }),
}
useQuery(goodsQueries.list('手机'))
qc.prefetchQuery(goodsQueries.detail(id))     // 同源定义
qc.invalidateQueries({ queryKey: ['goods'] }) // 前缀失效安全
```
