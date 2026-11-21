---
title: [RBL-244] WASM 插件的性能瓶颈在哪里怎么优化
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-244：WASM 插件的性能瓶颈在哪里怎么优化

**答**:
- 瓶颈排序：边界序列化（字符串/结构体跨内存拷贝）> GC 语言桥接（Go/AS 的 GC 与宿主不同域）> 计算本身（wasm 计算接近原生，通常不是瓶颈）
- 优化一：批量接口（一次调用处理 N 个输入，摊薄边界成本）；优化二：内存复用（宿主与 wasm 共享 buffer 而非每次分配）；优化三：减少往返（钩子内自足，少回调宿主）
- 度量：边界耗时单独打点（进入/离开 wasm 的时间戳），区分「边界时间 vs 计算时间」
- 架构级：热点下沉——如果 WASM 插件成为瓶颈，与工具方协作将其提升为内置/native 能力（Rspack 的部分实验能力就是这么来的）

```rust
// 批量化：transform_many 一次调用
#[plugin_fn]
pub fn transform_many(Json(inputs): Json<Vec<TransformInput>>) -> FnResult<Json<Vec<TransformOutput>>> {
    Ok(Json(inputs.iter().map(|i| do_transform(&i.code, &i.filename)).collect()))
}
// 度量：boundary_ms 与 compute_ms 分开打点
```
