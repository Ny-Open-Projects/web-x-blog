---
title: [RBL-033] 如何给 Rspack 构建实现进度显示与日志分级？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-033：如何给 Rspack 构建实现进度显示与日志分级？
**答**：
- 进度：内置 ProgressPlugin（CLI 自带条形输出），可自定义回调拿百分比与当前阶段（resolve/parse/emit）文案；自研看板用钩子自己聚合。
- 日志分级：infrastructureLogging.level（none/error/warn/info/log/verbose）控制基础设施日志；stats 字段控制产物报告详细度（preset minimal/errors-only 等）。
- CI 场景：进度条关闭（非 TTY 自动）、stats errors-only 减噪、错误输出完整堆栈 + 相关模块链。
- 自定义看板：done 钩子把 stats 关键指标（时长/模块数/产物体积/错误数）写进日志系统或上报，做多项目构建质量跟踪。
- 原理：进度与日志都是钩子数据的"消费端"，不影响构建本身；开 profile 模式才有 per-module 计时。
- 追问钩子：verbose 日志会显著拖慢大项目构建，只在排障时开。

```javascript
// rspack.config.js
const rspack = require('@rspack/core');
module.exports = {
  infrastructureLogging: { level: 'warn' },
  stats: 'errors-warnings',
  plugins: [
    new rspack.ProgressPlugin((percent, msg) => {
      // 接自研看板
      if (process.env.CI) console.log(`[rspack] ${(percent * 100).toFixed(0)}% ${msg}`);
    }),
    {
      apply(compiler) {
        compiler.hooks.done.tap('BuildReport', (stats) => {
          const s = stats.toJson({ modules: false });
          console.log(JSON.stringify({ time: s.time, assets: s.assets.length, errors: s.errors.length }));
        });
      },
    },
  ],
};
```
