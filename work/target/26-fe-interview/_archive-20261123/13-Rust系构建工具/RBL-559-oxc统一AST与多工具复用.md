---
title: [RBL-559] OXC 的统一 AST 设计：一份 AST 服务解析/转换/lint/压缩四件事
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-559：OXC 的统一 AST 设计：一份 AST 服务解析/转换/lint/压缩四件事

**答**：
- OXC（oxlint/oxc-transform/oxc-minify）核心思路：**单一 AST + 多 pass 复用**——解析一次，transform/lint/minify 都在同一个 AST 上跑，省掉 babel 式「parse→每个插件各自 parse/serialize」的往返。
- 设计点 1：AST 定义与 estree 兼容（`arena` 内存池 + 类型索引），节点用 `AstKind` enum 可哈希索引——lint 规则按节点类型 O(1) 派发（类似 ESLint visitor 但零虚调用）。
- 设计点 2：**Semantic 分析一次成型**：scope tree + symbol table + 引用关系在 parse 后统一构建，所有规则共享（ESLint 的 no-unused-vars 类规则各自遍历，OXC 一次遍历产出 symbol 表后规则只查表）。
- 设计点 3：span/注释保留完整，minify 直接在 AST 上做 DCE/常量折叠，与 transform 共享「语法合法性」保证——避免 minifier 再 parse 一次已转换产物。
- 对构建工具的意义：打包器内嵌 OXC 后，「parse → resolve 宏 → transform → lint 校验 → minify」单管道完成，中间不落盘不序列化。
- 追问钩子：统一 AST 的代价——任何节点结构变更牵动所有 pass（breaking 管理严格）；estree 兼容换来生态互操作（prettier/rolldown 可消费），但牺牲了部分 Rust 侧最优内存布局。

```javascript
// OXC 管道概念示意（JS 调用视角）
// 一份数据四件事：parse → lint → transform → minify 全在内存连续进行
import { Transformer, Matcher } from 'oxc-transform';       // 伪 API
// 内部：
//   Parser::new(src).parse() -> Program (arena)
//   SemanticBuilder::build(&program) -> Scoping { scopes, symbols, references }
//   LintPass::run(&scoping)      // 规则查 symbol 表，不再遍历 AST
//   Transformer::transform(...)  // TS 剥离 / JSX / legacy 装饰器
//   Minifier::new(MangleOptions).build(&program) // 同一 AST 直接压缩
//   codegen(&program) -> String  // 唯一一次输出

// 对比 babel：@babel/parser -> AST JSON -> @babel/traverse 深拷贝遍历 -> generator
// OXC 每一步都省掉了「AST 跨 pass 的重建」，这也是 rolldown 选它做转换底座的原因
```
