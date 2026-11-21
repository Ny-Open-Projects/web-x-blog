---
title: [RBL-012] Rspack 的 HMR 与 dev server 是如何工作的？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-012：Rspack 的 HMR 与 dev server 是如何工作的？
**答**：
- dev server 用 @rspack/dev-server（webpack-dev-server 的 fork），保留 proxy、historyApiFallback、静态目录等能力，底层编译器换成 Rspack。
- watch 增量：文件变更→Rust 侧失活对应模块缓存→只重建受影响的子图→产出 hot-update chunk（*.hot-update.js/json），流程与 webpack HMR 语义一致。
- 推送通道：dev server 通过 WebSocket 通知浏览器拉取 update chunk，runtime 里 manifest/hash 校验后 apply，accept 链路（module.hot.accept）沿用 webpack HMR API。
- 速度来源：增量编译在 Rust 内完成，模块失活判定与重编译并行，不经过 JS 事件循环；配合内存缓存，1s 内 hot update 是常态。
- 配置注意：devServer.hot: true、experiments.css 的热更新由内置处理，不需要 style-loader 专属 hot 逻辑。
- 追问钩子：大文件（如几十万行的 JSON/图标）变更会放大失效范围，应放在外部数据源而不是进打包图。

```javascript
// rspack.config.js 开发配置
module.exports = {
  mode: 'development',
  devtool: 'cheap-module-source-map',
  devServer: {
    hot: true,
    port: 3000,
    historyApiFallback: true,
    proxy: { '/api': { target: 'http://localhost:8080', changeOrigin: true } },
  },
  // 业务侧 HMR 接口与 webpack 一致
  // if (import.meta.webpackHot) {
  //   import.meta.webpackHot.accept('./App', () => render());
  // }
};
```
