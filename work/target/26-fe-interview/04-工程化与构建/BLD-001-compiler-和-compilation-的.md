---
title: [BLD-001] compiler 和 compilation 的区别是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-001：compiler 和 compilation 的区别是什么？
**答**：
- compiler 对象代表整个 webpack 生命周期，从启动到关闭只有一个，承载全局配置（options、root、outputPath）和全局级 hooks（run、emit、done、watchRun）。
- compilation 代表"一次编译过程"，watch 模式或 rebuild 时每次都会新建，承载本次的 modules、chunks、assets 和模块级 hooks（buildModule、seal、optimizeChunkAssets）。
- 插件若要操作"本次产物"（如改 chunk、加 asset）必须在 compilation 的钩子里做；若只关心"构建整体"（如统计、日志、清目录）用 compiler 钩子。
- 记忆口诀：compiler 是工厂，compilation 是一批订单。

```javascript
// webpack.config.js：同时演示 compiler 级与 compilation 级钩子
const plugin = {
  name: 'CompilerVsCompilationPlugin',
  apply(compiler) {
    // compiler 级：整个构建只触发一次
    compiler.hooks.run.tap('CompilerVsCompilationPlugin', () => {
      console.log('compiler：单次构建开始');
    });

    // compilation 级：watch 下每次 rebuild 都会触发
    compiler.hooks.compilation.tap('CompilerVsCompilationPlugin', (compilation) => {
      console.log('compilation：一次新编译，hash =', compilation.hash);
      compilation.hooks.seal.tap('CompilerVsCompilationPlugin', () => {
        console.log('compilation：模块封装开始，module 数 =', compilation.modules.size);
      });
    });
  },
};

module.exports = { plugins: [plugin] };
```
