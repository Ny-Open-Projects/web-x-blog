---
title: [BLD-127] babel-plugin-macros 的适用场景是什么？和普通 Babel 插件怎么选？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-127：babel-plugin-macros 的适用场景是什么？和普通 Babel 插件怎么选？
**答**：
- 普通插件是**全局编译管线**（配置在 babel.config，所有文件都被处理）；macro 是**文件内显式引用**（`import { gql } from '../macros/gql.macro'`），构建时把调用点展开为编译期结果——零配置注入、按文件生效。
- 典型场景：GraphQL 查询预编译（relay/virtoso? ）、`preval` 构建期求值（把模块执行结果内联为常量）、CSS-in-JS 零运行时（`linaria/compiled`）、i18n 编译期提取。
- 选型：**插件级**跨项目/全量转换 → 普通 babel 插件；**调用级**按需编译、想在业务代码里"看得见摸得着" → macro；macro 的优点是局部可控、不污染整条管线，缺点是约定 `xxx.macro` 命名且需要 babel-plugin-macros 驱动。
- 与 Vite 的关系：Vite 用 esbuild/rollup 走自身转换链，babel 宏需要 `vite-plugin-babel-macros` 显式接入——迁移技术栈时这是常见兼容点。

```javascript
// 自定义 macro：构建期内联版本号与 env 检查（version.macro.js）
const { createMacro } = require('babel-plugin-macros');
const t = require('@babel/types');

function versionMacro({ references, state, babel }) {
  const { types: t } = babel;
  references.default?.forEach((refPath) => {
    // BUILD_VERSION 宏调用 → 编译期内联 package.json 的 version
    const version = require(state.file.opts.filename.includes('/packages/')
      ? '../../package.json' : './package.json').version;
    refPath.replaceWith(t.stringLiteral(version));
  });
  references.envCheck?.forEach((refPath) => {
    // envCheck() → 编译期断言，非法直接让构建失败
    if (process.env.REQUIRED_ENV !== 'ok') {
      throw refPath.buildCodeFrameError('REQUIRED_ENV 未配置，禁止构建');
    }
    refPath.replaceWith(t.booleanLiteral(true));
  });
}
module.exports = createMacro(versionMacro);

// 业务代码：
// import BUILD_VERSION from './version.macro';
// const banner = `app@${BUILD_VERSION}`;   → 产物： var banner = "app@2.7.1";（零运行时）
// 对比 DefinePlugin：define 替换"标识符"，macro 可以带参数、有作用域、能报编译错误
```
