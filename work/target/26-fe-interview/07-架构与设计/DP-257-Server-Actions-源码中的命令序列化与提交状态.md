---
title: [DP-257] 源码识别：Server Actions 源码中的命令与提交状态机？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-257：源码识别：Server Actions 源码中的命令与提交状态机？
**答**:
- 命令序列化：Server Action 把服务端函数引用序列化为 action ID——客户端调用 = 发送命令（id+参数），服务端解释执行；本质是 RPC 命令模式的框架内建。
- 状态机：useActionState 的提交状态（idle → pending → success/error）内建；form action 与 fetch 两条提交路径同状态机。
- 乐观更新组合：useOptimistic 在命令发往服务端前插入本地视图（回滚由 transition 机制自动处理）。
- 识别要点：能说清"Action 的安全边界"——它不是 REST 端点而是框架私有协议（POST + 特殊头），鉴权要显式在 action 里做。

```tsx
// Server Action 命令流（心智模型）
// client: <form action={createOrder}>  →  POST /page?_rsc=... header: Next-Action: <actionId>
// server: registry[actionId](formData)  →  RSC payload 返回 → 客户端 reconcile
'use server';
async function createOrder(formData) {
  const user = await auth();                    // 鉴权必须显式（不是自动端点保护）
  const order = await db.order.create({ data: { ...parse(formData), userId: user.id } });
  revalidatePath('/orders');                    // 缓存失效命令
  return { ok: true };
}
// client 状态机：
const [state, formAction, pending] = useActionState(createOrder, { ok: false });
const [optimistic, addOptimistic] = useOptimistic(state);   // 乐观视图（回滚内建）
```
