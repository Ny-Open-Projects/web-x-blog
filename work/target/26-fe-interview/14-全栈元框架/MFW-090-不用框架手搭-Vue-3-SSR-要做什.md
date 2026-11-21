---
title: [MFW-090] 不用框架，手搭一个 Vue 3 SSR 应用要做哪些事？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-090：不用框架，手搭一个 Vue 3 SSR 应用要做哪些事？
**答**：
- 五件套：① 双入口构建（server bundle + client manifest）；② 服务端 `renderToString` 输出 HTML；③ 状态/数据**脱水**（`pinia.state.value` 序列化进 `window.__INITIAL_STATE__`）；④ 客户端 `createSSRApp` 复水；⑤ 路由与请求上下文（每请求新建 app/router 实例，防全局状态串请求）。
- 框架替你做的事就清楚了：路由代码分割、数据预取约定（Nuxt 的 useAsyncData）、HMR、manifest 与预加载资源注入、部署适配。手搭一遍是理解元框架价值的最好方式。
- 高频坑：每请求必须全新 app 实例（单例状态会跨用户泄漏）；`renderToString` 不含异步等待，异步组件需 `ssrManifest`/手动 await；样式提取要 vite ssrManifest 配合。

```js
// server.js —— 极简 Vue3 SSR（Express）
const { createSSRApp } = require('vue');
const { renderToString } = require('vue/server-renderer');
const { createPinia } = require('pinia');
const { buildApp } = require('./app'); // 工厂：每请求新实例

const express = require('express');
const server = express();

server.get('*', async (req, res) => {
  const { app, router, pinia } = buildApp(req.url); // ① 每请求新 app/pinia
  await router.push(req.url);
  await router.isReady();

  let html = '';
  try {
    html = await renderToString(app);               // ② SSR 渲染
  } catch (e) {
    return res.status(500).send('server error');
  }

  // ③ 脱水：把 pinia 状态注入 HTML
  const state = `window.__INITIAL_STATE__=${JSON.stringify(pinia.state.value)}`;
  res.send(`<!DOCTYPE html><html><body><div id="app">${html}</div>
    <script>${state.replace(/</g, '\\u003c')}</script>  <!-- 防 </script> 注入 -->
    <script type="module" src="/client-entry.js"></script></body></html>`);
});

server.listen(3000);
```

```js
// client-entry.js —— ④ 复水
import { buildApp } from './app';
const { app, pinia } = buildApp(window.location.pathname);
if (window.__INITIAL_STATE__) pinia.state.value = window.__INITIAL_STATE__; // 复水
app.mount('#app'); // 挂载即 hydration
```
