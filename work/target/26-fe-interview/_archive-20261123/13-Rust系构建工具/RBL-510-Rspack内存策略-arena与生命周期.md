---
title: [RBL-510] Rspack 的内存策略：arena 分配与 AST 生命周期
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-510：Rspack 的内存策略：arena 分配与 AST 生命周期

**答**：
- 编译器内存的核心策略：**AST 用 arena（区域分配器）**——所有 AST 节点分配在同一块连续内存，模块转换完成后**整块释放**——避免逐对象 GC/free 的开销与内存碎片。JS 引擎（Babel）逐对象分配 + GC 回收的内存峰值是 Rust 编译器的数倍。
- 生命周期设计：AST 的存活期 = 「转换阶段」——codegen 完成后 AST 即可释放（产物是字符串）；但 HMR 增量需要保留模块 AST（未变更模块不重 parse）——**两级生命周期**：转换期临时 AST（arena 释放）+ 增量期缓存 AST（长期持有）。长会话内存 = 缓存 AST 总量 × 平均大小——这就是「为什么 dev 久了内存涨」的主因，缓存淘汰（LRU）是解法。
- 大模块的内存尖峰：单个超大文件（万行 JSON）parse 的 arena 块就是尖峰——流式解析/分块处理是缓解手段，或者干脆「JSON 不进 AST」（特殊 loader 直接转 JS）。
- 与 JS 桥的内存交互：跨桥 Buffer 的内存归 Native 侧（ArrayBuffer 引用共享）——Rust 侧释放后 JS 侧访问会崩（UAF）——napi 的 lifetime 机制保证（JS 持有引用期间 Native 侧不释放）。
- 追问钩子：内存问题的排查路径（Rust 侧）——`heaptrack`/`valgrind massif` 找分配热点 + arena 块大小直方图——与 JS 侧 heap snapshot 方法不同，别混用。

```javascript
// Rspack 内存策略要点
const MEMORY_STRATEGY = {
  arena: 'AST 全部节点同块分配，转换完成整块释放——无逐对象 GC，无碎片',
  两级生命周期: {
    转换期: '临时 AST（arena 释放）——codegen 后即弃',
    增量期: '缓存 AST 长期持有（HMR 未变更模块不重 parse）',
    后果: 'dev 长会话内存 = 缓存 AST 总量——LRU 淘汰是解法',
  },
  尖峰: '超大文件 parse = arena 块尖峰——流式/分块/特殊 loader（JSON 不进 AST）',
  跨桥内存: 'Buffer 归 Native 侧——napi lifetime 保证 JS 持有期间不释放（防 UAF）',
  排查: 'Rust 侧用 heaptrack/massif + arena 直方图——别用 JS heap snapshot',
}
```
