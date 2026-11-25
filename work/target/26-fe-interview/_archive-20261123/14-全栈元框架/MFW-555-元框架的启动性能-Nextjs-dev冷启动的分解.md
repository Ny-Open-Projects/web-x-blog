---
title: [MFW-555] Next.js dev 冷启动分解：从 npm start 到首请求的管线
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-555：Next.js dev 冷启动分解

**答**:
- dev 冷启动的阶段分解：1) 配置加载 + 路由扫描（文件系统遍历 RBL-524）；2) **依赖预打包**（external 包预 bundle——esbuild/turbopack：node_modules 的 ESM/CJS 转换 RBL-616）；3) 编译器启动（Turbopack/webpack 初始化）；4) 首请求按需编译（路由闭包编译——lazy graph RBL-551）；5) 数据连接初始化。
- 各阶段的优化：1) 路由扫描缓存（manifest 持久化——文件变更事件增量更新而非重扫）；2) 预打包缓存（node_modules/.cache 持久化——依赖不变秒过 RBL-617）；3) 首请求编译（持久缓存 + 并行编译）。
- 「启动时长」的度量与 SLO（RBL-904 平台 SLI）：npm start → 首请求 200 OK 的墙钟时间；大仓 dev 启动 30s+ 是 DX 主要痛点。
- 追问钩子：为什么「依赖预打包」是 dev 冷启动的最大块且缓存收益最大？——node_modules 的模块转换（CJS→ESM/语法降级）在无缓存时占启动 60%+（esbuild 快但依赖树大：lodash 链/node polyfill——一次预打包 30s）；缓存后 = 0（依赖不变 RBL-617 失效判定：lockfile hash——「锁文件作为缓存键」与 RBL-582 一致）——dev 启动的缓存策略与 CI 缓存策略完全同构。

```javascript
// dev 冷启动画像
const DEV_STAGES = [
  { stage: 'config+routes', ms: 400, cacheable: false },
  { stage: 'deps-prebundle', ms: 12000, cacheable: true, key: 'lockfile-hash' },  // 最大块
  { stage: 'compiler-init', ms: 800 },
  { stage: 'first-request', ms: 3000, cacheable: true, key: 'route-closure' },
  { stage: 'db-connect', ms: 200 },
];
// 缓存后的启动 = 非 cacheable 部分之和 ≈ 1.4s（12s→0.2s 缓存命中）
// persistCache 目录策略
// node_modules/.cache/next-dev/
//   deps-bundle/         ← esbuild 预打包产物（lockfile hash 键）
//   routes-manifest.json ← 路由清单（fs watcher 增量）
// 失效判定
function needsRebundle(lockHash, cacheMeta) {
  return cacheMeta?.lockHash !== lockHash || cacheMeta?.toolVersion !== VERSION;
}
```
