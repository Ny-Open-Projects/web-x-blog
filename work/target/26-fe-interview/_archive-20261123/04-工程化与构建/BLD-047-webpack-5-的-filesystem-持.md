---
title: [BLD-047] webpack 5 的 filesystem 持久缓存原理与失效策略是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-047：webpack 5 的 filesystem 持久缓存原理与失效策略是什么？
**答**：
- 原理：首次构建把"模块的编译结果 + 依赖快照（snapshot）"序列化到 node_modules/.cache/webpack；下次构建对比文件时间戳/内容哈希与快照，未变模块直接反序列化复用。
- snapshot：managedPaths（node_modules 包管理器管理，默认信任）只做一次性快照，业务源码用 timestamp 或 hash 策略。
- 失效：buildDependencies 里的配置文件、loader、插件版本变化会整体失效；建议把 config、lockfile 都加入。
- cache.maxGenerations/maxAge 控制 GC；CI 里把缓存目录作为 artifact/restore key 是最有效的提速手段。

```javascript
// webpack.config.js：生产级缓存配置
const path = require('path');

module.exports = {
  cache: {
    type: 'filesystem',
    name: 'production-cache',        // 多 mode 分开缓存 防串台
    buildDependencies: {
      config: [__filename],          // 配置变化即失效
      // lockfile 变化（依赖升级）即失效
      // webpack 5 默认已跟踪 package.json 与 lockfile 的 buildDependencies
    },
    version: require('./package.json').version, // 手动追加版本维度
    compression: 'gzip',
    profile: true,                   // 缓存内建耗时分析
    maxAge: 1000 * 60 * 60 * 24 * 14,
    maxGenerations: 3,
  },
  snapshot: {
    // 业务文件用内容哈希 mtime 不可靠的 CI 场景改 hash
    module: { timestamp: true },
  },
  output: { path: path.resolve('dist') },
};
```
