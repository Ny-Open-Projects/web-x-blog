---
title: [BLD-124] @babel/plugin-transform-runtime 解决什么问题？helper 内联为什么会撑大产物？（高频）
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-124：@babel/plugin-transform-runtime 解决什么问题？helper 内联为什么会撑大产物？（高频）
**答**：
- Babel 编译产物依赖两类公共代码：**helper**（`_classCallCheck/_objectSpread` 等内联小函数）与 **polyfill**（Promise/Array.includes 等运行时 API）。不加 transform-runtime 时，helper 会被内联进**每个文件**，100 个文件就复制 100 份 `_classCallCheck`——产物膨胀。
- transform-runtime 把 helper 改为 `import _classCallCheck from '@babel/runtime/helpers/classCallCheck'`（**从统一包引用**），全项目只留一份；corejs 选项再把 `Promise` 等全局 API 替换为 `@babel/runtime-corejs3/core-js/...` 引用，**不污染全局**（库开发的关键）。
- 三选一：`corejs: 3`（库，无全局污染）／`corejs: { version: 3, proposals: true }`（可实验 API）／`false`（应用，polyfill 交给 useBuiltIns 全局垫）。
- 面试一句话：`useBuiltIns` 管"垫 API 全局"，`transform-runtime` 管"helper 去重 + 无污染引用"，两者职责不同，库项目通常两个都要。

```javascript
// babel.config.js：应用 vs 库两套典型配置
module.exports = (api) => {
  const isLib = api.env() === 'lib';
  return {
    presets: [['@babel/preset-env', { targets: { chrome: '80' } }]],
    plugins: [
      ['@babel/plugin-transform-runtime', {
        // helper：默认即开启引用化，这里显式声明
        helpers: true,
        // regenerator：async/await 的 runtime 引用化，否则每文件内联 regeneratorRuntime
        regenerator: true,
        // corejs3：库选 true（不污染全局）；应用选 false（走 useBuiltIns 全局垫一次）
        corejs: isLib ? { version: 3, proposals: false } : false,
        // 版本锁定：monorepo 内防止多份 @babel/runtime 版本并存（产物里出现重复 helper）
        version: require('@babel/runtime/package.json').version,
        absoluteRuntime: false,
      }],
    ],
  };
};
// 产物对比（同 100 个 class 文件）：
// 不加 transform-runtime：每个文件内联 ~300B 的 _classCallCheck → 共 30KB+
// 加后：每个文件一行 import + node_modules 里一份 helper，业务产物仅 ~1KB
```
