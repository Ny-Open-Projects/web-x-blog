---
title: [BLD-092] PostCSS 在构建链路中的角色是什么？autoprefixer、preset-env、Tailwind 的构建链路各是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-092：PostCSS 在构建链路中的角色是什么？autoprefixer、preset-env、Tailwind 的构建链路各是什么？
**答**：
- PostCSS 本身是"CSS 的 babel"：AST 解析 + 插件转换的框架；在 webpack 里以 postcss-loader 存在（置于 css-loader 之前，Vite 内置支持 postcss.config.js）。
- autoprefixer：按 browserslist 加前缀（-webkit-），现在职责部分被 postcss-preset-env 接管（含未来语法降级）。
- postcss-preset-env：把"现代 CSS"（nesting、custom properties 的 fallback、:has 等）按 targets 降级，类似 babel preset-env。
- Tailwind 构建：v3 用 postcss 插件扫描源码生成原子类；v4 改为 CSS-first（@import "tailwindcss"）由 lightningcss 引擎处理——配置重心从 js 到 css。

```javascript
// postcss.config.js：三种链路
module.exports = {
  plugins: [
    // 链路一 纯前缀
    require('autoprefixer')({ overrideBrowserslist: ['> 0.3%', 'not dead'] }),

    // 链路二 现代语法降级（与 autoprefixer 二选一或按序）
    // require('postcss-preset-env')({ stage: 2, features: { 'nesting-rules': true } }),

    // 链路三 Tailwind v3
    // require('tailwindcss')({ content: ['./src/**/*.{vue,tsx}'] }),
    // require('autoprefixer'),
  ],
};

// tailwind v4 的 CSS-first 入口（text 代码块）：
// @import "tailwindcss";            /* 替代 v3 的三层 @tailwind 指令 */
// @source "../src";                 /* 显式扫描范围 */
// @theme { --color-brand: #0ea5e9; }
```
