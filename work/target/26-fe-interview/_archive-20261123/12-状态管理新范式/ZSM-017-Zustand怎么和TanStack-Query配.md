---
title: [ZSM-017] Zustand 和 TanStack Query 怎么配合？哪些状态该放进 Zustand？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-017：Zustand 和 TanStack Query 怎么配合？哪些状态该放进 Zustand？
**答**：
- 分工：Query 管「服务端状态」（数据、缓存、loading/错误、失效重取），Zustand 只放「客户端状态」（UI 态、表单草稿、筛选条件、用户偏好）。
- 常见反模式：把接口返回的数据 copy 进 Zustand——等于绕过缓存造成双源，之后失效/重取全部失灵。
- 正确配合姿势：筛选条件放 Zustand → queryKey 依赖它自动重新请求；Mutation 成功后用 `queryClient.invalidateQueries` 而不是手动把结果写进 store。
- 例外：只有当数据要跨页面长期持有且与请求生命周期解耦（如购物车本地合并、离线清单）才考虑 store 持有。

```javascript
const useFilter = create(set => ({ keyword: '', setKeyword: k => set({ keyword: k }) }))

function GoodsList() {
  const keyword = useFilter(s => s.keyword)
  // keyword 变化 → queryKey 变化 → 自动重新请求，数据只活在 Query 缓存里
  const { data } = useQuery({
    queryKey: ['goods', keyword],
    queryFn: () => fetchGoods(keyword),
  })
  // 禁止：useCartStore.setState({ goods: data }) ← 双源反模式
}
```
