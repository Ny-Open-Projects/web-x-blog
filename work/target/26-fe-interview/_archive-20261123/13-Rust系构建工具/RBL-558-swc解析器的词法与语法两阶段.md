---
title: [RBL-558] SWC 解析器为什么拆词法与语法两阶段：Rust 实现的性能考量
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-558：SWC 解析器为什么拆词法与语法两阶段：Rust 实现的性能考量

**答**：
- 两阶段 = Lexer（产出 token 流）+ Parser（消费 token 建 AST）——与 JS 工具（babel 单遍内联 lexing）的差别源于 Rust 的所有权模型：token 作为独立 struct（含 span），生命周期与源码字符串分离，parser 可按值消费。
- 性能要点 1：Lexer 用字节级状态机 + SIMD 友好的扫描（跳空白/识别标识符），比逐字符 unicode 判断快数倍；ASR/JSX 等模式用 enum 参数化而非运行时分支。
- 性能要点 2：token 用 `enum Token` 紧凑表示（常见 token 零堆分配），Keyword 匹配用 perfect hash / match 而非字符串比较。
- 性能要点 3：span 体系（`BytePos` u32 偏移 + SourceMap）让 AST 节点只存位置不存原文——错误定位/sourcemap 反查都走 SourceMap，AST 保持轻。
- 工程收益：两阶段让「重新 lex 但复用 parse 缓存」或「增量 lex」成为可能；也更利于 fuzzing（lexer 单测）。
- 追问钩子：为什么 JS 侧很难做到同级别速度——V8/JIT 的 GC 压力 + 字符串不可变 + 无值语义，token 频繁分配是热点；SWC 的 arena/bumpalo 分配器把节点分配变成指针递增。

```javascript
// Rust 侧概念示意（伪代码）：两阶段解析的核心结构
struct Lexer<'a> { src: &'a str, pos: BytePos, state: State }
enum Token { Ident(Atom), Str(JsStr), Num(f64), Punct(u8), ... } // 紧凑 enum，无堆
struct Span { lo: BytePos, hi: BytePos }                         // 只存偏移

// 阶段1：src -> Vec<Token>（字节状态机扫描，arena 分配）
// 阶段2：Parser 按值消费 token 流
// fn parse_program(p: &mut Parser) -> PResult<Program> { ... }
// AST 节点统一放 bumpalo arena：释放 = 整个 arena drop，无逐节点 free

// JS 侧调用（@swc/core）：
const { parseSync } = require('@swc/core');
const ast = parseSync('const a = 1;', { syntax: 'ecmascript' }); // 跨 NAPI 边界序列化
// 关键：跨边界传输 JSON 是瓶颈，进程内（Rust 插件直接拿 Arc<Program>）可省掉
```
