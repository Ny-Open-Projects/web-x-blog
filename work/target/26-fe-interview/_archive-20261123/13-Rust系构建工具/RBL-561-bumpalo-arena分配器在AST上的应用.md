---
title: [RBL-561] 为什么 Rust 构建工具的 AST 都用 arena 分配：bumpalo 的收益与代价
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-561：为什么 Rust 构建工具的 AST 都用 arena 分配：bumpalo 的收益与代价

**答**：
- AST 是典型的「大量小对象、一次性生灭」结构——普通 malloc/free 逐节点分配释放，arena（bumpalo）把分配变成指针递增、释放变成整个 arena drop，分配成本近乎为零。
- 收益 1：局部性——arena 里节点连续排布，遍历 AST 的 cache miss 大幅减少（指针追逐是解释/遍历类程序的最大热点）。
- 收益 2：所有权简化——普通 Rust 里 AST 父子互相引用需要 Rc<RefCell> 或索引，arena + 引用计数 `&'a` 生命周期让节点互指零成本（SWC/OXC 都借此获得稳定引用）。
- 收益 3：并行友好——每个模块一个独立 arena，transform 完整 drop，无跨线程释放竞争。
- 代价 1：不能单独释放某个节点（整体生命周期绑定）；增量修改 AST 会导致内存滞留——增量编译场景要按「模块粒度」重建 arena。
- 代价 2：泄漏风险——arena 忘记 drop 就是纯泄漏，需要与模块生命周期严格绑定；调试器里 arena 数据不可直接查看。
- 追问钩子：与对象池/自由列表的区别——arena 是「栈式整体回收」，适合阶段化数据（AST/中间产物），不适合长期驻存的图结构（模块图要用常规分配 + 索引）。

```javascript
// 概念示意：模块级 arena 生命周期
// struct ModuleCtx { arena: bumpalo::Bump, ast: Program<'arena> }
// let bump = Bump::new();
// let ast = bump.alloc(parse_into(src, &bump)); // 所有节点 alloc 在 bump 上
// transform(&ast);                              // 零 malloc
// drop(bump);                                   // 一次性回收全部节点

// 增量场景的正确粒度：
// - 模块失效 -> 重建该模块的 arena（其余模块 arena 复用）
// - 错误做法：全局共享 arena，单个模块失效无法回收 -> 构建越长内存越高

// JS 侧可感知的现象：
// swc 处理 1 万模块时内存平稳（每模块 arena 即弃）
// 而长生命周期工具链若误用共享 arena，会表现成「内存随构建时间线性增长」
```
