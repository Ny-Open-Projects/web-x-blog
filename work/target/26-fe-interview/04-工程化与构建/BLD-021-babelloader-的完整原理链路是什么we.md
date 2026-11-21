---
title: [BLD-021] babel-loader 的完整原理链路是什么？webpack 如何与 babel 协作？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-021：babel-loader 的完整原理链路是什么？webpack 如何与 babel 协作？
**答**：
- 链路：webpack 命中规则 → babel-loader 收到源码 → @babel/core 的 transformAsync → parser（@babel/parser）生成 AST → 遍历（@babel/traverse）套用 plugins/presets（preset-env 含语法降级与 polyfill 注入）→ generator（@babel/generator）生成目标代码 + sourceMap。
- babel-loader 只做"胶水"：管理 cacheDirectory（基于文件 mtime、babel 配置、babel 版本的哈希缓存）、并发调用 @babel/core、传递 sourceMap 上下游。
- preset-env 的 targets/browserslist 决定编译程度；useBuiltIns: 'usage' 按需注入 core-js import。
- 关键点：babel 处理语法（syntax）靠 plugin，处理 API（Promise、Array.includes）靠 polyfill；两者都要配 targets。

```javascript
// webpack.config.js：生产级 babel-loader 配置
module.exports = {
  module: {
    rules: [{
      test: /\.(js|mjs|jsx|ts)$/,
      include: [require('path').resolve('src')], // 只编业务代码 严格 include 提速
      use: [{
        loader: 'babel-loader',
        options: {
          cacheDirectory: true,           // 开启 babel 层缓存
          cacheCompression: false,        // 缓存不压缩 换更快读取
          presets: [
            ['@babel/preset-env', {
              targets: { chrome: '87' },  // 或用 browserslistrc
              useBuiltIns: 'usage',       // 按需注入 polyfill
              corejs: { version: 3, proposals: false },
              modules: false,             // 关键 保留 ESM 让 webpack 做 tree-shaking
            }],
            '@babel/preset-typescript',
          ],
          plugins: [
            ['@babel/plugin-transform-runtime', { helpers: true, regenerator: true }],
          ],
          sourceType: 'unambiguous',      // ESM/CJS 混合仓库友好
        },
      }],
    }],
  },
};
```
