---
title: [203] Rspack Plugin 的执行顺序如何控制，stage 参数有什么用
date: 2026-11-17
categories: [Rust系构建工具]
tags: [前端面试, 面试题, Rspack, Plugin]
type: 面试题
---

## RBL-203：Rspack Plugin 的执行顺序如何控制？stage 参数有什么用？

**答**：
- 同一 hook 上多个 tap 的默认顺序 = 插件注册顺序，与 webpack 一致；想插队要用第三个参数 `stage`，数字越小越先执行。
- stage 支持 `-∞ ~ +∞`，常用档位在 `SyncWaterfallHook` 上最关键：前一个插件改了参数，后一个才拿得到，顺序错会导致结果被覆盖。
- Rspack 内置插件（如 html-plugin 对应能力）会占据固定 stage，业务插件一般用默认 0，需要「在内置之后兜底」时才调大。
- 追问钩子：Tapable 的 `before/after/stage` 三者优先级如何叠加？——before 优先于 stage，同 stage 再按注册序。

```javascript
class OrderDemoPlugin {
  apply(compiler) {
    // stage 越小越先跑：-100 保证自己排在别人前面
    compiler.hooks.emit.tap({ name: 'Early', stage: -100 }, (compilation) => {
      compilation.assets['early.txt'] = { source: () => 'first', size: () => 5 };
    });
    // 默认 stage 0，按注册顺序执行
    compiler.hooks.emit.tap('Normal', (compilation) => {
      compilation.assets['normal.txt'] = { source: () => 'second', size: () => 6 };
    });
    // stage 100：典型用途是在所有产物生成完之后做最终校验/清理
    compiler.hooks.emit.tap({ name: 'Late', stage: 100 }, (compilation) => {
      if (!compilation.assets['index.html']) {
        compilation.warnings.push(new Error('missing index.html'));
      }
    });
  }
}
module.exports = OrderDemoPlugin;
```
