---
title: [BLD-135] vite 的静态资源处理链：import asset 到 url、base64 内联与 manifest。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-135：vite 的静态资源处理链：import asset 到 url、base64 内联与 manifest。
**答**：
- 规则：`assetsInclude` 判定资源类型后，dev 下 import 返回 URL 字符串（`/src/logo.png`），build 下按 `build.assetsInlineLimit`（默认 4096B）决定**内联 base64** 或发射文件（`assets/[name]-[hash][extname]`，hash 保证缓存稳定）。
- 显式控制：`?url` 强制返回 URL、`?raw` 返回源码字符串、`?inline`（新版本）强制内联；`public/` 目录资源不经处理直接 copy，引用用**绝对路径**（`/favicon.ico`），不参与 hash——这是"public 里的文件更新后浏览器缓存不刷新"的原因。
- `new URL('./img.png', import.meta.url)` 语法 vite 原生支持（worker 场景必须用它而非 import），build 期同样发射并重写。
- manifest：`build.manifest: true` 生成 `.vite/manifest.json`（源路径→产物路径+hash+css 依赖），供后端 SSR/传统模板注入资源使用。

```javascript
// vite.config.ts：静态资源完整配置
export default defineConfig({
  publicDir: 'public',
  assetsInclude: ['**/*.glsl', '**/*.mp4'],       // 扩展可 import 的资源类型
  build: {
    assetsInlineLimit: (filePath, content) => {
      // 4KB 以下内联；但 svg 一律不内联（想走缓存）或一律内联（减少请求）按需定制
      if (filePath.endsWith('.svg')) return false;
      return content.length < 4096;
    },
    manifest: true,           // dist/.vite/manifest.json
    rollupOptions: { output: { assetFileNames: 'assets/[name]-[hash].[ext]' } },
  },
});
// 源码中的三种写法及其产物：
// import logo from './logo.png'        → 小图: data:image/png;base64,...；大图: /assets/logo-3f2a.png
// import txt from './a.md?raw'         → 模块导出原始字符串（构建期内联）
// import url from './big.mp4?url'      → 强制 URL（即使小于内联阈值）
// const u = new URL('./w.js', import.meta.url)  → worker 入口，build 期发射独立 chunk
// public/favicon.ico                   → 原样 copy 到 dist 根，无 hash，代码里写死 '/favicon.ico'
// manifest.json 片段：
// { "src/logo.png": { "file": "assets/logo-3f2a91b2.png", "src": "src/logo.png",
//   "isEntry": false, "css": [] } }
```
