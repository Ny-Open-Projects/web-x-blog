---
title: [BLD-104] 依赖收集全链路：parse 阶段如何把 import/require 变成 Dependency 并长出模块图？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-104：依赖收集全链路：parse 阶段如何把 import/require 变成 Dependency 并长出模块图？
**答**：
- NormalModuleFactory 创建 NormalModule 时，`hooks.parser` 上由 JavascriptParser 工厂绑定解析器；parser 内部用 acorn 生成 AST，再对其 walk。
- 遇到 `ImportDeclaration/ExportNamedDeclaration` 调 `parser.hooks.import/export`，生成 `HarmonyImportSideEffectDependency + HarmonyImportSpecifierDependency`；遇到 `import()` 生成 `ImportDependency`（这就是代码分割的挂点）；`require()` 生成 `CommonJsRequireDependency`。
- build 完成后 `compilation.processModuleDependencies(module)`：遍历 dependencies → `handleModuleCreation` → 对每个新依赖再 factorize/build，深度优先递归，直到闭包齐——ModuleGraph 由此长出（边即 Dependency，节点即 Module）。
- Dependency 的关键方法 `getReference()` 返回"我引用了哪个模块的哪个 export"，tree-shaking 的 usedExports、`import { x } from 'a'` 的命名空间访问都靠它回溯。

```javascript
// 自定义 Parser 插件：在 parse 阶段观测依赖生成（分析器/自定义 DSL 的基础套路）
class DependencyProbePlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('DependencyProbePlugin', (compilation, { normalModuleFactory }) => {
      // parser 钩子挂在 normalModuleFactory.hooks.parser.for('javascript/auto')
      normalModuleFactory.hooks.parser
        .for('javascript/auto')
        .tap('DependencyProbePlugin', (parser) => {
          // ① 静态 import：import React from 'react'
          parser.hooks.import.tap('Probe', (statement, source) => {
            console.log('[import]', source, 'line', statement.loc.start.line);
          });
          // ② 动态 import：import('./lazy') —— 代码分割的依赖类型
          parser.hooks.importCall.tap('Probe', (expression) => {
            console.log('[import()]', expression.source?.value ?? '<dynamic>');
          });
          // ③ require：CJS 依赖
          parser.hooks.call.for('require').tap('Probe', (expression) => {
            console.log('[require]', expression.arguments[0]?.value);
            return false; // 返回 false 表示不接管，继续默认处理
          });
          // ④ 表达式引用探测：拿 HarmonsDependencies 之外的全局使用（如 process.env）
          parser.hooks.expression.for('process.env.NODE_ENV').tap('Probe', () => {
            console.log('[free var] process.env.NODE_ENV 被直接引用');
          });
        });
    });
  }
}

// 对应产物形态（理解 Dependency → 生成代码的关系）：
// import { useState } from 'react'
//   ↓ HarmonyImportSpecifierDependency
// var _react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
// const { useState } = _react__WEBPACK_IMPORTED_MODULE_0__;   // 优化后可能直接解构
```
