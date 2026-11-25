---
title: [BLD-208] 打包产物的 runtime（模块加载器）都做了什么？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-208：打包 runtime 都做了什么？
**答**：
- 核心职责：模块注册表（modules 映射）、缓存（installedModules 保证单例）、require 实现（CJS wrapper：exports/module/this）、ESM 互操作（__esModule 标记/interop default）、chunk 加载器（jsonp/import 动态 script + promise 缓存）。
- 异步 chunk 加载：runtime 的 `__webpack_require__.e` —— script 注入 + onload/onerror + promise；加载失败的处理（chunk error → 提示刷新，SCN-OPS-218 自愈联动）。
- HMR runtime：WS 连接/更新清单/accept 传播（SCN-BLD-205）。
- 预加载协调：chunk 依赖图 → modulepreload 注入（SCN-ENG-325）。
- 追问钩子：为什么 ESM 互操作（interop）是产物 runtime 的重灾区——CJS 的 module.exports 与 ESM default 语义不对齐（exports 对象 vs default 值）；打包器用 `__esModule` 标记 + `_interopRequireDefault` 补桥，混用时 `default.default` 或 `undefined` 报错是产物级高频 bug。

```javascript
// runtime 核心（简化）
var installedModules = {};
function __webpack_require__(moduleId) {
  if (installedModules[moduleId]) return installedModules[moduleId].exports;   // 单例缓存
  var module = installedModules[moduleId] = { exports: {} };
  modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
  return module.exports;
}
// interop
function _interopRequireDefault(obj) {
  return obj && obj.__esModule ? obj : { default: obj };
}
```
