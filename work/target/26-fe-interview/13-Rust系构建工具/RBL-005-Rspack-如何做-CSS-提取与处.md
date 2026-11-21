---
title: [RBL-005] Rspack 如何处理 CSS？与 webpack 方案有何差异？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-005：Rspack 如何处理 CSS？与 webpack 方案有何差异？
**答**：
- webpack 经典链路是 css-loader + mini-css-extract-plugin（JS 插件）+ postcss-loader，三层 JS 实现，模块多时是主要瓶颈。
- Rspack 用内置 CSS 处理器：`type: 'css'`、`'css/module'`、`'css/auto'` 三个模块类型直接在 Rust 里完成解析与依赖收集，不需要 css-loader。
- 提取策略：生产模式默认把 CSS 提取成独立文件（相当于内置 mini-css-extract-plugin 语义），开发模式走 `experiments.css.hot` HMR 注入，不再依赖 style-loader。
- 预处理器不变：less/sass/scss 仍需对应 loader 把源码编译成 CSS，之后再交给内置 css 模块类型；PostCSS 可用 postcss-loader 或内置 lightningcss（experiments.css 选项）。
- 追问钩子：CSS Modules 约定 `.module.css` 配合 `css/auto` 自动识别；tree shaking 对 CSS 也生效（未引用的 class 导出可被摇掉）。

```javascript
// rspack.config.js
module.exports = {
  experiments: { css: true }, // 0.x 版本需显式开启，新版默认支持
  module: {
    rules: [
      { test: /\.css$/, type: 'css/auto' },          // 自动识别普通 css 与 css module
      { test: /\.scss$/, use: ['sass-loader'], type: 'css/auto' }, // 预处理器先转 css
    ],
  },
  optimization: {
    // 生产下 css 自动提取为独立 chunk 文件，无需 mini-css-extract-plugin
    minimizer: ['...', new (require('@rspack/plugin-lightning-css'))()], // 可选
  },
  output: { cssFilename: 'css/[name].[contenthash:8].css' },
};
```
