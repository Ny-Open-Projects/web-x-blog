---
title: [BLD-203] Tree-shaking 的原理与失效场景有哪些？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-203：Tree-shaking 怎么运作？
**答**：
- 原理：ESM 静态结构（import/export 编译期确定）→ 打包器标记导出使用情况（usage analysis）→ 未使用导出标记为可摇 → 压缩器（terser）按 /*#__PURE__*/ 注释与副作用分析实际删除。
- 失效场景：CJS 模块（动态 require）、有副作用的模块（顶层执行代码无 sideEffects:false 声明）、动态访问导出（obj[key]）、类成员方法（压缩器不敢删）、re-export 桶文件的副作用传递。
- sideEffects 的语义：`"sideEffects": false` 声明「导入无副作用可整体摇除」——但错误声明（实际有副作用）会导致运行时 bug（代码被删）。
- 摇不动时的手段：按需子路径导入（lodash-es）、babel-plugin-import 转换、包本身拆分入口。
- 追问钩子：为什么 `sideEffects: false` 用错会出运行时 bug——它告诉打包器「导入这个文件没有任何可观察效果，没用到导出就整体删掉」；若文件里有 polyfill/样式注入/全局注册（副作用），被摇除后功能静默失效——声明副作用清单是诚实性问题。

```jsonc
// package.json
{ "sideEffects": ["**/*.css", "./src/polyfills.js"] }   // 白名单声明副作用文件
```
```javascript
// PURE 注释辅助压缩器
const el = /*#__PURE__*/ createElement();  // 未使用可删
// 失效示例：CJS 动态
if (dev) { require('./debug'); }            // 打包器无法静态分析——整包打入
```
