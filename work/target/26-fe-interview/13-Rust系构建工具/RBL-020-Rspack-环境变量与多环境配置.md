---
title: [RBL-020] Rspack 项目如何管理环境变量与多环境配置？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-020：Rspack 项目如何管理环境变量与多环境配置？
**答**：
- 三层来源：process.env（构建机环境）、mode + DefinePlugin 注入的编译期常量、.env 文件体系（用 @rspack/core 内置 dotenv 语义或 rspack-cli 的 --env 参数）。
- 内置约定：mode: development/production/none 决定默认 optimization 与 DefinePlugin 的 NODE_ENV；业务常量用 DefinePlugin 注入 __APP_ENV__ 等。
- 与 Vite 的差异：Vite 用 import.meta.env + VITE_ 前缀约定，Rspack 走 webpack 的 DefinePlugin 风格，迁移 Vite 项目时注意访问方式改写。
- .env 加载：rspack-cli 支持 --env production 传入函数式 config；.env 文件需配合 dotenv-expand 自己加载再注入 DefinePlugin（或用 @rsbuild 这类上层框架内置）。
- 安全边界：所有注入都是字符串字面量替换，密钥会进产物，前端只放公开配置；私有配置走 BFF。
- 追问钩子：多环境产物用同一份代码+不同 DefinePlugin 注入构建，还是运行时配置接口？答案是尽量运行时，减少产物分叉。

```javascript
// rspack.config.js
const rspack = require('@rspack/core');
const dotenv = require('dotenv');
module.exports = (env) => {
  const cfg = dotenv.config({ path: `.env.${env.mode || 'development'}` }).parsed || {};
  const define = Object.fromEntries(
    Object.entries(cfg).map(([k, v]) => [`process.env.${k}`, JSON.stringify(v)])
  );
  return {
    mode: env.mode || 'development',
    plugins: [new rspack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(env.mode || 'development'),
      ...define,
    })],
  };
};
// 用法：rspack build --env mode=production
```
