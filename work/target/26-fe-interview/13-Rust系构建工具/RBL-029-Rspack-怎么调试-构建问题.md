---
title: [RBL-029] Rspack 构建报错或产物异常时怎么调试？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-029：Rspack 构建报错或产物异常时怎么调试？
**答**：
- 报错分类定位：resolve 失败（Module not found）查 alias/extensions/exports 字段；loader 转换错（SyntaxError）查 rules 顺序与 parser 配置；运行时错（undefined is not a function）多半是 shared/polyfill/双实例问题。
- stats 取证：`rspack build --json` 拿 modules/chunks/errors 全量数据，配合 stats.errors 堆栈里给出的模块链路追溯引入方。
- 最小复现：把可疑配置逐步裁剪（二分注释 rules/plugins），或建最小 demo 验证工具行为，再回填业务配置。
- 对 webpack 对照：同一配置在 webpack 下构建对比产物，确定是 Rspack 语义差异还是配置本身问题；diff 输出文件与 sourcemap。
- 社区渠道：GitHub issue 搜兼容性报告，很多"神秘错误"（如某插件 hook 时机）已有官方 issue 记录 workaround。
- 追问钩子：产物异常（运行时顺序错）优先查 splitChunks 与 entry vendor 的公共块依赖顺序，runtime 要在最前。

```javascript
// 追溯"这个模块为什么被引入"：用 stats.json 的 issuer 链
const stats = require('./dist/stats.json');
function trace(name) {
  let m = stats.modules.find(m => m.name.endsWith(name));
  while (m) {
    console.log(m.name);
    m = stats.modules.find(x => x.identifier === m.issuer);
  }
}
trace('lodash.js'); // 打印完整引入链 → 定位罪魁
```
