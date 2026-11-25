---
title: [ZSM-636] useMutation 的并发调用隔离：多次 mutate 的状态竞争与 isPaused
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-636：useMutation 的并发调用隔离：多次 mutate 的状态竞争与 isPaused

**答**：
- 与 useQuery「共享 Query 实例」相反，**每次 mutate() 调用创建独立的 Mutation 实例**——各自有自己的 state（variables/status/data），所以两次快速点击 mutate 会产生两条并行的 mutationFn 执行，onSuccess 各自回调。useMutation hook 返回的 state 是「最后一次 mutate 的状态」，这就是并发下 UI 显示抖动的根源。
- 竞态处理手段：1) `scope: { id }`（v5）——同 scope 排队串行执行；2) 回调层防护——onSuccess 里比对 `variables` 是否还是当前 UI 关注的（防止旧 mutation 回调更新已被改的 UI）；3) 组件层 disable（按钮 loading）或事务化（ZSM-542 幂等键）。
- `isPaused` 与 networkMode：mutation 在 offline 时进入 paused 状态（状态保持 pending+paused），onlineManager 恢复后自动重发——这就是「离线也能点提交」的实现基础，恢复顺序按提交时间。
- mutation 生命周期清理：MutationCache 按 gcTime 清理已完成的 mutation 实例（默认 5 分钟）；`mutationCache.clear()` 全清。
- 追问钩子：`mutateAsync` 返回 Promise（可 await 做流程编排），`mutate` 不返回（回调式，无 unhandled rejection 风险）——表单提交链路用 mutateAsync 记得 catch，否则未处理 rejection。

```javascript
// 并发 mutate 的隔离示例
const { mutate, mutateAsync, data, variables } = useMutation({ mutationFn: updateItem })

mutate({ id: 1, qty: 2 })     // Mutation 实例 A
mutate({ id: 1, qty: 5 })     // Mutation 实例 B（并行！）
// 两次都会执行、各自 onSuccess；hook 的 data 是最后完成者的结果
// 防御：scope 串行
const { mutate: scopedMutate } = useMutation({ mutationFn: updateItem, scope: { id: 'item-1' } })

// mutateAsync 编排 + 错误处理
async function checkout() {
  try {
    const order = await mutateAsync({ items: cart.items })   // await 完成才走下一步
    router.push(`/orders/${order.id}`)
  } catch (e) {
    toast.error(e.message)
  }
}

// 离线暂停：paused 状态 UI
const { isPaused } = useMutation({ mutationFn: save, networkMode: 'offlineFirst' })
// networkMode: 'offlineFirst' → 离线先试本地一次失败后 pause
// 恢复：onlineManager 发 online 事件 → MutationCache 重放 paused 队列（按 submittedAt 排序）
```
