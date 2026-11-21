---
title: [OPS-079] 报错如何与版本（release）关联？怎么定位"哪次发布引入"？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-079：报错如何与版本（release）关联？怎么定位"哪次发布引入"？
**答**：
- 双向绑定：构建时把版本号写进产物（window.__APP_VERSION__），运行时 Sentry init 带同一 release；CI 上传 map 用同一版本号——三处一致是命门。
- 版本号来源：git sha 短哈希 + 构建号（如 20261101.42-abc1234），保证唯一可追溯。
- Sentry 的 release 页自动给出：该版本新出现的 issue（new issues）、回归 issue（regressed）、崩溃用户数，"引入版本"一目了然。
- 发布事件（deploys）关联后，还能做"发布前后错误率对比"，自动判定发布质量。

```javascript
// webpack.config.js：版本贯穿构建、运行时、Sentry
const { defineConfig } = require('webpack');
const { WebpackPluginSentry } = require('sentry-webpack-plugin'); // 示意插件名
const { execSync } = require('child_process');

// 版本号三要素：日期.构建号.git短哈希
const GIT_SHA = execSync('git rev-parse --short HEAD').toString().trim();
const APP_VERSION = `${process.env.BUILD_NUMBER ?? '0'}.${GIT_SHA}`;

module.exports = defineConfig({
  output: {
    filename: 'assets/[name].[contenthash:8].js',
  },
  plugins: [
    new (require('webpack').DefinePlugin)({
      '__APP_VERSION__': JSON.stringify(APP_VERSION),   // 1. 运行时可见版本
    }),
    new WebpackPluginSentry({
      release: APP_VERSION,                             // 2. 构建时上传 map 用同一版本
      urlPrefix: '~/assets',
      include: './dist',
      cleanArtifacts: true,                             // 上传后清理产物中的 map
      setCommits: { auto: true },
    }),
  ],
});

// 3. 运行时：Sentry.init({ release: window.__APP_VERSION__ }) 与上面严格一致
// Sentry 后台 release 页即可看到 new issues / regressed / 崩溃用户数
```
