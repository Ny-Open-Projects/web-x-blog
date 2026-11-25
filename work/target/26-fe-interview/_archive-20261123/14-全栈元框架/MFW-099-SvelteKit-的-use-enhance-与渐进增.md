---
title: [MFW-099] SvelteKit 的 use:enhance 做了什么？不用它表单还能用吗？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-099：SvelteKit 的 use:enhance 做了什么？不用它表单还能用吗？
**答**：
- 能用：`<form method="POST" action="?/create">` 不加 enhance 就是原生 HTML 表单，POST 整页提交，服务端 action 照常执行——渐进增强的「基线」是纯 web。
- `use:enhance` 的默认行为：拦截 submit → fetch 提交 → 更新 `form` prop（action 返回值）→ 调用 `invalidateAll()` 让所有 load 重新运行 → 成功后 reset 表单 → 失败在页面内显示。把「整页刷新」变成「局部更新」。
- 自定义回调可以覆盖/扩展默认行为：发乐观更新、按钮 pending 态、局部 invalidate（`applyAction` 手动执行默认逻辑）。
- 对比 Next：Server Action 的渐进增强是框架内置自动的，SvelteKit 需要显式 `use:enhance`——一个隐式一个显式，都要求 action 语义与原生表单兼容（FormData 进、可序列化结果出）。

```svelte
<script>
  import { enhance } from '$app/forms';
  export let form;
  let submitting = false;
</script>

<form
  method="POST"
  action="?/create"
  use:enhance={() => {
    submitting = true;
    return async ({ update, result }) => {
      await update({ reset: false });   // 执行默认更新逻辑
      submitting = false;
      if (result.type === 'success') showToast('创建成功');
      // result.type: 'success' | 'failure' | 'redirect' | 'error'
    };
  }}
>
  <input name="name" />
  <button disabled={submitting}>{submitting ? '提交中…' : '创建'}</button>
</form>

{#if form?.errors?.name}<p>{form.errors.name}</p>{/if}
```
