---
title: [RBL-243] 用 Rust 写一个 WASM 构建插件的完整流程
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-243：用 Rust 写一个 WASM 构建插件的完整流程

**答**:
- 步骤：Cargo 项目（依赖 extism/swc-wasm 插件 SDK）→ 实现 trait 钩子（transform）→ `cargo build --target wasm32-wasi` 产出 .wasm → 打包工具加载注册
- 代码骨架：入口导出钩子函数，从宿主内存读输入，处理后写回线性内存——SDK 封装了内存管理细节
- 调试：wasm 时间线（宿主 profiling 需支持 wasm 帧符号化）；本地用 wasmtime CLI 单测钩子
- 工程现实：WASM 插件生态尚早，落地前确认目标工具的插件协议成熟度，避免押注未稳定 ABI

```rust
// Cargo.toml: crate-type = ["cdylib"], target wasm32-wasi
use extism_pdk::{plugin_fn, FnSignature, Json, Path};

#[plugin_fn]
pub fn transform(Json(input): Json<TransformInput>) -> FnResult<Json<TransformOutput>> {
    let out = do_transform(&input.code, &input.filename);
    Ok(Json(TransformOutput { code: out }))
}
// 构建: cargo build --target wasm32-wasi --release → target/.../*.wasm
```
