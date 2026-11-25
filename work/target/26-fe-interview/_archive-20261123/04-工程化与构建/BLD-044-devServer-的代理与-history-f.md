---
title: [BLD-044] devServer 的代理与 history fallback 怎么配？有哪些容易踩的坑？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-044：devServer 的代理与 history fallback 怎么配？有哪些容易踩的坑？
**答**：
- historyApiFallback：SPA 直接访问 /user/123 时服务器 404 → 回退 index.html；rewrites 可按前缀区分多应用；开启后静态目录里同名文件优先于 fallback。
- proxy 基于 http-proxy-middleware：changeOrigin 改 Host 头、secure 处理自签证书、cookieDomainRewrite 处理会话、bypass 让部分请求走静态。
- 坑一：代理目标也是 webpack 服务时 ws 需 ws: true（HMR websocket 转发）；坑二：pathRewrite 顺序在 changeOrigin 之前匹配；坑三：/api 与静态资源路径冲突要先配精确的。
- 生产等价物：nginx 的 try_files fallback + upstream 代理，dev 配置要能平滑映射到生产。

```javascript
// webpack.config.js：代理与 fallback 完整配置
module.exports = {
  devServer: {
    historyApiFallback: {
      disableDotRule: true,
      rewrites: [
        { from: /^\/admin/, to: '/admin.html' },
        { from: /^\/portal/, to: '/portal.html' },
        { from: /./, to: '/index.html' },
      ],
    },
    proxy: {
      '/api': {
        target: 'http://backend.internal:7001',
        changeOrigin: true,
        secure: false,                        // 自签证书
        ws: true,                             // 转发 websocket
        cookieDomainRewrite: 'localhost',
        pathRewrite: { '^/api': '' },
        onProxyRes(proxyRes) {                // 响应钩子 调试头
          proxyRes.headers['x-proxy'] = 'wds';
        },
      },
    },
  },
};
```
