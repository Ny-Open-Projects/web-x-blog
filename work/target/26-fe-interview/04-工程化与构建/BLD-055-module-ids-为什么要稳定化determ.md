---
title: [BLD-055] module ids 为什么要稳定化？deterministic 是什么原理？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-055：module ids 为什么要稳定化？deterministic 是什么原理？
**答**：
- 模块 id 是 webpack runtime 里 require 的索引；webpack 4 及以前默认数字递增 id，新增/删除文件会让后续模块全部改号 → 多个 chunk 的引用关系变化 → hash 变化 → 缓存失效面扩大。
- deterministic：以模块的相对路径 + 相关上下文做哈希，生成稳定 4 位短 id，不依赖构建顺序；代价是 id 稍长（约 2~3 字节/模块）。
- chunkIds 同理推荐 deterministic；natural/size 适用于特定调试场景。
- 验证方式：连续两次"加一个文件再删掉"的构建，比较 manifest 中 vendor chunk 的 hash 是否不变。

```javascript
// webpack.config.js：稳定 id 完整配置
module.exports = {
  mode: 'production',
  optimization: {
    moduleIds: 'deterministic', // 模块 id 由路径哈希得出
    chunkIds: 'deterministic',  // chunk id 同样稳定
    runtimeChunk: 'single',
  },
  output: {
    filename: '[name].[contenthash:8].js',
  },
};

// text 代码块：效果对比
// 递增 id（旧默认）：module {0,1,2,...}
//   新增 src/a.js -> a 成为 0 后所有模块 id 后移 -> 引用它的 chunk 全部 hash 变化
// deterministic：module {V2t3: a.js, Kd9s: b.js}
//   新增/删除文件不影响既有模块 id -> 只有真正变化的 chunk hash 变化
```
