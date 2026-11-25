---
title: [RBL-053] Rolldown 为什么基于 Oxc？Oxc 提供了什么？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-053：Rolldown 为什么基于 Oxc？Oxc 提供了什么？
**答**：
- Oxc 是 Rust 生态的"JS 工具全家桶"：oxc_parser（AST）、oxc_transformer（TS/JSX/语法降级）、oxc_minifier（压缩）、oxc_resolver（基于 ENO 的解析器）、oxc_sourcemap 等，全部零拷贝设计。
- 选 Oxc 的原因：性能（解析速度与 esbuild 同量级甚至更快）、纯 Rust 生态一致性（Rolldown 不必混搭 swc/napi），以及维护团队与 Rolldown 重叠（同一班人马），迭代协同快。
- 关键组件对应：模块 resolve 用 oxc_resolver（兼容 Node 语义+浏览器字段）、TS/JSX 转换用 oxc_transformer、压缩用 oxc_minifier。
- 零拷贝意义：AST 在解析/转换/打包各阶段共享内存表示，不像 JS 工具链那样反复序列化，这是整体速度的底层来源。
- 对比 swc：swc 偏通用编译器（供 Rspack/Next 使用），Oxc 偏打包器一体化（rolldown 专用且组件更全，如内置 linter）。
- 追问钩子：Oxc 还提供 oxc_minify 与 oxc_prettier 等外围能力，Rolldown 之外也独立可用（oxlint 已大规模落地）。

```text
Rolldown 内核
├── oxc_resolver   ：模块解析（node_modules / exports / browser field）
├── oxc_parser     ：AST（零拷贝，供 treeshaking 直接消费）
├── oxc_transformer：TS/JSX/decorator 语法转换
├── oxc_minifier   ：生产压缩（替代 terser/esbuild minify）
└── oxc_sourcemap  ：映射链合并
```
