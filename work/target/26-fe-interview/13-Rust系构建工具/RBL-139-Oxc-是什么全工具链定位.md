---
title: [RBL-139] Oxc 是什么？它与 SWC 的定位差异
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-139：Oxc（氧气 Oxidation Compiler）是什么？它与 SWC 的定位差异

**答**：
- Oxc 是 Rust 写的 JS 工具链全家桶：oxc_parser（AST 解析）、oxc_resolver（模块解析，对标 enhanced-resolve）、oxc_transformer（语法转换）、oxc_minifier、oxlint（linter）、oxc_formatter（对标 Prettier，规划中）。
- 定位差异：SWC 目标是替代 Babel（转换为主），Oxc 目标是给下一代工具链提供"原子能力库"——Vite/Rolldown 的底层解析、转换、resolve 都换成了 Oxc。
- 速度宣传：parser 比 SWC parser 更快（基准上常数倍），AST 设计成高内存局部性，便于遍历。
- Oxc 刻意不做"打包器"：打包交给 Rolldown（同生态），二者是分层关系——Rolldown 用 Oxc 做 parser/transform，自己管模块图与 chunk。
- 追问钩子：Vite 6+ 实验性 oxc 转换、Rolldown 集成、oxlint 独立可用，是三个不同的落地节奏，面试要分开说。

```javascript
// 用 oxc-parser 直接拿 AST（napi binding）
import { parseAsync } from 'oxc-parser';

const { program, errors } = await parseAsync('app.tsx', sourceCode, {
  sourceType: 'module',
  lang: 'tsx',
});
if (errors.length) throw new Error(errors[0].message);

// AST 遍历基于 ESTree 兼容结构（oxc 自有 Estraverse 家族），例：统计 import 来源
const imports = new Set();
walk(program, {
  ImportDeclaration(node) { imports.add(node.source.value); },
});
console.log([...imports]); // ['react', './utils'] —— 可做依赖分析、lint、codemod
```
