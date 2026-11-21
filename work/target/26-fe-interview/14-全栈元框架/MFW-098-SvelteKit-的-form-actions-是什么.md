---
title: [MFW-098] SvelteKit 的 form actions 是什么？和 Server Action 像不像？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-098：SvelteKit 的 form actions 是什么？和 Server Action 像不像？
**答**：
- form actions 是 SvelteKit 的服务端 mutation 机制：`+page.server.js` 里导出 `actions`（named actions），表单 `method="POST" action="?/create"` 提交到同路由的 action，服务端处理完返回 `fail()/redirect()`。
- 和 Next Server Action 高度同源（都是渐进增强 + POST + 序列化返回）：JS 可用时 `use:enhance` 拦截提交走 fetch 并拿到 result；JS 禁用时退化为原生表单 POST 整页刷新——「无 JS 也能用」是两者的共同设计目标。
- 返回值协议：`fail(400, { errors })` 返回 4xx + 数据（页面内回显）；`redirect(303, path)` 跳转。SvelteKit 的 action 结果（`ActionResult`）不是 React 那种 RSC payload，是纯 JSON。
- 差异：Server Action 可以作为事件处理器直接调用（onClick），form actions 只能挂在表单上——更严格的 web-first 约束。

```js
// +page.server.js
import { fail, redirect } from '@sveltejs/kit';

export const actions = {
  async create({ request, locals }) {
    const form = await request.formData();
    const name = String(form.get('name') ?? '').trim();

    if (!name) {
      return fail(400, { errors: { name: '名称不能为空' }, values: { name } });
    }
    if (!locals.user) return fail(401, { errors: { auth: '请先登录' } });

    const product = await db.product.create({ data: { name, ownerId: locals.user.id } });
    redirect(303, `/products/${product.id}`); // 303：POST 后重定向防表单重提交
  },
};
```

```svelte
<!-- +page.svelte -->
<script>
  import { enhance } from '$app/forms';
  export let data;
  export let form; // action 的返回值（fail 的 data 或 null）
</script>

<form method="POST" action="?/create" use:enhance={() => {
  return ({ update }) => { update({ reset: false }); }; // 保留输入，手动控制更新
}}>
  <input name="name" value={form?.values?.name ?? ''} />
  {#if form?.errors?.name}<p class="err">{form.errors.name}</p>{/if}
  <button disabled={form === undefined}>提交</button>
</form>
```
