---
title: [MFW-513] Server Action 的错误处理与乐观更新回滚协议
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-513：Server Action 错误处理与乐观更新回滚协议

**答**:
- 错误传播的三层：1) **预期错误**（useActionState 返回——action 返回 { error } 而非 throw：可序列化、UI 可展示）；2) **非预期错误**（throw → error boundary——Next 的 error.tsx；生产环境剥离堆栈只传 message）；3) **重定向**（redirect() 抛特殊错误被框架拦截——在 try/catch 里要重抛 RBL-914 的「框架控制流异常」）。
- 乐观更新回滚协议：useOptimistic 的状态在 action 成功后被 server 返回值/revalidate 替换，失败时自动回滚到基线——「乐观值 → 真值」的切换点是 action 的 resolve；失败回滚是框架保证。
- 回滚的边界：乐观 UI 的「部分成功」（批量操作 3 条成功 2 条失败）——乐观更新是全有全无模型，部分成功要手动管理（pending 列表 + 逐条确认）。
- 竞态：连续两次提交的乐观值覆盖（第二次的乐观基线含第一次的乐观值——顺序敏感）；框架按提交序处理，UI 侧要防重复提交（disable/pending）。
- 追问钩子：为什么预期错误用「返回值」而不是「throw」？——throw 会落到 error boundary（整页/整段错误 UI——过度反应：表单校验失败只需行内提示）；返回值让错误成为「数据」（useActionState 精确渲染）——「错误分级」决定传播通道：业务错误是数据、系统错误是异常（与 RBL-568 诊断分级同构）。

```javascript
// 分层错误处理 + 乐观回滚
'use server';
export async function addToCart(formData) {
  const item = JSON.parse(formData.get('item'));
  const valid = await validateItem(item);
  if (!valid.ok) return { error: valid.reason };         // 预期错误：返回值
  await db.cart.add(item);                               // 非预期错误：throw → error.tsx
  revalidateTag('cart');
  return { ok: true, cartCount: await db.cart.count() };
}
// client 侧
function AddToCart({ item }) {
  const [state, formAction] = useActionState(addToCart, null);
  const [optimistic, addOptimistic] = useOptimistic(
    cartCount, (cur, delta) => cur + delta);
  return (
    <form action={async (fd) => {
      addOptimistic(1);                                  // 乐观 +1
      await formAction(fd);                              // 失败自动回滚
    }}>
      <span>购物车: {optimistic}</span>
      {state?.error && <p role="alert">{state.error}</p>}
      <button>加入购物车</button>
    </form>
  );
}
```
