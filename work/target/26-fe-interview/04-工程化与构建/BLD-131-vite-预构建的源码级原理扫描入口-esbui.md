---
title: [BLD-131] vite 预构建的源码级原理：扫描入口、esbuild 打包 deps、缓存校验三步。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-131：vite 预构建的源码级原理：扫描入口、esbuild 打包 deps、缓存校验三步。
**答**：
- **扫描**：`optimizer.scanImports` 用 esbuild 的 `build({ write: false, plugins: [esbuildScanPlugin] })` 从 `optimizeDeps.entries`（默认 index.html）出发，把入口 HTML 里引用的模块全部扫一遍，收集**裸导入**（bare import，即 node_modules 依赖）——只扫描不产出。
- **打包**：对收集到的依赖跑第二次 esbuild build（`splitting: true` 产 ESM chunk），把 CJS 依赖转 ESM、把众多小模块合并、把互为依赖的包打平（如 react/react-dom/scheduler 共享 chunk）；产物写 `node_modules/.vite/deps/`，同时生成 `_metadata.json`（依赖 hash 与 chunk 映射）。
- **缓存校验**：对比 `lockfileHash + configHash + lockfile 内容`（`getDepHash`），一致则跳过预构建直接用缓存；不一致删目录重建。运行中新增依赖 → 处理不到 → "optimized deps changed" full-reload 重跑预构建。
- 面试要点：为什么不用 vite 的 transform 管道直接服务 node_modules——CJS 互引用、几百个小请求（lodash-es 数百文件）会让 dev 页面加载失控。

```javascript
// 预构建三步的源码级对照（optimizer/index.ts 精简）
async function optimizeDeps(config, server) {
  // ① scan：esbuild 扫描器（esbuildScanPlugin 拦截 resolve，收集裸导入）
  const { deps, missing } = await scanImports(config);
  // deps 形如 { react: 'node_modules/react/index.js', 'lodash-es': '...' }

  // ② 缓存校验：getDepHash = hash(lockfile + config 相关字段)
  const depHash = getDepHash(config);           // 含 optimizeDeps 配置 + lockfile 内容
  const data = loadCachedDepInfo(depHash);      // 读 node_modules/.vite/deps/_metadata.json
  if (data && data.hash === depHash && data.browserHash) {
    return data;                                 // 命中：跳过打包
  }

  // ③ esbuild 打包依赖（flatIdDedupe 处理同名多版本 → 别名去重）
  await esbuild.build({
    entryPoints: Object.values(flatIdDedupe(deps)),
    bundle: true, splitting: true, format: 'esm',
    outdir: depsCacheDir,                        // node_modules/.vite/deps/
    external: config.optimizeDeps.exclude,       // external 的包运行时按需 vite 化
    plugins: [esbuildCjsInteropPlugin],          // CJS → ESM interop（__esModule 处理）
  });
  // 产物 metadata 记录每个依赖对应 chunk 与 browserHash（import 重写的 ?v= 值）
}
// 常用命令：vite optimize / vite --force 强制重建
```
