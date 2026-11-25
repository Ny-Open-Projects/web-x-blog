---
title: [RBL-010] Rspack 的 Loader 与 Plugin 机制和 webpack 有什么异同？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-010：Rspack 的 Loader 与 Plugin 机制和 webpack 有什么异同？
**答**：
- 概念同构：loader 仍是"文件转换函数"（输入源码→输出源码），plugin 仍是 apply(compiler) 订阅钩子的对象，心智模型可直接迁移。
- 执行位置不同：Rspack 内置 loader（builtin:swc-loader、内置 css）在 Rust 线程池并行执行；JS loader 在 Node 侧逐个文件跨 FFI 调用，是串行化热点。
- 钩子覆盖是子集：compiler.hooks 的 compilation、thisCompilation、make、emit、done 等高频钩子可用；冷门钩子未实现或语义近似。tapable 的 tap/tapAsync/tapPromise 三种注册方式均支持。
- this 上下文差异：JS loader 的 this 上提供 getOptions、emitFile、async 等 API，与 webpack 对齐；个别字段（如 this.data 原子传递）可能缺失。
- 实战守则：能用内置 loader 就不用 JS loader；plugin 优先用 @rspack/core 内置或 rspack-* 官方版；自研 plugin 只碰文档列出的稳定 API。
- 追问钩子：pitch 机制保留，loaders 数组顺序语义（从后往前执行）与 webpack 一致。

```javascript
// 自定义 Rspack plugin：与 webpack 插件写法几乎一致
class LogAssetsPlugin {
  apply(compiler) {
    compiler.hooks.emit.tap('LogAssetsPlugin', (compilation) => {
      for (const name of Object.keys(compilation.assets)) {
        const size = compilation.assets[name].size();
        console.log(`[emit] ${name} ${size}B`);
      }
    });
  }
}
// 自定义 JS loader（与 webpack 相同）
const stripLog = (source) => source.replace(/console\.log\([^)]*\);?/g, '');
module.exports = { LogAssetsPlugin, stripLog };
```
