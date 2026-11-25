---
title: [RBL-239] 产物 hash 稳定性怎么设计（长缓存基石）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-239：产物 hash 稳定性怎么设计（长缓存基石）

**答**:
- 目标：内容不变 → hash 不变（跨机器/跨时间一致）；内容变 → hash 必变
- 稳定性威胁：构建路径进产物（absolute path）、时间戳/随机 id、模块 id 不稳定（数字 id 顺序敏感→用 deterministic 命名）、changelog 进 banner
- 分层 hash：contenthash（文件内容）→ chunkhash（chunk 内容）→ runtime hash——运行时单独拆 chunk 避免业务变更污染 runtime hash
- 验证：双跑测试（同输入两次构建 diff 产物），CI 固定 fixture 验证；不稳定 hash 直接导致 CDN 缓存全失效

```javascript
// rspack.config.js
{
  output: { filename: '[name].[contenthash:8].js', assetModuleFilename: '[name].[contenthash:8][ext]' },
  optimization: { runtimeChunk: 'single', moduleIds: 'deterministic' },
  plugins: [new rspack.DefinePlugin({ __BUILD_TS__: JSON.stringify(null) })],  // 时间戳禁入
}
```
