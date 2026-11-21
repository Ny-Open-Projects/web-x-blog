---
title: [BLD-108] Runtime 模块是什么？__webpack_require__ 和 __webpack_require__.e 是怎么生成的？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-108：Runtime 模块是什么？__webpack_require__ 和 __webpack_require__.e 是怎么生成的？
**答**：
- webpack5 把 runtime 拆成一个个 `RuntimeModule` 子类（AutoPublicPathRuntimeModule、LoadScriptRuntimeModule、GetMainFilenameRuntimeModule 等），按本次编译**实际需要**按需拼装，而不是大段静态模板——runtime 体积随用到的能力伸缩。
- 数据流：codeGeneration 阶段每个 module 上报 `runtimeRequirements`（如 `__webpack_require__.e`、`document`、`__webpack_require__.p`）；JavascriptModulesPlugin.render 时 `getRuntimeModules(runtimeRequirements, chunkRuntime)` 过滤出对应 RuntimeModule，经 RuntimeTemplate 渲染拼进 bootstrap。
- `__webpack_require__` 本体来自 RuntimeTemplate.requireFunction；`.e`（ensureChunk）来自 LoadScriptRuntimeModule：动态插 script 标签 + `webpackChunk.push` jsonp 回调 promise 化；`.p`（publicPath）来自 AutoPublicPathRuntimeModule（document.currentScript 探测）。
- 面试落点：为什么 runtimeChunk 的 contenthash 会飘——runtimeRequirements 是并集，动态 import 数量、publicPath 方式、HMR 开关都会改变 runtime 内容，进而影响引用它的 chunk hash。

```javascript
// 产出产物里的 runtime（LoadScriptRuntimeModule 生成的 __webpack_require__.e 核心逻辑，注释版）
__webpack_require__.e = (chunkId) => Promise.all(
  Object.keys(__webpack_require__.f).reduce((promises, key) => {
    __webpack_require__.f[key](chunkId, promises);   // f.j = jsonp chunk，f.script = script 加载
    return promises;
  }, [])
);
// 其中 f.j 的大致实现：
__webpack_require__.f.j = (chunkId, promises) => {
  if (installedChunks[chunkId] !== 0) {              // 0 = 已加载
    promises.push(installedChunks[chunkId] = new Promise((resolve, reject) => {
      installedChunks[chunkId] = [resolve, reject];
    }));
  }
};
// webpackChunk.push 回调：chunk 文件尾部自执行
(self["webpackChunkapp"] = self["webpackChunkapp"] || []).push([
  [chunkId],               // 命中 installedChunks[chunkId] → resolve promise
  { "./src/lazy.js": (module, exports, __webpack_require__) => { /* 模块体 */ } }
]);

// 用 webpack API 侧写 Runtime 模块（注入自定义 runtime 行为的正规方式）
const { RuntimeModule, RuntimeGlobals } = require('webpack');
class CustomPublicPathRuntime extends RuntimeModule {
  constructor() { super('custom-public-path', 10 /* STAGE_BASIC */); }
  generate() {
    return `${RuntimeGlobals.publicPath} = window.CDN_BASE + '/static/';`;
  }
}
class CustomRuntimePlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('CustomRuntime', (compilation) => {
      compilation.hooks.runtimeRequirementInTree
        .for(RuntimeGlobals.publicPath)                     // 拦截 __webpack_require__.p 的生成
        .tap('CustomRuntime', (chunk, set) => {
          set.delete(RuntimeGlobals.publicPath);            // 不用默认实现
          compilation.addRuntimeModule(chunk, new CustomPublicPathRuntime());
        });
    });
  }
}
```
