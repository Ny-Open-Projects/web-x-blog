---
title: [BLD-090] polyfill 与 targets：browserslist 全解 + Vite legacy 插件原理。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-090：polyfill 与 targets：browserslist 全解 + Vite legacy 插件原理。
**答**：
- browserslist：统一的"目标浏览器"声明，babel、postcss（autoprefixer）、esbuild、Vite 都读它——一处声明全链路生效；配置于 package.json 或 .browserslistrc，支持 queries（"> 0.5%", "not dead"）与 coverage。
- 组合语义：默认 queries 之间是 or；`and` 精确交集；`not dead` 排除无人用的版本；环境变量 BROWSERSLIST_ENV 或按 env 区分 dev/prod。
- Vite legacy 插件原理：额外用 @babel/preset-env 生成"降级版"bundle + SystemJS 运行时，index.html 注入 nomodule/module 双 script，现代浏览器只加载原生版。
- 验证手段：npx browserslist 输出目标集、browserslist --coverage、产物跑一次 grep core-js。

```bash
# .browserslistrc：完整示例
# 生产目标
defaults and supports es6-module and not dead

# 查询验证命令
npx browserslist
npx browserslist --coverage   # 当前目标覆盖全球用户百分比
npx browserslist "chrome > 80 and last 2 versions"
```

```json
// package.json：区分环境的 browserslist
{
  "browserslist": {
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version"]
  }
}
```

```javascript
// vite.config.js：legacy 插件完整配置
import { defineConfig } from 'vite';
import legacy from '@vitejs/plugin-legacy';

export default defineConfig({
  plugins: [
    legacy({
      targets: ['chrome >= 64', 'safari >= 12'],
      additionalLegacyPolyfills: ['regenerator-runtime/runtime'], // async/await 兜底
      modernPolyfills: ['es.array.at'], // 现代浏览器也按需补少数新 API
      renderLegacyChunks: true,
    }),
  ],
});

// index.html 产物注入效果（text 代码块）：
// <script type="module" src="/assets/index.mjs"></script>          现代浏览器
// <script nomodule src="/assets/index-legacy.js"></script>          旧浏览器 + SystemJS 注册表
```
