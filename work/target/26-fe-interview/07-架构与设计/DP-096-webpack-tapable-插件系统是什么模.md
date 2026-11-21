---
title: [DP-096] webpack/tapable 插件系统是什么模式组合？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-096：webpack/tapable 插件系统是什么模式组合？（高频）
**答**：
- tapable 提供各类 Hook（SyncHook/AsyncSeriesHook/AsyncParallelHook）——**发布订阅**的工程化（tap 注册、call/promise 触发）。
- webpack 编译流程（beforeRun→run→compile→make→emit→done）是一条**模板方法**骨架，每个阶段暴露钩子——插件通过 `compiler.hooks.xxx.tap` 在固定切面注入逻辑。
- **职责链**色彩：同一钩子上多个插件按注册顺序串行执行（AsyncSeriesHook 可拦截/异步传递）。
- **中介者**：Compiler/Compilation 是中心对象，所有插件围绕它协调（读取/改写构建产物）。

```javascript
// mini-tapable：发布订阅 + 异步串行职责链
class AsyncSeriesHook {
  #taps = [];
  tap(name, fn) { this.#taps.push({ name, fn }); }   // 订阅：插件注册
  async promise(...args) {                            // 发布：异步串行链
    for (const { name, fn } of this.#taps) {
      console.log(`[tap:${name}] before`);
      const r = await fn(...args);
      if (r === false) break;                         // 节点可短路（返回 false 中断链）
    }
  }
}
class ParallelHook {                                  // 并行变体：Promise.all
  #taps = [];
  tap(name, fn) { this.#taps.push({ name, fn }); }
  promise(...args) { return Promise.all(this.#taps.map(({ fn }) => fn(...args))); }
}
// mini-webpack：编译骨架（模板方法）+ 钩子切面
class Compiler {
  hooks = {
    beforeRun: new AsyncSeriesHook(),
    compile: new AsyncSeriesHook(),
    make: new AsyncSeriesHook(),
    emit: new AsyncSeriesHook(),
    done: new ParallelHook(),
  };
  async run() {                                       // 固定编译流程（骨架不可变）
    await this.hooks.beforeRun.promise(this);
    console.log('读取配置');
    await this.hooks.compile.promise(this);
    console.log('构建模块依赖图');
    await this.hooks.make.promise(this);
    console.log('产出 bundle');
    await this.hooks.emit.promise(this);
    await this.hooks.done.promise(this);
  }
}
// 插件 = 在切面 tap 注册逻辑的普通类（webpack 插件的全部秘密）
class HtmlPlugin {
  apply(compiler) {                                   // apply 即注入协议
    compiler.hooks.emit.tap('HtmlPlugin', (ctx) => {
      ctx.assets = { ...(ctx.assets || {}), 'index.html': '<html>...</html>' };
    });
  }
}
class SizePlugin {
  apply(compiler) {
    compiler.hooks.emit.tap('SizePlugin', (ctx) => {
      if (ctx.assets) for (const [f, c] of Object.entries(ctx.assets)) console.log(f, c.length, 'bytes');
    });
  }
}
// 装配
const compiler = new Compiler();
new HtmlPlugin().apply(compiler);
new SizePlugin().apply(compiler);
compiler.hooks.done.tap('report', () => console.log('构建完成'));
compiler.run();
// [tap:HtmlPlugin] before / [tap:SizePlugin] before / index.html 17 bytes / 构建完成
```
