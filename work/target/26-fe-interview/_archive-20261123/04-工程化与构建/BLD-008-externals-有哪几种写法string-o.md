---
title: [BLD-008] externals 有哪几种写法？string、object、function、promise 分别什么场景？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-008：externals 有哪几种写法？string、object、function、promise 分别什么场景？
**答**：
- string：单个库，'jquery' → 全局 jQuery（配合 script 标签引入 CDN）。
- object：一次声明多个，key 是 import 名，value 是全局变量名或 `commonjs mod` 指定输出格式。
- function：动态判断，可根据 request、context、callback 返回是否外部化，适合"部分子路径外部化"（如排除 lodash 单模块）。
- promise：异步拿到 externals 映射，适合运行时读取远程清单（CDN 版本由服务下发）。
- 关键点：externals 的库不进 bundle，运行时必须真实可用（CDN script、宿主环境、node 内置模块）；SSR 场景常配合 nodeExternals 排除 node_modules。

```javascript
// webpack.config.js：四种写法分别演示
module.exports = {
  // 写法一 string
  // externals: 'jquery', // import $ from 'jquery' -> window.jQuery

  // 写法二 object
  externals: {
    react: 'React',
    'react-dom': 'ReactDOM',
    lodash: {
      commonjs: 'lodash',  // CJS 侧从 node_modules 外部解析
      amd: 'lodash',
      root: '_',           // 浏览器全局变量
    },
  },

  // 写法三 function（四选一，此处给出函数版供参考）
  // externals: [
  //   (ctx, callback) => {
  //     if (/^lodash\//.test(ctx.request)) return callback(null, `commonjs ${ctx.request}`);
  //     callback();
  //   },
  // ],

  // 写法四 promise
  // externals: [() => fetch('/api/externals.json').then((r) => r.json())],

  output: { libraryTarget: 'umd' }, // 外部化后输出 umd 便于挂全局
};
```

## 第二章 Tapable 与 Plugin 开发（BLD-009 ~ BLD-016）
