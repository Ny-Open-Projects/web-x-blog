---
title: [ZSM-148] 怎么封装一层「资源级」useQuery Hook？团队规范该约定哪些硬性条款？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-148：怎么封装一层「资源级」useQuery Hook？团队规范该约定哪些硬性条款？
**答**：
- 目标：业务组件不直接写 queryKey/queryFn，只调 `useGoods(id)` / `useGoodsList(filter)` 这类资源 Hook——key 结构、请求路径、staleTime 全部收敛在一处。
- 必备元素：queryKey 工厂（杜绝手拼）、类型泛型（返回 TS 类型）、统一 staleTime/gcTime 基线（可在资源级覆盖）、错误规范化（HTTP 错转业务错）。
- 硬性条款建议：① 禁止内联 queryFn；② 禁止魔法字符串 key；③ mutation 与其 query 定义放同一文件（失效清单就近维护）；④ queryOptions 工厂复用（094 已考形态，这里考团队规范落地）。
- 追问钩子：能说出「封装层的边界是资源而非页面」——按页面封装会导致同资源多份定义、失效漏项。

```javascript
// api/goods.ts —— 资源级封装
import { queryOptions } from '@tanstack/react-query'

export const goodsKeys = {
  all: ['goods'] as const,
  detail: (id: string) => [...goodsKeys.all, id] as const,
  list: (filter: Filter) => [...goodsKeys.all, 'list', filter] as const,
}

export function goodsDetailOptions(id: string) {
  return queryOptions({
    queryKey: goodsKeys.detail(id),
    queryFn: async () => {
      const res = await api.get(`/goods/${id}`)
      if (!res.ok) throw normalizeError(res)      // 统一错误规范化
      return (await res.json()) as Goods
    },
    staleTime: 60_000,
  })
}

// 业务组件：只认资源 Hook，不知道 key 细节
export function useGoods(id: string) {
  return useQuery(goodsDetailOptions(id))
}

// 失效点与 key 同文件维护：
// queryClient.invalidateQueries({ queryKey: goodsKeys.detail(id) })
```
