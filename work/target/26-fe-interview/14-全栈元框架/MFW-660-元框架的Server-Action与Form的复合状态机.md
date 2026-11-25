---
title: [MFW-660] Server Action 与 Form 的复合状态机
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-660：Action 与 Form 的复合状态机

**答**:
- 表单提交的状态机：idle → submitting(pending) → success（redirect/更新）| error（返回错误）| redirect（导航离开）——useActionState 的状态封装（RBL-513）；「复合表单」的多步状态机：step1 → step2 → submit（多步表单的 state 演进——每步的 action 调用（部分保存）+ 最终提交）。
- 状态机的一致性约束：1) **pending 的互斥**（同 form 的并发提交禁止（disabled pending）——双击防重复 RBL-567；2) **redirect 的终态**（redirect 后 pending 清理——导航是终态（后续状态无意义）；3) **乐观与真值的交接**（乐观值在 action resolve 后被真值替换——交接点的 race RBL-580）。
- 多步表单的 state 持久化：step 间数据保存（formData 传递/隐藏字段/URL state——多步的渐进增强（每步都是独立 form action——server 侧 step 状态机））。
- 追问钩子：为什么「多步表单」在 Server Action 架构下要重新设计（vs 传统 SPA）？——传统 SPA：client state 管理多步（state 在内存——刷新丢）；Server Action：每步提交 = server 保存（DB draft——刷新不丢）；渐进增强（每步原生提交可用）；「多步的 state 归属」：从 client state 转为 server draft（每步持久化）——架构的转变让「用户中断恢复」成为默认能力（step3 刷新回来 step1-2 数据还在——server draft）。

```tsx
// 多步表单的 server 状态机
'use server';
export async function saveStep1(formData: FormData) {
  const draftId = formData.get('draftId') ?? crypto.randomUUID();
  await db.drafts.upsert(draftId, { step: 1, ...extract(formData) });
  return { draftId, nextStep: 2 };                       // 返回 draftId：client 传递
}
export async function submitFinal(formData: FormData) {
  const draft = await db.drafts.find(formData.get('draftId'));
  await db.orders.create(draft);                         // 最终提交
  revalidateTag('orders');
  redirect('/orders');                                   // 终态：导航
}
// client 多步组件
'use client';
function MultiStepForm() {
  const [state, action] = useActionState(saveStep1, null);
  const [step, setStep] = useState(1);
  return step === 1
    ? <form action={async (fd) => { const s = await action(fd); setStep(s.nextStep); }}>...</form>
    : <FinalStep draftId={state?.draftId} />;
}
// 状态机：step1.save → step2.submit → redirect（终态）
```
