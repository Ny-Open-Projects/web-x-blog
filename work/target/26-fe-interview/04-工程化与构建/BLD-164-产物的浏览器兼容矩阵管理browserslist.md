---
title: [BLD-164] 产物的浏览器兼容矩阵管理：browserslist 到各构建工具的联动全解。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-164：产物的浏览器兼容矩阵管理：browserslist 到各构建工具的联动全解。
**答**：
- 单一事实源：项目根的 `browserslist` 配置被 **babel（preset-env）、postcss/autoprefixer、vite（build.target）、terser/esbuild（语法降级目标）、core-js（polyfill 注入量）** 共同消费——改一处矩阵，全链路产物目标同步变化。
- 联动缺口与补法：vite 的 `build.target` 与 browserslist 不是自动同步的（vite 有自己的 esbuild target），需要插件（如 `browserslist-to-esbuild`）桥接；webpack 需要 `@babel/preset-env` 读 browserslist、terser 的 `ecma` 手动对齐。
- 矩阵治理：季度 review 覆盖率（`browserslist --coverage`）、dead browser 淘汰（`not dead`）、灰度新目标（先 `defaults` 后收紧）；降级产物（legacy build 双份 + `nomodule`）是矩阵的执行手段之一。
- 验证：`npx browserslist` 列出实际命中、`esbuild --target` 与 babel debug 输出对比、产物跑 `eslint-plugin-compat`? （源码层 API 检查）。

```json
// package.json：兼容矩阵（单一事实源）
{
  "browserslist": [
    "defaults",                    // >0.5%, last 2 versions, Firefox ESR, not dead
    "not op_mini all",
    "maintained node versions"
  ]
}
```

```javascript
// vite.config.ts：把 browserslist 桥接进 esbuild target（消除联动缺口）
import browserslistToEsbuild from 'browserslist-to-esbuild';
export default defineConfig({
  build: {
    // 未桥接的坑：vite 默认 target 'modules'（es2020 基线）与 browserslist 的 ie11 目标脱节
    target: browserslistToEsbuild(),     // 读 package.json 的 browserslist → esbuild 目标数组
    cssTarget: browserslistToEsbuild(),  // CSS 压缩目标同样对齐
  },
});
// webpack 侧对齐检查（webpack.config.js）：
// babel: preset-env 不写 targets（自动读 browserslist）
// terser: terserOptions.ecma = 2018（按矩阵下限手写或脚本生成）
// autoprefixer/postcss-preset-env：自动读 browserslist（零配置联动）
// 产物验证链：
//   npx browserslist --coverage        覆盖率报告
//   npx esbuild --target=es2015 --bundle app.js   模拟矩阵下限编译
//   grep -r "async function" dist/     目标含 es2017+ 时产物应保留 async（未转译即目标正确）
```
