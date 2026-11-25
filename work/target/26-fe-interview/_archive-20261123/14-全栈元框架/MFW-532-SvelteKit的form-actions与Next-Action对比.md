---
title: [MFW-532] SvelteKit Form Actions 与 Next Server Actions 的协议对比
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-532：Form Actions vs Server Actions 协议对比

**答**:
- 两者的渐进增强同构：SvelteKit form method="POST" → +page.server.js 的 actions.default/named（原生表单提交 + data 返回）；Next form action={serverAction}（RBL-512）——都是「JS 增强层包原生提交」。
- 协议差异：1) **返回形态**（SK actions 返回 `fail(400, { errors })` 显式失败状态——表单数据保留；Next useActionState 返回值——错误也是返回值）；2) **提交后导航**（SK 的 redirect() 在 action 内；Next 的 redirect 抛控制流异常 RBL-513）；3) **数据回传**（SK：data 自动回传同页；Next：Flight payload 重渲染）。
- SK 的独有细节：action 与 load 同文件（+page.server.js）——「读写同域」（数据获取与变更在一个模块——内聚）；applyAction（client 手动合并 action 结果）。
- 追问钩子：为什么 SK 把 action 与 load 放同一文件而 Next 分离（actions.ts）？——SK 的页面 = 「一个路由的数据读写单元」（load + actions 内聚——CRUD 同域直觉）；Next 的分层 = 「渲染单元（page）与变更单元（action）分离」（action 可跨页面复用）——内聚 vs 复用的组织权衡：表单为主的应用 SK 更顺、跨页复用变更逻辑的应用 Next 更顺。

```svelte
// +page.server.js —— load 与 actions 内聚
export const load = async () => ({ items: await db.items.all() });
export const actions = {
  create: async ({ request }) => {
    const data = await request.formData();
    const title = data.get('title');
    if (!title) return fail(400, { title, missing: true });   // 显式失败 + 数据保留
    await db.items.create({ title });
    return { success: true };                            // redirect(data) 可导航
  },
};
// +page.svelte —— use:enhance（JS 增强）
<script>
  import { enhance } from '$app/forms';
  export let data, form;
</script>
<form method="POST" action="?/create" use:enhance={({ formEl }) => {
  return ({ result, update }) => update({ reset: false });   // 增强层
}}>
  <input name="title" value={form?.title ?? ''} />
  {#if form?.missing}<span class="error">标题必填</span>{/if}
</form>
```
