---
title: [RBL-507] Rspack 的 Rust-JS 双栈架构：哪些留在 Rust、哪些留在 JS
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-507：Rspack 的 Rust-JS 双栈架构：哪些留在 Rust、哪些留在 JS

**答**:
- Rspack 的分层哲学：**热路径 Rust、冷路径 JS**——按「执行频率 × 单次成本」决定归属：
- **Rust 内建**：模块解析/转换（SWC）/模块图/chunking/压缩/SourceMap/HMR 增量——高频高频次，必须原生。
- **JS 保留**：webpack 兼容 loader/plugin 生态（社区资产）、用户自定义钩子（低频但灵活）、dev server 与 Node API——高频会跨桥所以尽量内置等价实现（内置 loader 替代 JS loader）。
- 混合热点的治理：「内置等价物」策略——高频的社区 loader（babel-loader/ts-loader）由 Rust 内建实现替代（内置 swc-loader vs JS swc-loader 差 10x）；plugin 的 hooks 若高频（每个模块触发）提供 Rust 侧批量钩子。
- 双栈一致性的代价：JS 生态语义对齐是持续工程（webpack plugin API 的行为兼容）——Rspack 团队用 webpack 的测试集对齐语义，兼容率是版本发布门槛。
- 追问钩子：双栈的「桥成本公式」——跨桥成本 ≈ 序列化(数据量) + 主线程调度(次数)——优化两轴：批量（减次数）与瘦身（减数据量，如 loader 只传变更内容）。

```javascript
// Rspack 双栈归属决策
const OWNERSHIP = {
  rust 内建: {
    items: ['模块解析 resolve', 'SWC 转换', 'Module Graph', 'chunking', '压缩', 'SourceMap', 'HMR 增量'],
    rule: '高频 × 高成本 = 必须 Rust',
  },
  js 保留: {
    items: ['webpack loader/plugin 生态', '用户自定义钩子', 'dev server / Node API'],
    rule: '生态资产 + 低频灵活钩子',
  },
  混合热点治理: {
    builtin 等价物: '高频社区 loader（babel/ts）→ 内置 swc-loader（差 10x）',
    批量钩子: '每模块触发的 plugin hook → Rust 侧批量钩子（减跨桥次数）',
  },
  桥成本公式: '跨桥成本 ≈ 序列化(数据量) + 主线程调度(次数) → 批量 + 瘦身',
  一致性: 'webpack 官方测试集对齐语义，兼容率 = 发布门槛',
}
```
