---
title: [MFW-115] Astro Actions 是什么？Astro 怎么处理数据提交？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-115：Astro Actions 是什么？Astro 怎么处理数据提交？
**答**：
- Astro Actions（2.10+ 稳定）：在 `src/actions/index.ts` 定义**类型安全的服务端函数**，客户端像调本地函数一样 `actions.subscribe(input)` 调用（底层 POST RPC），校验、错误结构标准化。定位 ≈ Next Server Actions / SvelteKit form actions。
- 与 API Endpoint 的分工：Actions 面向「表单/mutation」（入参校验 + JSON 结果），Endpoint（`src/pages/api/*.ts`）面向「REST/回调/webhook」。BFF 需求用 Actions，开放 API 用 Endpoint。
- 内置 zod 校验：入参 schema 在服务端执行，客户端 TS 类型自动推导——错误返回 `inputErrors`/`serverError` 结构化对象。
- 表单集成：`<form method="POST" action={actions.subscribe}>` 渐进增强可用，与 SvelteKit form actions 同思路。

```ts
// src/actions/index.ts
import { defineAction, z } from 'astro:actions';

export const server = {
  subscribe: defineAction({
    input: z.object({ email: z.string().email() }),  // 服务端校验
    handler: async ({ email }, context) => {
      if (await db.subscriber.exists(email)) {
        throw new Error('ALREADY_SUBSCRIBED');
      }
      await db.subscriber.create({ data: { email } });
      return { ok: true };
    },
  }),
};
```

```astro
---
// src/pages/newsletter.astro
import { actions } from 'astro:actions';
---
<form method="POST" action={actions.subscribe}>  <!-- 无 JS 也能提交 -->
  <input name="email" type="email" required />
  <button>订阅</button>
</form>

<script>
  // JS 场景：类型安全 RPC
  document.querySelector('form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = { email: new FormData(e.target as HTMLFormElement).get('email') as string };
    const { data, error } = await actions.subscribe(input); // 类型自动推导
    if (error) alert(error.message);
    else alert('订阅成功');
  });
</script>
```
