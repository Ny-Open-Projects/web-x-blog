---
title: [BLD-114] 微前端 qiankun 场景下，主应用与子应用的 webpack 配置清单是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-114：微前端 qiankun 场景下，主应用与子应用的 webpack 配置清单是什么？
**答**：
- 子应用必须：`libraryTarget: 'UMD'`（或 ESMD 支持）、`output.library: packageName`、`output.globalObject: 'window'`、**devServer 开 CORS**（`headers: { 'Access-Control-Allow-Origin': '*' }`），因为 qiankun 用 `import-html-entry` 跨域拉取并 eval 脚本。
- **单实例运行**（qiankun 常规）：CSS 隔离靠 `strictStyleIsolation`（Shadow DOM）或 `experimentalStyleIsolation`（scope 前缀），构建侧无侵入；**多实例**需在构建期给样式加应用前缀（postcss prefix plugin 或 CSS Modules）。
- publicPath 必须运行时动态：qiankun 环境 `__webpack_public_path__ = window.__INJECTED_PUBLIC_PATH_BY_QIANKUN__`，否则子应用资源 404（webpack5 推荐入口首行注入）。
- 主应用：无需 UMD；给 qiankun 容器预留 DOM、配置 `rules` 透传子应用资源；生产建议子应用独立域名 + 网关路由，避免主子同域 cookie 冲突。

```javascript
// ===== 子应用 vue.config / webpack.config.js 关键项 =====
module.exports = {
  output: {
    library: 'sub-app-portal',            // 与注册时 name 一致
    libraryTarget: 'umd',
    chunkLoadingGlobal: 'webpackJsonp__sub-app-portal', // 避免 jsonp 全局数组冲突（多子应用必配）
    globalObject: 'window',
    publicPath: 'auto',                   // webpack5：运行时自动推导，或入口注入 qiankun 变量
  },
  devServer: {
    port: 7101,
    headers: { 'Access-Control-Allow-Origin': '*' }, // qiankun 跨域 fetch 子应用资源
  },
};
// src/main.js 入口（qiankun 生命周期挂载）
import './public-path'; // 首行：__webpack_public_path__ = window.__INJECTED_PUBLIC_PATH_BY_QIANKUN__
export async function bootstrap() {}
export async function mount(props) { props.onGlobalStateChange?.((s) => s); /* render app */ }
export async function unmount() { /* destroy instance */ }

// ===== 主应用 webpack.config.js =====
module.exports = {
  devServer: { port: 7000, historyApiFallback: true },
  module: { rules: [{ test: /\.js$/, exclude: /node_modules/, use: 'babel-loader' }] },
  // 无需 library 配置；注册子应用：
  // registerMicroApps([{ name: 'sub-app-portal', entry: '//localhost:7101',
  //   container: '#subapp', activeRule: '/portal' }]);
};
```
