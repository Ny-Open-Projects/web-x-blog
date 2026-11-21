---
title: [BLD-030] ModuleConcatenationPlugin 的作用域提升原理是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-030：ModuleConcatenationPlugin 的作用域提升原理是什么？
**答**：
- 原理：把一组 ESM 模块"拍平"进同一个闭包（单一模块作用域），消掉模块边界——import/export 不再是独立模块调用，而是闭包内变量引用，从而省去模块包装函数与 _webpack_require 调用开销。
- 收益：运行时更快（无模块查找与缓存跳转）、代码更小（省包装样板）、tree-shaking 更彻底（跨模块的死代码在同一作用域可直接删）。
- 参与条件：全部为 ESM（harmony modules）、同一 chunk、无动态 import 中断、非 external、无 top-level await 冲突。
- 验证：optimization.concatenateModules: true，stats 里 concatenatedModules 字段显示哪些模块被合并；注意合并后 sourcemap 行号跨文件，调试时用真实行号映射。

```javascript
// webpack.config.js
module.exports = {
  mode: 'production',
  optimization: {
    concatenateModules: true,
    stats: { concatenatedModules: true, modules: true },
  },
};

// 合并效果示意（text 代码块）：
// 源码（两个 ESM 模块）：
//   a.js: export const add = (x, y) => x + y;
//   b.js: import { add } from './a.js'; export const sum = (list) => list.reduce(add, 0);
//
// 合并后（同一闭包 伪代码）：
//   (function () {
//     var add = (x, y) => x + y;          // a.js 内联
//     var sum = (list) => list.reduce(add, 0);
//     // __webpack_require__ 调用消失 模块边界消失
//   })();
```

## 第五章 代码分割 deep dive（BLD-031 ~ BLD-038）
