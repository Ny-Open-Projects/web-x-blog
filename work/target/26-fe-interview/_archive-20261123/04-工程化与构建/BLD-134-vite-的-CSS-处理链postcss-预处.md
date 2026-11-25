---
title: [BLD-134] vite 的 CSS 处理链：postcss、预处理器、CSS Modules 与构建期 CSS 拆分行为。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-134：vite 的 CSS 处理链：postcss、预处理器、CSS Modules 与构建期 CSS 拆分行为。
**答**：
- dev 下 CSS 走 transform 钩子：`.css` 内置处理（含 postcss 配置自动发现 postcss.config.js），`.less/.scss` 先由 vite 内嵌的编译器（通过 `css.preprocessorOptions` 传参）转 CSS 再走同链路；产物以 JS 模块形式返回（style 注入，HMR 原生支持）。
- **CSS Modules**：`.module.css` 自动开启，导出映射对象 `style.a`；`css.modules.localsConvention` 控制命名（camelCase），`generateScopedName` 自定义 hash——面试常问"vite 不需要配 css-loader 是因为内置了 postcss-modules"。
- **build 期 CSS 提取**：rollup 产 JS 后 `vite:build-css-plugin` 把所有 CSS 从模块中抽出合并，按 chunk 拆分（`build.cssCodeSplit: true` 默认），异步 chunk 的 CSS 在动态 import 时由 vite 自动注入对应 `<link>`（与 webpack 的 MiniCssExtract 差异点）。
- 常见坑：库文件不写 `.module` 导致全局污染；`cssCodeSplit: false` 时单文件全量 CSS；preprocessorOptions.additionalData 注入变量文件的重复编译成本。

```javascript
// vite.config.ts：CSS 全链路配置
export default defineConfig({
  css: {
    postcss: {
      plugins: [
        require('autoprefixer')(),
        require('postcss-preset-env')({ features: { 'nesting-rules': true } }),
      ],
    },
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/styles/var.scss" as *;`, // 注入变量（@use 而非 @import）
        api: 'modern-compiler',                            // 用现代编译器 API，速度更快
      },
      less: { math: 'always', javascriptEnabled: true },
    },
    modules: {
      localsConvention: 'camelCaseOnly',   // style['brand-color'] → style.brandColor
      generateScopedName: 'vp-[name]__[local]--[hash:base64:5]',
    },
    // devtools: true（新版本）可映射源码位置
  },
  build: {
    cssCodeSplit: true,        // 异步 chunk 的 CSS 随 chunk 拆分，import 时自动注入 link
    cssTarget: 'chrome87',     // CSS 单独指定压缩目标（esbuild/minify CSS）
    // cssCodeSplit: false → 单一 style.css，适合"纯静态落地页"或需要手动引入的场景
  },
});
// 产物验证：异步路由组件 → dist/assets/Xxx-[hash].css + JS 中 import 该 css 的注入逻辑
```
