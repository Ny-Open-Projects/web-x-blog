---
title: [BLD-116] 静态站点预渲染：prerender-spa-plugin 的原理、局限与替代方案。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-116：静态站点预渲染：prerender-spa-plugin 的原理、局限与替代方案。
**答**：
- 原理：构建完成后启动无头浏览器（puppeteer）访问指定路由，等渲染稳定（`renderAfterDocumentEvent`，如 `document.dispatchEvent(new Event('render-event'))`）后抓取 DOM，写回对应路径的 `index.html`——即"把 CSR 的首屏 DOM 固化进 HTML"。
- 产物特性：HTML 内含完整首屏标记 + 原有 bundle，首屏直出、SEO 可收录；JS 加载后 hydration? Vue 是重新挂载（替代而非接管），所以快照数据与运行时数据必须一致，否则闪变。
- 局限：路由数多时构建时间线性上涨（每路由一次浏览器渲染）；动态路由/带鉴权页不适用；产物是"死快照"，数据更新需重新构建。
- 替代：SSR（Nuxt/Next，动态数据）、vite-plugin-ssr? 、react-snap、或 SSG 框架（Astro）；面试要能对比"预渲染 = 构建时 SSG of CSR，SSR = 请求时渲染"。

```javascript
// webpack + prerender-spa-plugin 生产配置
const PrerenderSPAPlugin = require('prerender-spa-plugin');
const Renderer = PrerenderSPAPlugin.PuppeteerRenderer;

module.exports = {
  plugins: [
    new PrerenderSPAPlugin({
      staticDir: path.join(__dirname, 'dist'),
      routes: ['/', '/products', '/products/detail/1', '/about'], // 可枚举的静态路由
      renderer: new Renderer({
        headless: true,
        renderAfterDocumentEvent: 'render-event',   // 与应用内约定：mounted 后 dispatch
        renderAfterTime: 8000,                      // 兜底超时，防止事件未触发挂住构建
        maxConcurrentRoutes: 4,                     // 并发渲染路由数（CI 机器内存内调）
      }),
    }),
  ],
};
// main.js 配合：
// new Vue({ render: h => h(App), mounted() { document.dispatchEvent(new Event('render-event')) } }).$mount('#app')
// 取舍：路由 >50 或数据强动态 → 放弃预渲染走 SSR；
//       纯内容站且路由可枚举 → 预渲染/SSG 成本最低（无服务端）。
```
