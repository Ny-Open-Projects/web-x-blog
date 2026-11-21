---
title: [ENG-026] @babel/preset-env 是如何按需转译的？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-026：@babel/preset-env 是如何按需转译的？
**答**：
- preset-env 根据 targets 中声明的浏览器范围，只注入必要的语法转换，不把所有语法无脑降级。
- useBuiltIns: 'usage' 配合 corejs 按需注入 API polyfill（Promise、Array.includes 等）。
- 浏览器范围通常写在 package.json 的 browserslist 字段，被 babel/autoprefixer 等共享。
- 目标越新产物越小：现代浏览器用 esbuild/SWC 直出，可显著减体积。

```javascript
// babel.config.js
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: { chrome: '100', firefox: '100' },
        useBuiltIns: 'usage', // 按实际用到的 API 注入 polyfill
        corejs: '3.36',
      },
    ],
  ],
};
```
