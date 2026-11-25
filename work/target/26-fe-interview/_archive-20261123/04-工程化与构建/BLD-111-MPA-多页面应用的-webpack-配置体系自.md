---
title: [BLD-111] MPA 多页面应用的 webpack 配置体系：自动扫描入口 + 公共 chunk 策略怎么设计？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-111：MPA 多页面应用的 webpack 配置体系：自动扫描入口 + 公共 chunk 策略怎么设计？
**答**：
- 入口自动扫描：约定 `src/pages/*/index.{js,ts}`，用 `fs.readdirSync` + glob 生成 `entry` 与 `HtmlWebpackPlugin` 列表，新增页面零配置——面试要能写出完整生成逻辑。
- 公共 chunk 三层策略：`vendors`（node_modules 单独抽）、`common`（pages 间被 ≥2 引用的模块 `splitChunks.cacheGroups.common`）、runtime 单独抽（`runtimeChunk: 'single'`，多页共享且利于长效缓存）。
- HTML 模板按页面可覆盖：`pages/<name>/index.html` 存在则用之，否则回落全局模板；每页注入自己的 chunk（`chunks: [name]` + runtime + vendors）。
- 坑：多页共享的 splitChunks `minChunks` 需按页数调整；HTML 数量多时构建慢（可用 html-webpack-plugin 的 childCompilationHookName? 缓存或并发插件）。

```javascript
// webpack.mpa.config.js：生产级多页配置生成器
const fs = require('fs');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const glob = require('glob');

function collectPages(dir) {
  // 约定：src/pages/<pageName>/index.{tsx,js} + 可选 <pageName>/index.html
  return glob
    .sync(`${dir}/*/index.{tsx,js}`)
    .map((entry) => {
      const name = path.basename(path.dirname(entry));
      const tpl = `${path.dirname(entry)}/index.html`;
      return { name, entry, tpl: fs.existsSync(tpl) ? tpl : `${dir}/_template.html` };
    });
}

module.exports = (env, argv) => {
  const pages = collectPages(path.resolve(__dirname, 'src/pages'));
  const pageNames = pages.map((p) => p.name);
  const isProd = argv.mode === 'production';

  return {
    entry: Object.fromEntries(pages.map((p) => [p.name, { import: p.entry, filename: `js/${p.name}.[contenthash].js` }])),
    output: { path: path.resolve(__dirname, 'dist'), clean: true, publicPath: isProd ? '//cdn.example.com/m/' : '/' },
    optimization: {
      runtimeChunk: 'single',                       // 所有页面共享一个 runtime，可长效缓存
      splitChunks: {
        chunks: 'initial',
        cacheGroups: {
          vendors: { test: /[\\/]node_modules[\\/]/, name: 'vendors', priority: 10, enforce: true },
          // 页面间公共代码：至少 2 个页面用到才抽，避免负优化
          common: { name: 'common', minChunks: 2, minSize: 30 * 1024, priority: 5, reuseExistingChunk: true },
        },
      },
    },
    plugins: pages.map(
      (p) =>
        new HtmlWebpackPlugin({
          filename: `${p.name}.html`,
          template: p.tpl,
          chunks: ['runtime', 'vendors', 'common', p.name], // 顺序即注入顺序
          chunksSortMode: 'manual',
          minify: isProd ? { collapseWhitespace: true } : false,
        })
    ),
  };
};
```
