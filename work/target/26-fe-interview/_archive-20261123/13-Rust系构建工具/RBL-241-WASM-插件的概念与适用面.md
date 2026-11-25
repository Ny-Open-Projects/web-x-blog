---
title: [RBL-241] WASM 插件是什么它与 Native 插件的取舍
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-241：WASM 插件是什么，它与 Native 插件的取舍

**答**:
- WASM 插件：用 Rust/Go/AssemblyScript 写、编译为 .wasm，由打包工具以沙箱方式加载执行（如 Rspack/Turbopack/Wasm 插件协议、Extism 类运行时）
- 价值：跨平台分发（一份 wasm 全平台）、沙箱安全（内存隔离，插件崩溃不伤宿主）、语言自由
- 与 Native 插件取舍：Native（Rust 直接编译进宿主/动态库）性能最好但分发/版本兼容复杂；WASM 有 10-30% 性能损耗（边界序列化与 GC 语义差异）但分发干净
- 适用判断：高频热点转换（每模块）用 Native/内置；低频重逻辑（产物后处理、自定义压缩策略）WASM 足够

```text
选择矩阵：
每模块高频转换 → Native/内置（零边界成本）
每产物低频处理 → WASM（分发友好）
纯 JS 逻辑     → JS 插件（生态与调试最友好）
```
