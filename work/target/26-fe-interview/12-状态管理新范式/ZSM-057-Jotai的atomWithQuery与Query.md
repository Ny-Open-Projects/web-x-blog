---
title: [ZSM-057] Jotai 的 atomWithQuery / atomWithSuspenseQuery 是什么？和直接用 TanStack Query 有什么区别？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-057：Jotai 的 atomWithQuery / atomWithSuspenseQuery 是什么？和直接用 TanStack Query 有什么区别？
**答**：
- atomWithQuery：把 TanStack Query 包成异步 atom，`atomWithQuery(get => ({ queryKey, queryFn }))`，依赖 atom 变化自动换 key 重请求；read 返回 Promise，配 Suspense。
- 本质上仍是 Query 的缓存引擎（gcTime/staleTime/失效机制都在），Jotai 只是「订阅面」换成了 atom 风格。
- 区别：组件树里没有 queryClient hook 的消费点，适合「状态视角」占主导、查询分散派生链的场景；但 devtools、SSR dehydrate/hydrate、乐观更新的官方支持都在 Query hook 侧更顺。
- 选型建议：项目主用 TanStack Query 时不要为了一两个页面引入 atomWithQuery，双 API 心智成本大于收益。

```javascript
import { atomWithQuery } from 'jotai-tanstack-query'

const keywordAtom = atom('')
const goodsAtom = atomWithQuery(get => ({
  queryKey: ['goods', get(keywordAtom)],   // 依赖 atom 自动进 key
  queryFn: ({ queryKey }) => fetchGoods(queryKey[1]),
}))
function List() {
  const goods = useAtomValue(goodsAtom) // Suspense 自动接管 loading
}
```
