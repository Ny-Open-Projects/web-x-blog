---
title: [MFW-057] Next.js 的 rewrites、redirects、headers 配置各适合什么场景？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-057：Next.js 的 rewrites、redirects、headers 配置各适合什么场景？
**答**：
- `redirects`：**URL 变了**，浏览器地址栏更新（301/302），用于旧路径迁移、SEO 权重转移。
- `rewrites`：**URL 没变**，服务端内部转发到另一条路由或外部地址，用于 BFF 代理、灰度切流、屏蔽后端真实路径。
- `headers`：统一注入响应头，安全头（CSP/HSTS）、缓存策略都在这里收口。
- 三者都在 `next.config.js` 构建期固化，需要运行时条件判断（按 cookie/geo 分流）就升级到 Middleware。
- 顺序：headers 先应用，redirects 优先于 rewrites，rewrites 按 beforeFiles/afterFiles/filesystem 三阶段匹配。

```js
// next.config.js
module.exports = {
  async redirects() {
    return [
      { source: '/p/:id', destination: '/products/:id', permanent: true }, // 301 迁移
    ];
  },
  async rewrites() {
    return {
      beforeFiles: [
        // 灰度：命中实验 cookie 的用户内部转发到新版本路由，URL 不变
        { source: '/checkout', has: [{ type: 'cookie', key: 'exp', value: 'new' }], destination: '/checkout-v2' },
      ],
      afterFiles: [
        // BFF 代理：前端统一走 /api，后端地址不暴露
        { source: '/api/:path*', destination: 'https://internal-api.example.com/:path*' },
      ],
    };
  },
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          { key: 'X-Frame-Options', value: 'DENY' },
          { key: 'Strict-Transport-Security', value: 'max-age=63072000' },
        ],
      },
    ];
  },
};
```
