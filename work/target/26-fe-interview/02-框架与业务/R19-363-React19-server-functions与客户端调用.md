---
title: [R19-363] React19 Server Functions：客户端调用与序列化边界
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 全栈]
type: 面试题
---

## R19-363：React19 Server Functions：客户端调用与序列化边界

**答**：
- Server Function（'use server'）：编译为「RPC 端点引用」——客户端拿到的是函数引用（序列化的 ID），调用即发 POST 请求
- 序列化边界：参数与返回值走 React Flight 序列化——支持 Promise/Map/Set/Date/循环引用，不支持函数/类实例/DOM——「能传什么」是设计 API 的第一约束
- 与 Action 结合：`<form action={serverFn}>` 表单提交 + useActionState——渐进增强（无 JS 也能提交，form action 原生语义）
- 安全模型：server fn 是公开 HTTP 端点——所有参数都是「客户端可控输入」，必须校验（zod）+ 权限检查；「以为只有前端能调」是安全误区
- 重验证（revalidation）：server fn 内 revalidatePath/revalidateTag——失效缓存触发重新渲染，客户端自动接收新 UI 流

```jsx
// server.ts
'use server';
export async function createOrder(fd: FormData) {
  const data = OrderSchema.parse(Object.fromEntries(fd));   // 必须校验
  await checkAuth();                                        // 必须鉴权
  await db.orders.create(data);
  revalidatePath('/orders');
}
// client.tsx
<form action={createOrder}> <input name="sku" /> </form>    // 渐进增强
```
