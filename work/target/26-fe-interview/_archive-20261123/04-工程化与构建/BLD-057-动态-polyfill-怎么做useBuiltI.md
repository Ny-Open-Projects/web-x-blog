---
title: [BLD-057] 动态 polyfill 怎么做？useBuiltIns: usage + core-js 3 与按 UA 下发如何选择？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-057：动态 polyfill 怎么做？useBuiltIns: usage + core-js 3 与按 UA 下发如何选择？
**答**：
- 静态按需：@babel/preset-env 的 useBuiltIns: 'usage' + corejs: 3，扫描源码用到的 API 注入对应 import（构建期定，产物稳定，主流选择）。
- entry 模式：入口一次性注入 targets 所需全部 polyfill（体积大但可控）；false 表示不注入（库模式常用，交给使用方）。
- 动态按 UA：Polyfill.io / CDN 服务根据 User-Agent 返回差异 polyfill——产物最小，但依赖外部服务稳定性和缓存策略，有供应链风险需自托管。
- 结合 browserslist：targets 越新注入越少；用 `browserslist --coverage` 量化覆盖率取舍。

```javascript
// babel.config.js：usage + corejs3（推荐）
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: { chrome: '87', ie: '11' },
      useBuiltIns: 'usage',       // 按 API 使用情况注入
      corejs: { version: 3.36, proposals: false },
      modules: false,             // 保留 ESM 交给 webpack
    }],
  ],
};

// 源码效果（text 代码块）：
// 源码只用了 Promise 与 Array.prototype.includes
// 编译后自动注入：
// import 'core-js/modules/es.promise';
// import 'core-js/modules/es.array.includes';

// 动态 polyfill 自托管示例（index.html 片段，text 代码块）：
// <script defer
//   src="https://polyfill.internal.example.com/v3/polyfill.min.js?features=default,IntersectionObserver">
// </script>
```
