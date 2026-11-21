---
title: [BLD-110] webpack5 filesystem 持久化缓存的原理：缓存层级、快照与版本失效策略。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-110：webpack5 filesystem 持久化缓存的原理：缓存层级、快照与版本失效策略。
**答**：
- `cache.type: 'filesystem'` 是**模块级缓存**：每个 module 的 build 结果（含 source、依赖列表、快照）序列化到 `node_modules/.cache/webpack`，默认 memory 优先、file 兜底（`cache.maxGenerations` 控制内存版轮换）。
- 失效判定三层：**版本层**（`cache.version` + webpack 版本 + 关键配置 hash，变了全量失效）；**buildDependencies**（loader 包、配置文件、`--env`，变了全量失效）；**快照层**（每个模块构建时生成 `mtime+size` 的 timestamps 快照，rebuild 时对比决定单模块是否重 build）。
- `managedPaths`（默认含 node_modules）内的文件默认信任不改直接复用缓存——这是 CI 上要装好依赖再构建的原因；`snapshot.managedPaths` 可扩展到私有包目录。
- 经典脏缓存根因：loader 里读 `process.env.X` / 读取未声明的外部文件，而 buildDependencies 没声明，导致"代码没变但产物应该变"的缓存假命中。

```javascript
// 生产级 filesystem cache 配置（webpack.config.js 片段）
module.exports = (env, argv) => ({
  cache: {
    type: 'filesystem',                    // 开启持久化缓存
    name: process.env.APP_ENV ?? 'dev',    // 缓存命名空间：不同环境不共用
    version: 'v1-config-hash',             // 大配置变更时手动 bump，等价"全量失效开关"
    buildDependencies: {
      config: [__filename],                // 配置文件本身变化 → 全量失效（关键！）
      // 声明 loader/插件包，升级后自动失效：
      // webpack5 默认会追踪 package.json，但 monorepo 私有 loader 需要显式加
    },
    managedPaths: [process.env.PNPM_HOME ?? 'node_modules'], // 信任区：不参与快照对比
    maxMemoryGenerations: 1,               // dev 内存缓存轮换，防 OOM
    profile: process.env.CACHE_PROFILE === '1', // 输出缓存命中统计
    store: 'pack',                         // webpack5 默认 pack（合并存储，IO 更少）
  },
  snapshot: {
    // timestamp：只比 mtime+size，快；hash：比内容，准。一般维持默认 timestamp
    module: { timestamp: true },
    resolve: { timestamp: true },
    // 自定义 loader 读了外部 json 时，必须把该文件纳入快照管理：
    // managedPaths 之外的目录默认就是可失效区，无需额外配置
  },
});
// CI 使用姿势：先 actions/cache 缓存 node_modules/.cache/webpack，命中率可达 70%+
// 验证：stats.toString({ cachedModules: true }) 或 --profile 看 "cache hit"
```

## 十二章 webpack 高级场景（BLD-111 ~ BLD-118）
