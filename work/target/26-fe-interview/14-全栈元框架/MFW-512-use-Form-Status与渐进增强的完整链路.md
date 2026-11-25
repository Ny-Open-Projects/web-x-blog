---
title: [MFW-512] useFormStatus 与渐进增强：无 JS 环境的表单提交链路
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-512：useFormStatus 与渐进增强：无 JS 的表单链路

**答**:
- 渐进增强链路：`<form action={serverAction}>` → SSR 渲染时 action 编译为表单属性（method=POST + hidden 字段携带 action id）——JS 禁用时表单原生提交（服务端处理 action + 重渲染整页）；JS 启用时拦截提交 → fetch 调 action → 局部更新。
- useFormStatus 的语义：必须在 form 内的子组件使用（读取最近祖先 form 的 pending 状态）——无 JS 时无 pending（原生提交，浏览器自带加载态）；「pending UI」是 JS 增强项。
- hidden 字段的绑定协议：formData 序列化（action 的参数从 form 字段取）——`bind` 的参数走 hidden input（`$ACTION_ID_xxx` 与 `$ACTION_KEY`）——「action 参数与表单字段的编码」是渐进增强的协议核心。
- 追问钩子：为什么「无 JS 可用」要作为一等场景而非边缘 case？——1) 首访 JS 未加载（网络慢时用户已可交互——提交不丢）；2) SEO/爬虫；3) 无障碍与脆弱性冗余——渐进增强的价值在「JS 加载失败时网站仍完成核心任务」；RSC 架构把 server 优先做到极致，JS 是增强层——这与 RBL-724 分层产物哲学同源：核心层不依赖增强层。

```javascript
// 渐进增强表单（无 JS 也能提交）
import { submitOrder } from './actions';
export default function OrderForm() {
  return (
    <form action={submitOrder}>                          // SSR: method=POST + hidden action id
      <input name="sku" required />
      <input name="qty" type="number" defaultValue={1} />
      <SubmitButton />
    </form>
  );
}
function SubmitButton() {
  const { pending } = useFormStatus();                   // JS 增强态
  return <button disabled={pending}>{pending ? '提交中…' : '下单'}</button>;
}
// 服务端 action 接收 formData（两形态统一入口）
'use server';
export async function submitOrder(formData) {
  const sku = formData.get('sku');                       // 原生提交与 fetch 提交都走这里
  await db.orders.create({ sku, qty: formData.get('qty') });
  revalidatePath('/orders');
}
```
