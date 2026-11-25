---
title: [MFW-178] Server Actions、SvelteKit form actions、Astro Actions 三方对比？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-178：Next 的 Server Actions、SvelteKit 的 form actions、Astro 的 Actions 三方对比？
**答**：
- 共同心智：都是「服务端函数即端点」，表单原生提交可用（渐进增强），框架负责序列化与调用，省掉手写 REST 端点。
- Next Server Actions：绑定 React 生态，与 RSC/缓存系统（revalidate）深度联动，可以在任意组件上引用；支持 `useActionState`/`useOptimistic` 等客户端协议，但只服务 React。
- SvelteKit form actions：是路由的一部分（`+page.server.js` 的 `actions`，按命名 action 分发），数据流是「提交 → redirect/返回 data → load 重跑」，与 Svelte 的页面状态天然整合，也带 CSRF 校验（origin 检查）。
- Astro Actions：面向内容站+少量交互的形态，配合 Server Islands 使用；输入校验内置（标准 schema 校验），但不承担重交互页面的复杂状态更新。
- 选型差异点：错误回显方式（Next 走 state 返回，SvelteKit 走 `form` prop、Astro 走 ActionError）、CSRF 防护（SvelteKit/Astro 默认开启，Next 靠 POST origin 校验）、与各自缓存/失效系统的耦合深度。

```javascript
// SvelteKit: +page.server.js —— 命名 action
export const actions = {
  login: async ({ request, cookies }) => {
    const data = await request.formData();
    const user = await login(String(data.get('email')), String(data.get('password')));
    cookies.set('session', user.token, { httpOnly: true, path: '/' });
    return { success: true }; // 触发同页 load 重跑，form prop 更新
  },
};
```