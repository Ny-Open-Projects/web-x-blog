---
title: [V3-065] Vue SSR 的原理与优缺点是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-065：Vue SSR 的原理与优缺点是什么？
**答**：
- 服务端用 renderToString 把组件渲染成 HTML 字符串直接返回，首屏无需等待 JS 执行。
- 客户端 createSSRApp 挂载时不重建 DOM，而是 hydration"激活"已有 DOM 并接管事件。
- 优点：首屏快、SEO 友好；代价：服务器压力、开发约束增加（生命周期只执行部分、注意内存泄漏）。
- window/document 等浏览器 API 必须放在 onMounted 或客户端分支中访问。

```typescript
// SSR 核心流程：服务端 renderToString 生成 HTML -> 客户端 hydration 激活
import { createSSRApp } from "vue";
import { renderToString } from "vue/server-renderer";

function createAppInstance() {
  return createSSRApp({
    data: () => ({ count: 1 }),
    template: `<button @click="count++">{{ count }}</button>`,
  });
}

// 服务端：只执行一次，输出首屏 HTML
const html = await renderToString(createAppInstance());

// 客户端：createSSRApp + 挂载时不再重建 DOM，而是激活已有 DOM
// 注意：服务端每个请求要新建 app 实例，避免跨请求状态污染
// onMounted / onBeforeMount 只在客户端执行，浏览器 API 写在这些钩子里
```
