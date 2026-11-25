---
title: [BLD-046] 构建慢如何定位？speed-measure-plugin 和 profiling 怎么用？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-046：构建慢如何定位？speed-measure-plugin 和 profiling 怎么用？
**答**：
- 先分桶：loader 耗时（可通过 stats 的 module.timings 看）、压缩耗时（terser 对大 chunk 慢）、插件耗时、resolve/IO 耗时。
- speed-measure-plugin 包裹 plugins 与 loaders 输出各阶段耗时表；webpack 5 官方方式：--profile + stats.json（profileTimings）或 NODE_OPTIONS="--cpu-prof" 火焰图。
- 常见元凶：babel-loader 处理了 node_modules、terser 没并行、sourceMap 全开、每个 rebuild 全量编译（未开缓存）。
- 定位后逐一治理并做基线：把每次优化写入 CI 耗时对比，防止回退。

```javascript
// webpack.config.js：speed-measure-plugin 用法 + webpack5 官方 profiling
const SpeedMeasurePlugin = require('speed-measure-webpack-plugin');
const smp = new SpeedMeasurePlugin();

module.exports = smp.wrap({
  module: {
    rules: [{
      test: /\.js$/,
      include: /src/,          // 不碰 node_modules 是最大提速
      use: 'babel-loader',
    }],
  },
  optimization: {
    minimizer: [new (require('terser-webpack-plugin'))({
      parallel: true,          // 多进程压缩
    })],
  },
});

// bash 代码块：webpack 5 官方定位命令
// npx webpack --profile --json > stats.json
// node -e "const s=require('./stats.json');
//   console.table(s.modules.map(m=>({name:m.name,time:m.time})).sort((a,b)=>b.time-a.time).slice(0,10))"
// NODE_OPTIONS=--cpu-prof npx webpack   # 生成 .cpuprofile 用 Chrome DevTools 看火焰图
```
