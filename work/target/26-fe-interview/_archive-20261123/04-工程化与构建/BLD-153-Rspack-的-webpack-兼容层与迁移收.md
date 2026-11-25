---
title: [BLD-153] Rspack 的 webpack 兼容层与迁移收益：哪些能直接用、哪些要适配？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-153：Rspack 的 webpack 兼容层与迁移收益：哪些能直接用、哪些要适配？
**答**：
- **兼容现状**（截至 2026 常态）：核心配置（entry/output/module.rules/optimization 常用项）、主流 loader（babel-loader? 更常见 swc-loader、css-loader、less/sass-loader）、常用 API（tapable 形态的 compiler/compilation 钩子）可用；官方保证"高频配置兼容"而非全量。
- **需适配项**：复杂自定义 plugin（部分钩子缺失/行为差异）、依赖 Node API 深度操作的 loader（Rspack 内核 Rust，loader 仍在 JS 跑但沙箱差异）、个别插件等价物（CopyPlugin 等内置化）、experiments 选项（css 异步模块等新语义）。
- 收益实测项清单（面试汇报结构）：冷启动、二次构建（缓存）、watch 增量、产物体积 diff（与 webpack 应一致，需 diff 确认）、生态功能回归（MF/CSS chunk/HMR 时序）。
- 迁移路径：Rsbuild（上层框架，约定式）vs Rspack（直接换内核，配置渐进兼容）——存量 webpack 项目选 Rspack + @rspack/cli 改造成本最低。

```javascript
// 迁移评估用的兼容性探测脚本：scripts/rspack-compat-check.js
const cfg = require('../webpack.config.js');
const issues = [];
for (const rule of cfg.module?.rules ?? []) {
  const l = typeof rule.use === 'string' ? rule.use : rule.use?.[0]?.loader ?? rule.loader;
  if (l && !/swc|css|style|less|sass|postcss|asset|babel/.test(l)) {
    issues.push(`loader 待确认: ${l}`);
  }
}
const RSPACK_BUILTIN = ['HtmlWebpackPlugin', 'CopyPlugin', 'DefinePlugin', 'TerserPlugin'];
for (const p of cfg.plugins ?? []) {
  const n = p.constructor.name;
  if (RSPACK_BUILTIN.includes(n)) issues.push(`${n} → 换 rspack 内置/等价物`);
}
console.log(issues.length ? issues.join('\n') : '基础兼容，进入实测阶段');
```

```javascript
// 迁移后的 rspack.config.js（webpack5 配置的最小改动示例）
module.exports = {
  entry: './src/index.tsx',
  output: { filename: '[name].[contenthash].js', clean: true },
  resolve: { extensions: ['.tsx', '.ts', '.js'], alias: { '@': '/src' } },
  module: {
    rules: [
      { test: /\.tsx?$/, use: { loader: 'builtin:swc-loader',  // 内置 swc 替代 babel-loader
        options: { jsc: { parser: { syntax: 'typescript', tsx: true }, target: 'es2020' } } } },
      { test: /\.css$/, type: 'css/module',        // experiments.css：Rspack 内置 CSS 管线（可选新路径）
        },
      { test: /\.png$/, type: 'asset/resource' },
    ],
  },
  optimization: { splitChunks: { chunks: 'all' }, realContentHash: true },
  plugins: [new rspack.HtmlRspackPlugin({ template: './index.html' })],  // 内置 HTML 插件
  experiments: { css: true },
  devServer: { hot: true },
  // 兼容开关：rspack 保持对 webpack-plugin 的执行沙箱，不兼容时回退 webpack5
};
```
