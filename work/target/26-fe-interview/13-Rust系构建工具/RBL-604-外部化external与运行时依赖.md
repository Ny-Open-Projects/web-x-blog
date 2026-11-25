---
title: [RBL-604] External 的精确语义：从字符串匹配到正则到函数的三代演进
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-604：External 的精确语义：从字符串匹配到正则到函数的三代演进

**答**：
- external = 打包时不解析不打包，产物里保留 import 语句交由运行时环境解析。三代 API：字符串数组（全等匹配，无法处理子路径）、正则（`/^react/` 误伤 react-dom-interop 之类前缀包）、**函数**（`(id, importer, isEntry) => boolean`，可读上下文精确决策）——现代工具以函数为主、字符串为语法糖。
- 语义细节：1) external 的粒度是「导入说明符 + 子路径」，`react` external 但 `react/jsx-runtime` 不一定（要分别判定）；2) **external 的输出形式由 output.format 与全局环境决定**——ESM 产物保留 import，IIFE 产物需要 globals 映射（react -> React）；3) relative import 一般不可 external（相对路径运行时不存在），函数式 API 要防止误判。
- 场景校准：SSR bundle external 全部 node_modules（运行时走 node_modules，减少 bundle 体积与启动解析）；微前端子应用 external 宿主共享依赖（react/vue 只加载一份）；SDK 产物 external peer 依赖（避免多实例）——同一工具不同场景 external 策略完全不同，这是「按场景配置」而非默认值。
- external 与 tree shaking 的交互：external 模块的**使用面**（用了哪些导出）仍可用于副作用分析——打包器可以对外部模块做 reexport 代理优化（保留具名 import 而非命名空间），这是「外部化 ≠ 放弃分析」。
- 追问钩子：external 依赖的版本一致性风险——bundle 不带版本，运行时拿到的版本由宿主/用户环境决定，SDK 场景要用 peerDependencies + 运行时能力探测（feature detect）双保险，否则宿主 react 16 与 SDK 要求 18 的冲突静默炸运行时。

```javascript
// 函数式 external 配置
export default {
  external: (id, importer, opts) => {
    // SSR 场景：node_modules 全外置
    if (opts.env === 'ssr' && !id.startsWith('.') && !path.isAbsolute(id)) return true;
    // SDK 场景：peer 依赖外置（含子路径），其余内联
    if (opts.env === 'sdk') return ['react', 'react-dom'].some(p => id === p || id.startsWith(p + '/'));
    return false;
  },
  output: {
    format: 'iife',
    globals: { react: 'React', 'react-dom': 'ReactDOM' },  // IIFE 的全局映射
  },
};

// reexport 代理优化：外部模块保留具名
// 源：import { useState } from 'react'    （external）
// 产物：import { useState } from 'react'; // 保持具名而非 import * as react（利于 CJS 互操作 tree-shaking）
```
