---
title: [RBL-063] Rolldown 如何处理 CommonJS 互操作？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-063：Rolldown 如何处理 CommonJS 互操作？
**答**：
- 内置 commonjs 原生插件：把 CJS 模块（lodash、旧版包）转换成 ESM 可导入的形式，替代 @rollup/plugin-commonjs 的 JS 实现（更快）。
- 互操作规则：CJS 的 module.exports 对象映射为 default 导出 + 具名导出推断（可枚举属性）；__esModule 标记被识别时尊重原始 ESM 转译结构。
- 常见坑：CJS 的动态 require（require(variable)）无法静态分析——需要显式声明 external 或限制 glob；CJS 模块的 side effect（顶层 require 触发逻辑）保留。
- default vs named：`import _ from 'lodash'`（CJS）拿到的是 module.exports 本体；rolldown 会给出互操作警告提示使用方式。
- 与 node 的语义对齐：ESM 导入 CJS 在 Node 的 default = module.exports，rolldown 遵循同一规则，避免浏览器/Node 双端行为差异。
- 追问钩子：`default is not exported` 类报错的根因通常是 CJS 导出了函数或重赋值 module.exports，要用 default-import + 解构或改用动态加载。

```javascript
// rolldown.config.js
import native from 'rolldown/experimental';
export default {
  input: 'src/index.ts',
  plugins: [native.commonjs()], // CJS → ESM 互操作
  // 动态 require 场景兜底：
  external: [/^lodash(\/.*)?$/], // 直接 external 交给运行时
};
// 源码
// import _ from 'lodash'; // CJS default → module.exports 本体
```
