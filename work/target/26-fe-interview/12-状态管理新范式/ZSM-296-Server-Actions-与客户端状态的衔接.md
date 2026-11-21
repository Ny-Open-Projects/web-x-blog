---
title: [ZSM-296] Server Action 写完后客户端状态怎么衔接
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-296：Server Action 写完后客户端状态怎么衔接

**答**:
- 衔接三式：Action 返回最新数据直接 setQueryData（免一轮 refetch）；revalidatePath/Tag 触发 RSC 重渲染（服务端组件数据自动新）；客户端 Query 缓存 invalidate（客户端数据源刷新）
- 顺序敏感：乐观更新 → Action → 确认落缓存/回滚；Action 内部再发请求会绕过 Query 缓存去重，重复请求要靠 Action 参数幂等
- 状态归属判断：RSC 树上的数据交给 revalidate；客户端组件消费的跨页数据交给 Query；纯客户端临时态交给 Zustand/Jotai——三者边界清晰才不打架
- 错误衔接：Action 抛错要被客户端 catch 并呈现（useActionState/ErrorBoundary），不能静默吞掉导致 UI 与服务端不一致

```javascript
const action = async (formData) => {
  'use server'
  const order = await createOrder(formData)
  revalidatePath('/orders')                       // RSC 数据刷新
  return { ok: true, order }                       // 返回给客户端
}
// 客户端
const [state, formAction] = useActionState(action, null)
useEffect(() => { if (state?.ok) {
  qc.setQueryData(['order', state.order.id], state.order)   // 直接落缓存
  qc.invalidateQueries({ queryKey: ['orders'] })
} }, [state])
```
