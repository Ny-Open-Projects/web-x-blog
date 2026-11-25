---
title: [V3-251] Vue SSR 的 renderToString 内部流程是怎样的？与客户端渲染路径差在哪？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-251：Vue SSR 的 renderToString 内部流程是怎样的？与客户端渲染路径差在哪？
**答**：
- 入口：`createSSRApp` 打上 SSR 标记，render 走 `ssrRender` 分支（编译器双产物之一），而不是客户端 render。
- 核心循环：组件 setup → 拿模板编译的 ssrRender 函数 → 直接向缓冲区 `_push` 拼 HTML 字符串，遇到子组件递归、遇到列表 `ssrRenderList` 展开。
- 无 DOM 副作用：SSR 分支跳过所有 DOM 操作、事件绑定、Transition/Teleport 真实挂载（Teleport 输出到 teleports 缓冲）。
- 无响应式订阅：服务端渲染**不建立 effect 依赖**，track 被关闭（无后续交互），数据变化靠重新请求。
- 产物：返回完整 HTML 字符串（含 `<!--[-->/<!--]-->` 注释锚点 + data-v 作用域 + 水合所需数据 payload 由框架注入）。

```javascript
import { createSSRApp, renderToString } from 'vue';
import { createRouter, createMemoryHistory } from 'vue-router';
export async function render(url) {
  const app = createSSRApp(Root);
  const router = createRouter({ history: createMemoryHistory(), routes });
  app.use(router);
  await router.push(url); await router.isReady(); // 路由级数据就绪
  const ctx = { teleports: {}, modules: [] };
  const html = await renderToString(app, ctx);     // 同步渲染为字符串
  return { html, teleports: ctx.teleports };       // teleports 单独注入弹窗容器
}
```
