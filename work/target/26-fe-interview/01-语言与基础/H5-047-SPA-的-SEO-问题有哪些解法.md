---
title: [H5-047] SPA 的 SEO 问题有哪些解法？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-047：SPA 的 SEO 问题有哪些解法？
**答**：
- 根因：CSR 首屏 HTML 几乎是空壳，爬虫若不执行 JS 就拿不到内容；即使能执行，渲染等待与配额也吃亏。
- 解法：SSR（服务端直出 HTML）、SSG/预渲染（构建期生成静态页）、动态渲染（对爬虫 UA 返回预渲染内容，仅作过渡）。
- SPA 内必须做：每条路由独立 title/meta（history 模式 + 语义 URL）、语义化标签与可访问名称、sitemap、`<a>` 真实 href 而非纯 JS 跳转。
- 衡量工具：Search Console 的网址检查、Lighthouse SEO 项。

```javascript
// 路由切换时维护文档头（SPA 内的 SEO 基本盘）
const SEO = {
  '/': { title: '首页 - 示例商城', desc: '精选好物每日上新' },
  '/products': { title: '全部商品 - 示例商城', desc: '浏览全部商品分类' },
};

function updateSEO(path) {
  const meta = SEO[path];
  if (!meta) return;
  document.title = meta.title;

  let desc = document.querySelector('meta[name="description"]');
  if (!desc) {
    desc = document.createElement('meta');
    desc.name = 'description';
    document.head.appendChild(desc);
  }
  desc.content = meta.desc;
}

// 预渲染示例：vite-plugin-prerender 在构建期为每条路由产出静态 HTML
// vite.config.js
// import prerender from 'vite-plugin-prerender';
// export default {
//   plugins: [
//     prerender({
//       routes: ['/', '/products', '/products/1'], // 爬虫直接拿到完整 HTML
//     }),
//   ],
// };
```

## 十、无障碍与离线应用
