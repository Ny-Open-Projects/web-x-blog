---
title: [RBL-132] SWC 与 Babel 的差异？什么场景仍需要 Babel
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-132：SWC 与 Babel 的差异？什么场景仍需要 Babel

**答**：
- 性能：SWC 是 Rust 原生实现，解析+转换一次到位；Babel 的 traverse 阶段每访问一个节点都要 JS 回调 + 跨 AST 引用，慢 1~2 个数量级。
- 插件生态：Babel 有海量社区插件（按 visitor 写 JS），SWC 插件要编译成 WASM，生态薄很多——这是迁移最大的阻力点。
- 行为兼容：SWC 声明对齐 Babel preset-env 的能力（browser 兼容降级、proposal 插件内置），常见 preset 场景可直接替换。
- 仍需要 Babel 的场景：1) 依赖小众 Babel 插件（如某些装饰器实验特性、自定义宏）；2) 做源码级 AST 分析/改写的工具链（jscodeshift 等）；3) 团队无法承担 WASM 插件开发成本。
- 追问钩子：两者可以共存——SWC 做语法降级（热点路径），Babel 只跑少数插件链，用 cacheDirectory 控制成本。

```javascript
// babel.config.js 与 .swcrc 的等价映射示例
// Babel:
//   presets: [["@babel/preset-env", { targets: "> 0.25%, not dead" }], "@babel/preset-react"]
// SWC 等价：
module.exports = {
  jsc: {
    parser: { syntax: 'ecmascript', jsx: true },
    target: 'es2018', // 具体目标版本；按 browserslist 用 env 项指定
    transform: { react: { runtime: 'automatic' } },
  },
  env: {
    targets: '> 0.25%, not dead', // 与 browserslist 同源，SWC 会按需降级 + 注入 helper
    mode: 'usage',                // 类似 useBuiltIns: 'usage'，按用到的语法注 polyfill
    coreJs: '3.30',
  },
};
```
