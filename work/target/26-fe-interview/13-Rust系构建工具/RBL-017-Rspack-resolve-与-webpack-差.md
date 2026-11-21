---
title: [RBL-017] Rspack 的 resolve 能力与 webpack 有哪些差异？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-017：Rspack 的 resolve 能力与 webpack 有哪些差异？
**答**：
- Rspack 用 Rust 重写的 RspackResolver（基于 enhance-resolve 语义）：alias、extensions、mainFiles、mainFields、conditionNames、fallback 等高频字段语义对齐。
- 快的原因：目录扫描、symlink 处理、package.json 解析全部在 Rust 并行完成，且有解析结果缓存；resolve 是 webpack 构建前半程的主要耗时之一。
- 常见坑：extensions 数组顺序影响优先级（'.ts','.tsx' 要在 '.js' 前）；alias 精确匹配用 $ 结尾（'@/utils$'）；tsconfig paths 需要配套 tsconfig-paths 插件或 alias 手写映射。
- 差异点：部分冷门字段（如 alias 内函数形式、descriptionFiles 的极端用法）行为可能不同，迁移时用`resolve`报错清单验证。
- 性能建议：显式设置 resolve.extensions 尽量短、避免无界 fallback、设置 tsconfig 的 paths 双写一致。
- 追问钩子：symlink + preserveSymlinks 的行为与 node/webpack 对齐，monorepo 里 pnpm 链接场景要重点回归。

```javascript
// rspack.config.js
const path = require('path');
module.exports = {
  resolve: {
    extensions: ['.tsx', '.ts', '.jsx', '.js', '.json'],
    alias: {
      '@': path.resolve(__dirname, 'src'),
      'react$': 'react',                 // 精确匹配强制版本
    },
    mainFields: ['module', 'browser', 'main'], // 优先 ESM 入口利于 tree shaking
    conditionNames: ['import', 'browser'],
  },
};
```
