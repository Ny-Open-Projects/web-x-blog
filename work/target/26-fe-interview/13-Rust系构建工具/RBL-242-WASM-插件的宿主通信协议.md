---
title: [RBL-242] WASM 插件的宿主通信协议怎么设计
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-242：WASM 插件的宿主通信协议怎么设计

**答**:
- 通信面：宿主调用插件的钩子（resolveId/transform/renderChunk），插件回调宿主能力（读文件/取配置）——双向 ABI
- 数据传输：wasm 线性内存 + 偏移量传递（宿主写 buffer → 传指针/长度 → wasm 读），序列化格式选 protobuf/flatbuffers（跨语言 schema 化）
- 能力模型：插件声明需要的宿主能力（fs.read/http），宿主按白名单注入——Wasmtime/WASI 的能力安全模型
- 版本兼容：ABI 版本号协商（宿主与插件各自声明支持版本，取交集），避免插件与宿主升级后接口断裂

```text
协议骨架：
Host → Plugin: hook(transform, codePtr, len) → Plugin: 返回 (outPtr, outLen)
Plugin → Host: guest_call(readFile, path) → 宿主能力白名单校验 → 返回数据
ABI 版本协商：host(1,2) ∩ plugin(1) → 用 v1
```
