---
title: [RBL-220] Rolldown 与 Oxc 原子能力的组合使用
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-220：Rolldown 与 Oxc 原子能力的组合使用

**答**:
- Oxc 是原子工具链（parser/transformer/resolver/minifier/linter），Rolldown 内部复用这些原子件——理解原子件有助于定制
- 组合场景：oxc-transform 单独做 TS 转译（脚本工具）、oxc-minifier 做压缩（CI 产物优化）、oxc-resolver 替代 enhanced-resolve
- 优势：同一套 AST/类型系统，工具间零转换成本；行为一致性（transform 与 bundler 内转译同源）
- 实践：写构建周边脚本时优先用 oxc 原子件替代 babel/ts-node（快一个数量级且依赖小）

```javascript
import { transform } from 'rolldown/experimental'   // 或 oxc-transform 包
const { code, map } = transform('a.ts', sourceCode, { typescript: { declaration: false } })
// 脚本场景：单文件转译无需起 bundler
```
