---
title: [BLD-022] style-loader 的注入原理是什么？它和 HMR 有什么关系？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-022：style-loader 的注入原理是什么？它和 HMR 有什么关系？
**答**：
- style-loader 几乎全在 pitch 阶段工作：pitch 里用 remainingRequest 组一个虚拟 require，返回一段运行时代码——运行时把 css-loader 导出的 CSS 模块结果，通过 addStyle（创建 style 标签、insert 到指定位置）注入 document。
- 好处：CSS 变成了 JS 模块的一部分，天然获得 webpack 模块系统的 HMR 能力：模块更新时只重新执行该模块，style-loader 会移除旧 style、插入新 style。
- 源码结构：lib/index.js（pitch）+ lib/runtime/injectStylesIntoStyleTag.js（运行时，处理 attrs、transform、insert、单实例引用计数）。
- 与 mini-css-extract-plugin 互斥：一个走运行时注入，一个在构建期抽成 css 文件，生产抽离（避免 FOUC）、开发注入（HMR 更快）。

```javascript
// style-loader pitch 原理简化实现
module.exports = {};
module.exports.pitch = function (remainingRequest) {
  // remainingRequest 是"链上剩余 loader + 资源"的可 require 描述
  return `
    var content = require(${JSON.stringify('-!' + remainingRequest)}); // -! 禁用 pre/normal loader 防止递归
    var style = document.createElement('style');
    style.setAttribute('data-vite-hmr-marker', 'webpack-style');
    style.innerHTML = content.toString();
    document.head.appendChild(style);

    if (module.hot) {
      module.hot.accept(${JSON.stringify('-!' + remainingRequest)}, function () {
        // HMR：新内容到达 移除旧标签 换新标签
        var newContent = require(${JSON.stringify('-!' + remainingRequest)}).toString();
        style.innerHTML = newContent;
      });
    }
  `;
};

// webpack.config.js：开发/生产差异化
// module.exports = (_, argv) => ({
//   module: { rules: [{
//     test: /\.css$/,
//     use: [
//       argv.mode === 'development' ? 'style-loader'          // dev 注入 快 + HMR
//         : require('mini-css-extract-plugin').loader,        // prod 抽离 避免 FOUC
//       'css-loader',
//     ],
//   }] },
// });
```
