---
title: [BLD-148] 库构建选型：tsup / unbuild / 纯 rollup + tslib 怎么选？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-148：库构建选型：tsup / unbuild / 纯 rollup + tslib 怎么选？
**答**：
- **tsup**（esbuild 内核）：配置最少、速度最快，开箱出 cjs/esm/iife + dts（调 tsc）+ preserveModules；适合中小 TS 库的"零心智"方案，深度定制（复杂钩子）受限。
- **unbuild**（rollup 内核，Nuxt 系）：约定式配置（stub 模式链接本地包做 dev）、自动生成 stubs 与 cjs/esm 双产物、内置 mkdist（按文件转译，适合 UI 库源码直出）；适合 Nuxt/monorepo 生态。
- **纯 rollup**：插件生态最全（dts、svg、postcss、多 pass），一切可定制；代价是配置与维护成本最高，适合有特殊产物需求（SFC、样式、多入口、UMD）的组件库。
- **tslib**：不是构建器而是 runtime helper 库——`import tslib from 'tslib'` 让 tsc/rollup 产出的代码复用 `__awaiter/__extends` 等 helper，`importHelpers: true` 减少每个文件的内联重复；与构建器是配合关系。

```javascript
// 三种方案的等价配置对照（同一个库：esm+cjs+dts）
// ── 方案一：tsup（package.json scripts: "build": "tsup"）──
// tsup.config.ts
import { defineConfig } from 'tsup';
export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,                  // 自动跑 tsc 出 d.ts
  splitting: true,            // esm 共享 chunk
  clean: true, external: [/^react/],
});

// ── 方案二：unbuild（scripts: "build": "unbuild"）──
// build.config.ts
import { defineBuildConfig } from 'unbuild';
export default defineBuildConfig({
  entries: ['src/index'],
  declaration: true,
  rollup: { emitCJS: true, esbuild: { target: 'es2020' } },
  stub: true,                 // dev 模式：产物 stub 指向源码，改库即时生效
});

// ── 方案三：tsc 直出 + tslib（传统最大化控制）──
// tsconfig.json
// {
//   "compilerOptions": {
//     "importHelpers": true,            // helper 从 tslib 引，产物更小
//     "declaration": true, "target": "ES2020", "module": "NodeNext"
//   }
// }
// 产物： import { __awaiter } from "tslib";   ← 配合 dependencies: { tslib: "^2.6.0" }
```

## 十六章 esbuild / SWC 与新工具实践（BLD-149 ~ BLD-156）
