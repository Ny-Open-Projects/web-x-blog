---
title: [ZSM-827] React 19 的表单 Actions：useActionState 之后的表单状态架构
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-827：React 19 的表单 Actions：useActionState 之后的表单状态架构

**答**：
- React 19 的 `<form action={fn}>` + `useActionState(fn, initialState)` 把表单提交状态（pending/result）框架化：action 函数签名 `(prevState, formData) => Promise<newState>`，返回值成为新的 state，`isPending` 由框架管理。表单不再需要手写 submitting 状态机（ZSM-542 的 phase 三态被框架接管）。
- 状态架构的变化：**「提交协议」上移到框架**——幂等键、错误态、乐观值（useOptimistic）各归其位：幂等键仍要自己管（框架不管重复提交的资损语义），错误态进 useActionState 的返回值，字段级校验仍用受控组件或 ZSM-534 引擎。
- `useFormStatus`（子组件读取父 form 的 pending）——按钮 loading 态不再需要 prop 透传或 store 订阅，「提交中」的 UI 状态就近获取。
- 仍然要手写的部分：1) 重入防护——form action 默认可重复触发（双击仍需 disabled/idempotency key）；2) 跨步骤表单向导——多 form 编排还是 ZSM-533 的状态机；3) 文件上传进度——action 是一次性的，分片进度仍要自定义。
- 追问钩子：useActionState 与 TanStack mutation 的选型——form 语义（submit → state）用 action，数据变更语义（改了要失效别的查询）用 mutation + invalidate；两者可混用但同一条链路别混。

```javascript
'use client'
import { useActionState, useFormStatus } from 'react'

// Server Action：prevState + formData → newState
async function submitOrder(prev, formData) {
  'use server'
  const idemKey = formData.get('idemKey')            // 幂等键仍自己管
  const res = await createOrderServer(formData, idemKey)
  if (!res.ok) return { ...prev, error: res.message, ok: false }
  return { error: null, orderId: res.orderId, ok: true }
}

function CheckoutForm() {
  const [state, action, isPending] = useActionState(submitOrder, { error: null, ok: false })
  return (
    <form action={action}>
      <input name="address" />
      <input type="hidden" name="idemKey" value={useIdemKey()} />
      <SubmitButton />
      {state.error && <p role="alert">{state.error}</p>}
    </form>
  )
}

// 子组件就近读取 pending（替代 prop 透传）
function SubmitButton() {
  const { pending } = useFormStatus()
  return <button type="submit" disabled={pending}>{pending ? '提交中…' : '提交'}</button>
}

// 仍然手写的部分：
// ① 幂等键生命周期（框架不管资损语义）② 向导多步编排（533 状态机）
// ③ 分片上传进度 ④ 全局乐观（跨组件 → store 层）
```
