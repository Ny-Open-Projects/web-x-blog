---
title: [RBL-052] Rolldown 如何统一 esbuild 与 Rollup 的能力？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-052：Rolldown 如何统一 esbuild 与 Rollup 的能力？
**答**：
- 背景痛点：Vite 旧架构 dev 用 esbuild（转换+预构建）、prod 用 Rollup（打包+tree shaking），两套内核导致 dev/prod 行为差异（依赖处理、模块图、sourcemap 链）、配置双轨。
- Rolldown 的统一：在一个 Rust 内核里同时实现 esbuild 的强项——超快 transform（基于 Oxc）、minify、dev 预构建；以及 Rollup 的强项——高效 tree shaking、scope hoisting、干净 ESM 产物、插件钩子体系。
- 实现手段：Oxc 提供与 swc/esbuild 同级的解析转换速度；打包器核心移植 Rollup 的模块图与摇树算法并 Rust 化并行。
- 效果：Vite 只需要一个内核，transform 层（esbuild API、rollup transform 钩子）都打到同一引擎，dev/prod 一致性从架构上保证。
- 对用户的意义：配置更少（minify/transform 内置）、插件复用面更广（rollup 插件基本可用、esbuild 插件有兼容层）、构建更快。
- 追问钩子：统一不是"合并两份代码"，而是在 Rust 里按各自语义重写再对齐行为，工程量是主要难点。

```text
旧 Vite 架构                    Rolldown 后
dev : esbuild(transform)        dev : Rolldown(Oxc transform + 预构建)
      rollup 不参与                    ↓ 同一内核
prod: esbuild(minify)           prod: Rolldown(tree shaking + minify)
      rollup(bundle)                   ↓
问题：dev/prod 模块图/语义漂移   单一内核 → 行为一致、配置单轨
```
