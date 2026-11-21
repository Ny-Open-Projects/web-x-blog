---
title: [ENG-018] 如何写一个自定义 webpack plugin？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-018：如何写一个自定义 webpack plugin？
**答**：
- plugin 是带 apply(compiler) 方法的类或对象，通过 compiler.hooks / compilation.hooks 注册回调。
- compiler 代表整个构建生命周期；compilation 代表一次资源编译，可拿到 chunks 与 assets。
- tap 第一个参数是插件名，用于调试追踪；关注时机的典型选择有 emit、afterOptimizeChunkAssets。
- 输出文件阶段可改写 compilation.assets。

```javascript
// plugins/build-log-plugin.js
class BuildLogPlugin {
  apply(compiler) {
    const pluginName = 'BuildLogPlugin';

    compiler.hooks.compilation.tap(pluginName, (compilation) => {
      compilation.hooks.afterOptimizeChunkAssets.tap(pluginName, (chunks) => {
        for (const chunk of chunks) {
          console.log(chunk.name, '模块数', chunk.getModules().length);
        }
      });
    });

    compiler.hooks.done.tap(pluginName, (stats) => {
      console.log('构建完成，耗时', stats.endTime - stats.startTime, 'ms');
    });
  }
}

module.exports = BuildLogPlugin;
```
