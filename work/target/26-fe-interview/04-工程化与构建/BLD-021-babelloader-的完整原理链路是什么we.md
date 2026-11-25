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

## 追问（补充）

**追问**：

1. 同一 rule 里 loader 为什么倒序执行？ → 正常阶段从右到左、从下到上，pitch 阶段正序，所以 babel-loader 要写在数组最右边，source map 才能沿着 loader 链正确传递。
2. 为什么要开 `cacheDirectory`？ → babel 每次全量重跑很贵，缓存按文件内容与 babel 配置哈希落到 node_modules/.cache，只有源文件或配置变了才失效。
3. babel 和 webpack 各管什么？ → babel 只做单文件语法转换与 polyfill 注入，模块解析、依赖图构建和 chunk 拆分归 webpack，两者职责不要混，混用会导致重复转译。
