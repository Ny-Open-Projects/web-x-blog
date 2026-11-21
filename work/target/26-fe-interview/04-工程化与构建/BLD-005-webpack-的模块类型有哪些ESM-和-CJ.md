---
title: [BLD-005] webpack 的模块类型有哪些？ESM 和 CJS 混用怎么解析？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-005：webpack 的模块类型有哪些？ESM 和 CJS 混用怎么解析？
**答**：
- 内置模块类型：javascript/auto（默认，自动判断 ESM/CJS）、javascript/esm（强制 ESM，违规报错）、javascript/dynamic（强制 CJS）、json、webassembly/asset、css（实验性）等，可通过 test + type 在 module.rules 里指定。
- javascript/auto 的混用规则：CJS 文件里可以 `require()` 一个 ESM 文件，取到的是其 namespace 对象（.default 属性拿默认导出）；ESM 文件里 `import` 一个 CJS 文件，整个 module.exports 被当作 default，命名导出靠 webpack 的静态分析尽力提取（cjs-module-lexer）。
- 坑点：CJS 的 `module.exports = { a }` 命名导出可以被静态分析；但 `module.exports = require('./x')` 或动态计算导出就不行，会退化为只有 default。
- mjs/cjs 后缀与 package.json 的 type 字段会改变默认判断。

```javascript
// webpack.config.js：显式声明模块类型
module.exports = {
  module: {
    rules: [
      {
        test: /\.legacy\.js$/,
        type: 'javascript/dynamic', // 强制按 CJS 处理 禁止 ESM 语法
      },
      {
        test: /\.strict\.mjs$/,
        type: 'javascript/esm', // 只允许 ESM 语法 出现 require 直接报错
      },
    ],
  },
};
```

```javascript
// src/cjs-lib.js —— CommonJS 侧
module.exports = { hello: () => 'hi', version: '1.0.0' };

// src/esm-app.js —— ESM 侧 混用 CJS
import cjsLib from './cjs-lib.js';      // default = module.exports 整体
import { hello } from './cjs-lib.js';   // 命名导入 依赖 cjs-module-lexer 静态分析成功

console.log(cjsLib.version, hello());

// src/cjs-entry.js —— CJS 侧 require ESM
const esm = require('./esm-app.js');    // 拿到 namespace
esm.default && console.log('default 存在');
```
