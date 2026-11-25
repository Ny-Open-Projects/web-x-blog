---
title: [WEB-629] wasm-bindgen：Rust 与前端互操作的工程实践
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-629：wasm-bindgen：Rust 与前端互操作的工程实践

**答**：
- wasm-bindgen 自动生成绑定：Rust 类型（字符串/Option/Vec）与 JS 值桥接，比手写线性内存序列化安全得多；wasm-pack 打包出 pkg 目录（wasm + js 绑定 + d.ts）直接进前端依赖
- 类型边界成本仍在：JsValue/字符串跨边界有序列化开销，热点路径仍要「批量扁平数据」模式（js_sys Uint8Array 引用共享）
- 异步互操作：Rust future ↔ JS Promise 用 wasm-bindgen-futures（spawn_local / js future 桥接），注意 Rust 侧 panic 默认 abort 实例
- 体积与调试：`wasm-opt -Oz` + `console_error_panic_hook`（panic 转可读 console 输出）；d.ts 让 TS 项目类型完整
- 工程结构建议：算法核心 crate 纯 Rust 可测（不依赖 wasm 绑定），绑定层薄壳——核心逻辑能在 node/rust 测试里回归

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Pipeline { /* 内部纯 Rust 状态 */ }

#[wasm_bindgen]
impl Pipeline {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Pipeline { Pipeline { /* ... */ } }
    // 批量扁平数据: 收 u8 数组引用, 返回处理长度, 避免逐元素跨界
    pub fn process(&self, data: &mut [u8]) -> usize { /* 核心算法 */ }
}
// 前端: import init, { Pipeline } from 'pkg'; await init(); const p = new Pipeline();
```
