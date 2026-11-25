---
title: [RBL-019] Rspack 有哪些局限性？哪些项目不适合迁移？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-019：Rspack 有哪些局限性？哪些项目不适合迁移？
**答**：
- 插件强依赖型：构建管线里挂了多个自研 webpack 插件（操作 compilation 内部结构、webpack-sources 深度 API）的项目，改造成本可能吃掉全部提速收益。
- 极端边界型：重度依赖 webpack 冷门语义（复杂 loader pitch 编排、动态 require 的极端模式、老版本 target 变体）的项目，回归验证成本高。
- 小项目：模块数少（几百以内）时构建本来就秒级，迁移 ROI 低，配置迁移风险大于收益。
- 生态盲区：某些私有协议 loader（公司内 webpack 专属插件）没有 Rust/兼容实现，需要团队自己补。
- 收益预估公式：提速收益 ≈ 现构建时长 × 可迁移比例 − 迁移与回归成本；先量构建时间分布（resolve/transform/emit 各占多少）再决策。
- 追问钩子：决策顺序通常是"先开缓存与持久化 → 再收敛 loader/plugin → 最后才换构建器"。

```javascript
// 迁移 ROI 粗算脚本（读构建 stats）
const stats = require('./dist/stats.json');
const t = stats.time; // 总耗时 ms
const jsLoaderCost = stats.modules.filter(m => /babel-loader|ts-loader/.test(m.issuerPath?.[0]?.name || m.name)).length;
console.log({ total: t, jsLoaderModules: jsLoaderCost });
// 判定：total < 20000 → 不值得迁移；jsLoader 占比高 → 迁移收益大
```
