---
title: [RBL-024] 为什么 Rspack 场景下 JS loader 会成为瓶颈？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-024：为什么 Rspack 场景下 JS loader 会成为瓶颈？
**答**：
- 跨界成本：每个文件经 JS loader 都要 Rust→FFI→JS 执行→FFI→Rust 的往返，包括源码字符串封包与 this 上下文构造；文件数×loader 数越大成本线性放大。
- 单线程限制：JS loader 在 Node 事件循环执行，天然串行；Rust 侧并行流水线到 loader 这一环被"收窄"，整体并行度被 JS 环节拖住。
- 二次开销：很多 JS loader（babel/postcss）内部还有自己的插件遍历，自身就慢，双慢叠加。
- 优化清单：优先 builtin:swc-loader、内置 CSS；必须用 JS loader 时缩小 test 范围、排除 node_modules、加 cacheDirectory；重度 loader 用 thread-loader 思路改 worker 的方案在 Rspack 里收益有限（瓶颈在 FFI 不在编译本身）。
- 度量方法：Rsdoctor loader 耗时榜看 top10，把 JS loader 逐个替换并对比构建时长。
- 追问钩子：这也是 Rspack 官方"迁移 checklist"把「减少 JS loader/plugin」排在第一位的原因。

```javascript
// rspack.config.js：JS loader 收敛示例
module.exports = {
  module: {
    rules: [
      // 1) 只对业务源码启用，排除 node_modules
      { test: /\.[cm]?js$/, include: path.resolve('src'), use: 'builtin:swc-loader' },
      // 2) 确需 postcss 时限定文件类型并缓存
      { test: /\.css$/, use: ['postcss-loader'], type: 'css/auto' },
      // 3) 全量 fallback loader 用 include 白名单而不是 exclude 黑名单
    ],
  },
};
```
