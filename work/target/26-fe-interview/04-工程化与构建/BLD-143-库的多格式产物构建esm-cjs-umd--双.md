---
title: [BLD-143] 库的多格式产物构建：esm/cjs/umd + 双 package.json + exports 映射。（高频）
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-143：库的多格式产物构建：esm/cjs/umd + 双 package.json + exports 映射。（高频）
**答**：
- 现代规范用一个 package.json 的 `exports` 条件映射解决多格式：`import` → esm、`require` → cjs、`types` 指向 d.ts；**Node 与打包器按条件顺序取第一个匹配**，types 必须放前面（TS 解析）。
- 双 package.json（旧方案/monorepo 里仍常见）：根 package.json main 指向 cjs，`module` 指向 esm（webpack 系消费），esm 目录里再放一个 package.json 标 `type: 'module'`（让 Node 原生把 .js 当 ESM）。
- UMD 现在只给"直接 script 引入"的场景（CDN/无构建页），浏览器环境建议额外出 `dist/umd/index.min.js`（iife/umd 格式 + name）。
- 坑：`type: 'module'` 与 cjs 共存时扩展名规则（.cjs/.mjs）；exports 会**封闭深层路径**，需要 `./package.json`、`./dist/*` 通配显式放行。

```json
// package.json：单包多格式现代方案（Node 12.7+/主流打包器全支持）
{
  "name": "my-lib",
  "version": "1.0.0",
  "type": "module",
  "main": "./dist/index.cjs",                       // 兜底（老 Node/工具）
  "module": "./dist/index.js",                      // 打包器偏好 esm
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",                 // TS 优先取 types 条件
      "import": "./dist/index.js",                  // esm
      "require": "./dist/index.cjs",                // cjs（Node）
      "default": "./dist/index.js"
    },
    "./package.json": "./package.json",             // 显式放行，否则深层路径全被封闭
    "./*": "./dist/*"                               // 允许子路径导入（工具函数子模块）
  },
  "sideEffects": false,                             // 摇树契约：全库无副作用
  "files": ["dist"],
  "engines": { "node": ">=18" }
}
```

```javascript
// rollup.config.mjs：一次产出三格式（type: module 项目用 .mjs 保 cjs 产出合法）
import { defineConfig } from 'rollup';
import esbuild from 'rollup-plugin-esbuild';
import dts from 'rollup-plugin-dts';

export default defineConfig([
  {
    input: 'src/index.ts',
    plugins: [esbuild({ target: 'es2020' })],
    external: (id) => !id.startsWith('.') && !id.startsWith('/'),  // 全外部化
    output: [
      { format: 'esm', file: 'dist/index.js', sourcemap: true },
      { format: 'cjs', file: 'dist/index.cjs', sourcemap: true, exports: 'named' },
      { format: 'umd', file: 'dist/umd/index.min.js', name: 'MyLib',
        plugins: [/* terser/esbuild minify */] },
    ],
  },
  {
    input: 'dist/index.d.ts',       // 第二轮：用已生成的类型做聚合
    plugins: [dts()],
    output: { format: 'esm', file: 'dist/index.d.ts' },
  },
]);
// 双 package.json 旧方案对照（monorepo tsc 直出时）：
// dist/esm/package.json: { "type": "module" }   dist/cjs/package.json: { "type": "commonjs" }
```
