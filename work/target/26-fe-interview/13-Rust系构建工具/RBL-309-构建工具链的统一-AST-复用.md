---
title: [RBL-309] 构建工具链的统一 AST 与复用
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-309：构建工具链的统一 AST 与复用

**答**:
- 传统痛点：babel 解析→tsc 再解析→eslint 再解析——同一文件被解析 3+ 次，AST 结构还互不兼容（babel AST vs TS AST）
- 统一 AST 价值：一次解析多处使用（parse 一次给 transform/lint/format），工具间零转换；Rust 工具链（Oxc/SWC）通过共享原生 AST 实现
- 生态影响：lint（oxlint）与 transform（oxc-transform）同源后行为一致（「lint 过了但 transform 报错」类问题消失）；插件能力增强（拿到更完整语义：符号表/作用域链）
- 工程实践：自定义工具脚本选型时优先「能复用 bundler 内 AST 生态」的工具（插件内做 lint 比独立进程快）

```text
旧：parse × N（babel/tsc/eslint 各自 AST，互不兼容）
新：Oxc parse ×1 → transform + lint + minify 共享（含符号表）
收益：解析成本砍半 + 行为一致性
```
