---
title: [BLD-169] 构建期常量注入的滥用风险：DefinePlugin 注入 JSON 的那些坑。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-169：构建期常量注入的滥用风险：DefinePlugin 注入 JSON 的那些坑。
**答**：
- 坑一 **JSON 引号与转义**：`new DefinePlugin({ __CFG__: cfg })` 若 cfg 是对象需 `JSON.stringify`；注入字符串忘加引号会变成变量引用（运行时 ReferenceError）；注入含 `</script>` 的文案会**破坏 HTML 内联产物**（需要 `JSON.stringify(x).replace(/</g, '\\u003c')`）。
- 坑二 **引用点替换语义**：define 只替换**代码文本**，`obj.a === process.env.X`、`typeof process.env.X`、动态 key 都不符合预期；`typeof __CFG__` 在某些替换路径下仍是 object 假阳性。
- 坑三 **体积与安全**：大对象注入等于把数据打包进每个引用文件（应生成虚拟模块让产物只打包一次）；把非公开配置注入前端产物即泄露（与 BLD-139 同源）。
- 正确姿势：结构化配置走 virtual module（onLoad/env-ns）而非 define；define 只留少量原始标量（NODE_ENV、版本号、feature flag 布尔）。

```javascript
// 反模式 → 正确姿势对照
const webpack = require('webpack');
const appConfig = require('./config/app.json'); // 10KB 的业务配置

module.exports = {
  plugins: [
    // ── 反模式一：直接注入对象（未 stringify → 变量引用，运行时崩） ──
    // new webpack.DefinePlugin({ __CFG__: appConfig }),
    // ── 反模式二：stringify 了但含 </script>（HTML 内联产物被截断） ──
    // new webpack.DefinePlugin({ __CFG__: JSON.stringify(appConfig) }),

    // ── 正确姿势一：标量进 define，且转义 < ──
    new webpack.DefinePlugin({
      'process.env.BUILD_VERSION': JSON.stringify(process.env.BUILD_VERSION ?? 'dev'),
      __FEATURE_NEW_CHECKOUT__: JSON.stringify(true),
      // 转义防 HTML 截断（若确需注入字符串）：
      // __MSG__: JSON.stringify(msg).replace(/\u2028|\u2029/g, m => '\\u' + m.charCodeAt(0).toString(16)),
    }),

    // ── 正确姿势二：结构化配置走虚拟模块（产物只含一次，且可 tree-shake） ──
    // esbuild/rollup 用 onLoad；webpack 用 virtual module 等价实现：
    new webpack.NormalModuleReplacementPlugin(/^app-config$/, (res) => {
      res.request = path.resolve('config/app.build.js');   // 构建期选择真实配置文件
    }),
  ],
};
// 虚拟模块产物收益：import cfg from 'app-config' 只在用到的 chunk 打包一份；
// define 注入大 JSON 则会在**每个引用文件**重复出现（bundle 体积按引用次数翻倍）。
```
