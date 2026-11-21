---
title: [OPT-145] polyfill 体积膨胀如何治理？按 UA 下发的方案怎么做？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-145：polyfill 体积膨胀如何治理？按 UA 下发的方案怎么做？

**答**：
- 全量 `core-js@3` + `regenerator-runtime` 可占 90~120KB，其中 80% 是老浏览器才需要的。治理三板斧：browserslist 精确目标、按 UA 下发、优先用原生特性检测。
- 工程配置：`browserslist` 声明目标（如 `chrome >= 87`），Babel/SWC 按目标只注入缺失的 polyfill（`useBuiltIns: 'usage'` + `corejs: 3`）。
- 双产物方案：构建现代/传统两份 bundle（`module`/`nomodule`），现代浏览器只吃无 polyfill 版本，可省 30~50% JS 体积。
- 缺陷排查：`core-js-compat` 或 `npm ls core-js` 查幽灵 polyfill；某依赖硬塞全量 core-js 时用 `resolve.alias` 强制指向项目内的精简版。

```javascript
// 一一对应：按 UA 下发 polyfill + 双产物入口（Express + script type）
// 1. 构建侧 .browserslistrc：
//   [production]
//   chrome >= 87
//   > 0.5%
//   not dead
// 2. webpack.config.js 关键配置：
// module.exports = {
//   target: ['web', 'es2020'],                 // 现代产物，语法级降级都省了
//   module: { rules: [{
//     test: /\.m?js$/, exclude: /node_modules\/(?!(oldd dep)\/)/,
//     use: { loader: 'babel-loader',
//       options: { presets: [['@babel/preset-env', { useBuiltIns: 'usage', corejs: 3 }]] } }
//   }] }
// };

// 3. 服务端按 UA 决定下发哪份产物（Express）
const UAParser = require('ua-parser-js');
app.get('*', (req, res) => {
  const { browser } = UAParser(req.headers['user-agent']);
  const isModern = (browser.name === 'Chrome' && +browser.major >= 87) ||
                   (browser.name === 'Safari' && +browser.major >= 14) ||
                   (browser.name === 'Firefox' && +browser.major >= 85);
  res.send(`<!doctype html>
<html><head>
  <!-- 现代浏览器吃 module 版，老浏览器吃 nomodule + 全量 polyfill -->
  <script type="module" src="${isModern ? '/js/main.modern.js' : '/js/main.legacy.js'}"></script>
  ${isModern ? '' : '<script nomodule src="/polyfills.legacy.js"></script>'}
</head><body><div id="root"></div></body></html>`);
});
```
