---
title: [RBL-059] Rolldown 的 advancedChunks 与 Rollup manualChunks 有何不同？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-059：Rolldown 的 advancedChunks 与 Rollup manualChunks 有何不同？
**答**：
- manualChunks 的老问题：函数式 manualChunks 只能"指名模块进哪个组"，无法精确控制 chunk 内成员、minSize/maxSize、依赖闭合关系，常产生碎片 chunk 或循环引用告警。
- advancedChunks 提供声明式分组：每个 group 可配 name、test（模块匹配）、priority、minShareCount、minSize/maxSize，并在 Rust 侧统一计算，保证组间依赖闭合（被共享的依赖自动进对应组）。
- 语义对照：接近 webpack splitChunks cacheGroups 的表达力——这也是 rolldown 吸收 webpack 系用户经验的体现。
- 典型分组：vendor（node_modules）、ui 库单独（体积大缓存稳定）、业务公共（minShareCount >= 2）。
- 兼容性：manualChunks 仍支持（函数式），但官方推荐新项目用 advancedChunks。
- 追问钩子：chunk 过碎会增加请求数与 module prelude 开销，chunk 过大影响缓存粒度——advancedChunks 的 minSize/maxSize 就是平衡器。

```javascript
// rolldown.config.js
export default {
  input: { main: 'src/index.ts' },
  output: {
    advancedChunks: {
      groups: [
        { name: 'vendor-ui', test: /[\\/]node_modules[\\/](react|antd)/, priority: 10 },
        { name: 'vendor',    test: /[\\/]node_modules[\\/]/, priority: 5,
          minShareCount: 1, minSize: 20_000 },
        { name: 'common',    minShareCount: 2, priority: 1 }, // 业务公共
      ],
    },
  },
};
```
