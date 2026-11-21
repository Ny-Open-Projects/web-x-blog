---
title: [BLD-043] React 和 Vue 的 HMR 边界如何处理？react-refresh 与 vue-loader 的 HMR API 是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-043：React 和 Vue 的 HMR 边界如何处理？react-refresh 与 vue-loader 的 HMR API 是什么？
**答**：
- react-refresh（Fast Refresh）：babel 插件在编译期给每个组件模块注入热更新注册代码，运行时 refresh runtime 对比组件类型：组件文件更新 → 保留 state 重渲染；非组件导出被修改 → 边界失效，冒泡到入口整页刷新（如路由配置、context 定义变化）。
- vue-loader（SFC）：每个 SFC 编译成 template/script/style 三个子模块，分别 hot accept——改 template 只重渲染、改 style 只换样式、改 script 触发组件实例重载（Vue 2 通过 data 保留，Vue 3 的 defineComponent 保留 setup 内状态有限）。
- 边界共同点：改"副作用型导出"（全局注册、provide、store 定义）无法安全热替换，需要人工 accept 或刷新。
- 面试表达："框架 HMR 的本质是把 module.hot.accept 的样板代码编译期自动生成，并把替换粒度细化到组件。"

```javascript
// react-refresh 编译产物核心逻辑（简化）
import { register, performReactRefresh } from '@pmmmwh/react-refresh-webpack-plugin/runtime';

// babel 已把 App 注册进 refresh 家族表
const prevType = register(App, 'App'); // 记录组件类型签名

if (module.hot) {
  module.hot.accept('./App', () => {
    // 模块更新后 react-refresh 比对组件类型
    const NextApp = require('./App').default;
    if (isReactComponentBoundary(NextApp)) {
      performReactRefresh(); // 保留 hooks state 局部重渲染
    } else {
      module.hot.invalidate(); // 非组件边界变化 冒泡刷新
    }
  });
}

// webpack.config.js：完整 Fast Refresh 配置
module.exports = {
  module: { rules: [{
    test: /\.[jt]sx?$/,
    exclude: /node_modules/,
    use: [{
      loader: 'babel-loader',
      options: { plugins: [require.resolve('react-refresh/babel')] },
    }],
  }] },
  plugins: [new (require('@pmmmwh/react-refresh-webpack-plugin'))()],
  devServer: { hot: true },
};
```
