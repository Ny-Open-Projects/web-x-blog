---
title: [ZSM-149] TanStack Query 的 enabled 门控都有哪些玩法？链式依赖和多段取数怎么组织？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-149：TanStack Query 的 enabled 门控都有哪些玩法？链式依赖和多段取数怎么组织？
**答**：
- enabled 四类用法：条件未就绪不发请求（`enabled: !!userId`）、手动模式（enabled: false + refetch() 主动触发，如「保存前预检」）、轮询开关（`enabled: paused === false && autoPoll`）、灰度/特性开关控制取数。
- 链式依赖：qA 数据就绪后 enabled: !!qA.data 才发起 qB；两段以上依然平铺写，不要在 queryFn 里嵌套 await——嵌套会把两段结果绑进一个缓存，任何一段失效都全量重取。
- enabled 变 false 时不会取消已发出的请求，需要硬取消配 `queryClient.cancelQueries`；恢复 true 时数据若 stale 会自动重取。
- 边界：依赖链中下游组件首渲染是 pending 态，UI 要区分「等待上游」与「请求中」（fetchStatus 都会是 idle，用 isPlaceholderData/enabled 判断）。

```javascript
function OrderFlow({ orderId }) {
  // 第一段：订单
  const order = useQuery({
    queryKey: ['order', orderId],
    queryFn: () => api.order(orderId),
  })
  // 第二段：等订单里有 merchantId 才取商家
  const merchant = useQuery({
    queryKey: ['merchant', order.data?.merchantId],
    queryFn: () => api.merchant(order.data.merchantId),
    enabled: !!order.data?.merchantId,        // 门控：上游就绪才发
  })
  // 第三段：手动预检，点按钮才触发
  const precheck = useQuery({
    queryKey: ['precheck', orderId],
    queryFn: () => api.precheck(orderId),
    enabled: false,
  })

  if (!order.data) return <OrderSkeleton/>
  return <Flow order={order.data}
               merchant={merchant.data}
               runPrecheck={() => precheck.refetch()}/>
}
```
