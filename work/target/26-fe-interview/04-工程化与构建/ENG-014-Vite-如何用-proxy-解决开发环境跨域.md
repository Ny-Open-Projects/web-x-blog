---
title: [ENG-014] Vite 如何用 proxy 解决开发环境跨域？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-014：Vite 如何用 proxy 解决开发环境跨域？
**答**：
- 浏览器同源策略限制开发时直连后端；dev server 内置 http-proxy 把匹配路径转发到目标服务。
- 前端请求同源的 /api，代理服务器转发到真实后端，响应再透传回来，浏览器认为是同源。
- changeOrigin 修改请求 Host 头；rewrite 重写路径；ws: true 支持 WebSocket。
- 它只存在于开发环境，生产环境由 Nginx 做同样的反向代理。

```javascript
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    proxy: {
      // 前端请求 /api/users -> http://localhost:8080/users
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // WebSocket 代理
      '/ws': {
        target: 'ws://localhost:8081',
        ws: true,
      },
    },
  },
});
```

---

## 第三章 webpack 核心（ENG-015 ~ ENG-021）
