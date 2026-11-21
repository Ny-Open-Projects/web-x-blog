---
title: [RBL-031] 如何给 Rspack 编写并调试自定义 loader？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-031：如何给 Rspack 编写并调试自定义 loader？
**答**：
- 写法与 webpack 兼容：导出 function(source)（同步）或 function(source, cb)（异步 this.async()），this 上有 getOptions、resourcePath、emitFile 等上下文。
- 尽量同步返回：同步函数开销小于异步回调；能纯转换就不要 IO。
- options 校验：用 schema-utils 或手动 getOptions 校验，避免静默错误配置。
- 调试手段：loader 内 console.log 输出 resourcePath 与转换前后长度；配合 Rsdoctor 看 loader 命中文件列表与耗时；本地 loader 用 resolveLoader.modules 指向本地目录。
- 缓存契约：无副作用的 loader 声明可缓存语义（Rspack 会缓存转换结果），副作用型（emitFile）要小心重放。
- 追问钩子：Rspack 对 JS loader 每次 emit 都走 FFI，因此自定义 loader 要"一次做完"，避免中间多次回调。

```javascript
// loaders/md-to-html-loader.js
const { marked } = require('marked');
module.exports = function (source) {
  const opts = this.getOptions() || {};
  const html = marked.parse(source, { gfm: !!opts.gfm });
  // 输出成可 import 的模块而不是裸 HTML
  return `export default ${JSON.stringify(html)};`;
};
// rspack.config.js
// { test: /\.md$/, use: { loader: path.resolve('loaders/md-to-html-loader.js'), options: { gfm: true } } }
// resolveLoader: { modules: ['node_modules', path.resolve(__dirname, 'loaders')] }
```
