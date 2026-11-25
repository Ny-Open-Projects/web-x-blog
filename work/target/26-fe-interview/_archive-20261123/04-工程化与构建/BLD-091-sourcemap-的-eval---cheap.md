---
title: [BLD-091] sourcemap 的 eval / cheap / module / nosources 各修饰符含义是什么？生产怎么选？（高频）
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-091：sourcemap 的 eval / cheap / module / nosources 各修饰符含义是什么？生产怎么选？（高频）
**答**：
- eval：模块包在 eval 执行，映射指向转换后代码，快但可能"不精确"；不生成 .map 文件（性能最好，调试粒度最粗）。
- cheap：只映射到行不映射到列；module：映射到"原始源码"（TS/JSX 编译前），没有它调试的是 babel 产物；nosources：只有映射无源码内容（省体积，配合外部上传）。
- 组合逻辑：[生成速度] eval-* 最快；[质量] source-map 全量最准；常见 dev 用 eval-cheap-module-source-map（重编译快 + 能看原始代码），生产用 hidden-source-map 或 nosources-source-map 上传到监控平台。
- 生产安全：source-map 直接暴露等于泄露源码——options：hidden（生成不引用）+ Sentry 上传、或干脆不开。

```javascript
// webpack.config.js：devtool 选择矩阵
module.exports = (_, argv) => ({
  devtool: argv.mode === 'development'
    ? 'eval-cheap-module-source-map' // 快速 rebuild + 可见原始源码
    : 'hidden-source-map',           // 生成 .map 但产物不引用 上传 Sentry 后删除
});

// text 代码块：常见组合速查
// eval                    快   转换后代码  无 map 文件
// eval-source-map         较快 原始源码    内嵌 dataURI map
// eval-cheap-source-map   快   转换后代码  仅行级
// eval-cheap-module-source-map   快  原始源码  仅行级   <- 开发推荐
// source-map              慢   全量列级 原始源码 独立 .map  <- 需要精确上报时
// hidden-source-map       慢   同 source-map 但不引用  <- 生产 + 监控平台
// nosources-source-map    中   有映射无源码内容       <- 生产 可公开
```

```javascript
// Sentry 上传 sourcemap 的 CI 片段（bash 代码块风格用 js 演示）
// scripts/upload-sourcemaps.js
const { execSync } = require('child_process');

execSync(`
  npx @sentry/cli sourcemaps inject ./dist &&
  npx @sentry/cli sourcemaps upload --release ${process.env.GIT_SHA} ./dist &&
  find ./dist -name "*.map" -delete &&           # 上传后删除本地 map 防泄露
  find ./dist -name "*.js" -exec sed -i '' '/sourceMappingURL/d' {} +
`, { stdio: 'inherit' });
```
