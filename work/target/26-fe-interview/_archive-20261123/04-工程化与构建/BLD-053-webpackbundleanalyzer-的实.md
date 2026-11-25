---
title: [BLD-053] webpack-bundle-analyzer 的实操与读图方法？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-053：webpack-bundle-analyzer 的实操与读图方法？
**答**：
- 两种模式：构建后生成静态报告（stats 文件 + analyzer 静态页，适合 CI）与 dev 时实时面板；读图要点是 treemap 的面积 = gzip 前体积。
- 读图四步：找最大的单个模块（常是重复依赖或多语言包）、找应进异步 chunk 却在主包的三方库、找重复打包（同一库两个版本并排出现）、找可外部化的大文件。
- 配合 stats.json 用 `duplicate-package-checker-webpack-plugin` 或 `npm ls` 查重。
- 报告要纳入基线管理：CI 产出对比图，体积异常增长自动告警。

```bash
# 生成 stats 并产出静态报告
npx webpack --json > stats.json
npx webpack-bundle-analyzer stats.json dist -r report.html -m static --mode static

# 用压缩后体积看报告（更接近真实收益）
npx webpack --json > stats.json
npx webpack-bundle-analyzer stats.json dist --report report.html
```

```javascript
// webpack.config.js：CI 集成的分析插件配置
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = (_, argv) => ({
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: process.env.CI ? 'static' : 'server', // CI 出静态文件 本地起服务
      reportFilename: 'bundle-report.html',
      openAnalyzer: !process.env.CI,
      defaultSizes: 'stat',       // 可改 gzip 更贴近线上
      generateStatsFile: true,
      statsFilename: 'stats.json',
    }),
  ],
});
```
