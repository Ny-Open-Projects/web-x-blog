---
title: [BLD-109] 给一份 React 项目产物做 runtime 逐行解读：IIFE、模块缓存、require 函数、模块表。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-109：给一份 React 项目产物做 runtime 逐行解读：IIFE、模块缓存、require 函数、模块表。
**答**：
- 产物骨架四段：IIFE 外壳 → `__webpack_module_cache__`（模块缓存，保证模块单例）→ `__webpack_require__(moduleId)`（查缓存→加载模块→返回 exports）→ `__webpack_modules__`（模块表，key 为 moduleId，value 为模块包装函数）。
- ESM 编译形态：`__webpack_require__.r(__webpack_exports__)` 打 `__esModule` 标记；`.d` 定义 getter 实现命名空间导出；`.n` 处理 ESM/CJS default 兼容（getDefault vs getModuleExport）。
- import 语句编译：`import { useState } from 'react'` → `var react__WEBPACK = __webpack_require__("react")`，后续使用点直接从该变量取；tree-shaking 生效时未被使用的 getter 会被删除。
- 动态 import 编译为 `__webpack_require__.e(chunkId).then(__webpack_require__.t.bind(...))`：先拉 chunk（jsonp）再取模块（t 做 interop）；entry 尾部是 `__webpack_require__("./src/index.js")` 启动调用。

```javascript
// dist/main.js 产物剖析（逐段注释，面试可直接口述）
(() => { // webpackBootstrap
  var __webpack_modules__ = ({
    "./src/App.js": ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
      "use strict";
      __webpack_require__.r(__webpack_exports__);          // 标记 ESM：__esModule + Symbol.toStringTag
      /* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, {
        default: () => __WEBPACK_DEFAULT_EXPORT__          // getter：导出绑定而非值拷贝
      });
      var _react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
      const App = () => _react__WEBPACK_IMPORTED_MODULE_0__.useState(0)[0]; // import 的使用点
      __WEBPACK_DEFAULT_EXPORT__ = App;
    }),
  });

  var __webpack_module_cache__ = {};
  function __webpack_require__(moduleId) {
    var cachedModule = __webpack_module_cache__[moduleId];
    if (cachedModule !== undefined) return cachedModule.exports;   // ① 缓存命中 → 单例
    var module = __webpack_module_cache__[moduleId] = { exports: {} }; // ② 先入缓存再执行（防循环引用）
    __webpack_modules__[moduleId](module, module.exports, __webpack_require__);
    return module.exports;                                          // ③ 返回 exports
  }
  // .r/.d/.n/.e 等辅助函数定义（省略）

  __webpack_require__("./src/index.js");   // entry 启动：执行主入口模块
})();
```
