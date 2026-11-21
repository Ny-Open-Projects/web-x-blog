---
title: [BLD-004] loader 和 plugin 的本质区别是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-004：loader 和 plugin 的本质区别是什么？
**答**：
- 本质一：loader 是"文件转换函数"，输入是文件内容（字符串/Buffer），输出是转换后的内容，它无状态、纯转换、链式执行、只作用于匹配的 module。
- 本质二：plugin 是"基于 Tapable 钩子的事件订阅者"，通过 apply(compiler) 挂钩，能在构建全生命周期任意时机介入，可以改模块图、改产物、发请求、写文件。
- 作用面不同：loader 只在 module 构建阶段起作用；plugin 覆盖初始化、编译、封装、产出全流程。
- 一个"文件的搬运工"，一个"流程的监工"；复杂 loader 内部也可用 this.emitFile / 与 plugin 通过共享对象通信。

```javascript
// 一个 loader：本质就是 输入 -> 输出 的转换函数
module.exports = function (source) {
  // this 上有资源路径、query、async 等上下文，但没有 compiler 钩子
  return source.replace(/console\.log\([^)]*\);?/g, ''); // 示例：剔除 console.log
};

// 一个 plugin：本质是 Tapable 钩子对象上的订阅者
class HookBasedPlugin {
  apply(compiler) {
    // compiler 上挂着几十个钩子，可在任意生命周期介入
    compiler.hooks.compilation.tap('HookBasedPlugin', (compilation) => {
      compilation.hooks.processAssets.tap('HookBasedPlugin', (assets) => {
        for (const name of Object.keys(assets)) {
          compilation.updateAsset(name, (source) => source); // 可改产物
        }
      });
    });
  }
}
module.exports = HookBasedPlugin;
```
