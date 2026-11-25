---
title: [BLD-040] webpack-dev-server 的原理是什么？express、middleware、websocket 各承担什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-040：webpack-dev-server 的原理是什么？express、middleware、websocket 各承担什么？
**答**：
- wds 本质是一个 express 应用：挂 webpack-dev-middleware，把 webpack 的输出接到"内存文件系统"（memfs），磁盘上不产生 dist。
- HTTP：静态资源请求由 middleware 从内存产物直接响应（快、天然与编译一致）；history fallback、代理（http-proxy-middleware）也在这一层。
- WebSocket：独立 ws 服务，编译完成推送 hash/ok/warnings/errors；客户端 sockjs/ws 客户端按协议处理 HMR 与 live reload。
- 其他职责：热更新文件的 HTTP 响应（.hot-update.json/js 由 runtime 发起，middleware 应答）、托管 HMR runtime 注入（HotModuleReplacementPlugin）。

```javascript
// webpack.config.js：devServer 核心参数对照底层职责
module.exports = {
  devServer: {
    hot: true,                              // ws 推送 + HotModuleReplacementPlugin
    static: { directory: 'public', watch: true },
    compress: true,                         // gzip
    historyApiFallback: true,               // SPA 路由 404 回退 index.html
    client: {
      overlay: { errors: true, warnings: false }, // 编译错误浮层
      reconnect: 3,
    },
    proxy: [{
      context: ['/api'],
      target: 'http://localhost:7001',
      changeOrigin: true,
      pathRewrite: { '^/api': '' },
    }],
    setupMiddlewares(middlewares, devServer) { // 自定义 express 中间件
      devServer.app.get('/health', (_req, res) => res.json({ ok: true }));
      return middlewares;
    },
  },
};
```
