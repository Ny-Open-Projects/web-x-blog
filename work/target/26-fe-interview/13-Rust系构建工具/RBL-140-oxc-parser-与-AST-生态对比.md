---
title: [RBL-140] oxc-parser 的 AST 与 Babel/SWC AST 有何不同
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-140：oxc-parser 的 AST 与 Babel/SWC AST 有何不同

**答**：
- 命名风格：Babel AST 用 @babel/types 命名（如 ClassProperty），oxc 输出尽量对齐 ESTree（SpiderMonkey 标准），工具迁移时节点名更通用；SWC AST 是 swc_ecma_ast 自有命名。
- 内存布局：oxc AST 是 Rust 结构体的紧凑布局（span 用 u32 偏移），遍历缓存友好；JS 侧通过 NAPI 暴露时仍转成普通对象。
- 速度：oxc parser 基准是 Babel 的几十倍、SWC 的数倍，主要是零分配 span 与字符串驻留（atom）优化。
- 生态配套：oxc 提供自己的 walker/visit 家族与 ESTree 兼容序列化；做 codemod 时若团队已有 Babel AST 工具，要注意 `directives`/`flow` 等节点差异。
- 追问钩子：为什么 Rolldown 选 oxc 而不是 swc？——同生态（都是 oxc 项目群）、AST 无需跨结构转换、issue 响应在同一仓库体系内闭环。

```javascript
// 同一段代码三种 AST 的节点命名对比
const src = 'class A { #x = 1 }';
// Babel:  ClassPrivateProperty
// SWC:    PrivateProp
// Oxc:    PropertyDefinition(private: true)  —— 对齐 ESTree

// 实操建议：写 codemod 前用 AST explorer 确认节点类型，
// oxc 的 JS binding 也可 dump AST 比对：
import { parseAsync } from 'oxc-parser';
const ast = (await parseAsync('a.js', src)).program;
console.log(ast.body[0].body.body[0]); // PropertyDefinition { privateName: '#x', ... }
```
