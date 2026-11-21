---
title: [BLD-101] webpack 主流程源码导览——WebpackCLI 到 Compiler 到 Compilation 的类关系是怎样的？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-101：webpack 主流程源码导览——WebpackCLI 到 Compiler 到 Compilation 的类关系是怎样的？
**答**：
- webpack5 中 `lib/index.js` 只导出 `webpack/create` 函数：`webpack(options, callback)` 里 `new Compiler(options.context)` → `new WebpackOptionsApply().process(options, compiler)`，这一步按配置逐个 apply 内置插件（EntryOptionPlugin 注册 EntryPlugin、ExternalsPlugin、JavascriptModulesPlugin 等）。
- WebpackCLI（webpack-cli 包）只负责解析命令行、合并 `-c/--env`、加载配置文件，最终调用 `webpack()`，CLI 完全不参与编译；面试常考"webpack 与 webpack-cli 职责边界"。
- `compiler.run()` 触发 `hooks.run` → `compile()` 里 `newCompilationParams`（含 normalModuleFactory）→ `new Compilation()` → `hooks.make` 上 EntryPlugin 的回调执行 `compilation.addEntry()`，从此进入模块构建。
- 记忆画图：CLI → webpack() → OptionsApply 注册插件占位 → compiler.run → new Compilation → make/addEntry → build → seal → emit → done。

```javascript
// 主流程源码级复现：手写一个 20 行的"迷你 webpack 启动器"，展示关键调用链
const webpack = require('webpack');
const config = require('./webpack.config.js');

const compiler = webpack(config, (err, stats) => {
  // webpack5：stats 是编译结果句柄，err 只代表"流程级"错误（配置错误等）
  if (err) { console.error(err); return; }
  console.log(stats.toString({ colors: true, modules: false }));
});

// 等价拆解（webpack() 内部做的事）：
// 1. new Compiler(options.context)                 —— 创建全局单例
// 2. new NodeEnvironmentPlugin().apply(compiler)   —— 注入 fs/日志基础设施
// 3. for (const plugin of options.plugins) plugin.apply(compiler)
// 4. new WebpackOptionsApply().process(options, compiler)
//    —— EntryOptionPlugin: 按 entry 逐个 new EntryPlugin(context, entry, name).apply(compiler)
// 5. callback ? compiler.run(callback) : 编译器返回给调用方（多编译器 webpack([cfg1, cfg2]) 时各自 run）

// 关键 hooks 观测：验证"OptionsApply 注册插件"与"make 时才建 Compilation"的时序
const order = [];
compiler.hooks.entryOption.tap('Probe', () => (order.push('entryOption'), true));
compiler.hooks.beforeRun.tap('Probe', () => order.push('beforeRun'));
compiler.hooks.compile.tap('Probe', () => order.push('compile: 创建 compilationParams'));
compiler.hooks.make.tap('Probe', (compilation) => order.push('make: 开始 addEntry'));
compiler.hooks.afterSeal.tap('Probe', () => order.push('afterSeal'));
compiler.hooks.done.tap('Probe', () => console.log(order.join('\n')));
```
