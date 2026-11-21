---
title: [BLD-138] vite 的 SSR 架构：dev 的 createServer 内存模块执行与 build 的 ssr manifest。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-138：vite 的 SSR 架构：dev 的 createServer 内存模块执行与 build 的 ssr manifest。
**答**：
- dev SSR：`createServer({ server: { middlewareMode: true } })` 暴露 `ssrLoadModule(url)`——**不走网络不走产物**，直接在 Node 里用 ssrTransform 后的模块（把 ESM 转成 `__vite_ssr_import__` 包装，支持 HMR 与缓存失效），请求级实时执行。
- build SSR：`vite build --ssr entry-server.js` 产 Node 可用格式（cjs/esm）；再跑一次 `vite build --ssrManifest` 生成 `ssr-manifest.json`：**源码模块 → 产物 chunk/css 的映射**，服务端渲染时据此知道"这个组件依赖哪些 css/异步 chunk"，实现客户端关键 CSS 与预加载注入。
- 双配置要点：ssr 的 `external`（node_modules 直接 require 不打包）、`resolve.conditions` 加 `ssr`、客户端构建需与 server 共享同一份数据获取逻辑（如 React Query prefetch）。
- 面试对比：SSR manifest 本质是"服务端渲染产物 ↔ 客户端产物"的资源映射协议，与 webpack 的 asset manifest 同构。

```javascript
// vite.config.ts：SSR 双构建配置
export default defineConfig({
  build: {
    ssrManifest: true,        // 产出 dist/.vite/ssr-manifest.json（客户端构建时）
    // SSR 构建（--ssr）时的产物格式：
    ssr: { target: 'node', format: 'esm', external: ['express', 'pino'] },
  },
  resolve: { conditions: process.env.SSR ? ['ssr', 'node'] : [] },
});

// server.js：dev 内存执行 vs build 用产物（同一份 server 代码切换）
import express from 'express';
const app = express();
if (process.env.NODE_ENV === 'development') {
  const { createServer: createViteServer } = await import('vite');
  const vite = await createViteServer({ server: { middlewareMode: true }, appType: 'custom' });
  app.use(vite.middlewares);
  app.get('*', async (req, res) => {
    const { render } = await vite.ssrLoadModule('/src/entry-server.jsx'); // dev：内存模块
    res.send(await render(req.url, vite));
  });
} else {
  app.use(express.static('dist/client'));
  const manifest = (await import('./dist/client/.vite/ssr-manifest.json')).default;
  const template = readFileSync('./dist/client/index.html', 'utf-8');
  const { render } = await import('./dist/server/entry-server.js');      // prod：静态产物
  app.get('*', async (req, res) => {
    const { html, preloadLinks } = await render(req.url, manifest);      // manifest 驱动资源注入
    res.send(template.replace('<!--ssr-outlet-->', html).replace('<!--preload-links-->', preloadLinks));
  });
}
```
