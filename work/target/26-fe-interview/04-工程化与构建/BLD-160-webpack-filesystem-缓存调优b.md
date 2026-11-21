---
title: [BLD-160] webpack filesystem 缓存调优：buildDependencies 与 snapshot 管理细节。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-160：webpack filesystem 缓存调优：buildDependencies 与 snapshot 管理细节。
**答**：
- 调优三件套：`cache.name` 隔离场景（dev/test/build 各一份）；`buildDependencies.config` 必须含配置文件与关键 json（漏了就是脏缓存重灾区）；`managedPaths` 把 node_modules（pnpm 加 .pnpm 路径）纳入信任区，快照对比跳过海量文件。
- snapshot 策略：默认 timestamp（mtime+size）够用；如果 loader/依赖有"内容变但 mtime 不变"（如 git checkout 精确还原、CI 容器层缓存），切 `snapshot: { module: { hash: true } }`（构建变慢但正确）。
- 缓存文件治理：`cache.maxAge`（默认 30 天）、`maxGenerations`；CI 里把 `node_modules/.cache/webpack` 缓存上传下载（key 含 `cache.name` + lockfile + 配置哈希）。
- 验证手段：`webpack --profile --progress` 后 stats 里看 `cachedModules` 占比；`cache.profile: true` 输出缓存构建详情。

```javascript
// webpack.config.js：缓存调优的生产配置（含 CI 场景分支）
const path = require('path');
module.exports = (env, argv) => {
  const isCI = !!process.env.CI;
  return {
    cache: {
      type: 'filesystem',
      name: `${argv.mode}-${process.env.APP_ENV ?? 'local'}`,   // 场景隔离
      version: process.env.BUILD_CACHE_VERSION ?? '1',          // 紧急情况全量失效的开关
      buildDependencies: {
        config: [
          __filename,
          path.resolve('tsconfig.json'),
          path.resolve('postcss.config.js'),
          path.resolve('src/theme.vars.js'),   // loader 读取的任何外部文件都要进来
        ],
      },
      managedPaths: [path.resolve('node_modules')],   // pnpm: 再加 node_modules/.pnpm
      maxGenerations: isCI ? 1 : 5,    // CI 每次全新，内存版 1 轮即可；本地多轮
      maxAge: 1000 * 60 * 60 * 24 * 14,
      profile: process.env.WEBPACK_CACHE_PROFILE === '1',
    },
    snapshot: {
      // CI 的 docker layer 可能造成 mtime 失真：CI 用 hash 快照保证正确性
      module: isCI ? { hash: true } : { timestamp: true },
      resolve: isCI ? { hash: true } : { timestamp: true },
      buildDependencies: { hash: true },
    },
  };
};
```
