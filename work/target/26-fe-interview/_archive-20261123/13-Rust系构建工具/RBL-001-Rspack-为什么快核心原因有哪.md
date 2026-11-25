---
title: [RBL-001] Rspack 为什么快？核心原因有哪些？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-001：Rspack 为什么快？核心原因有哪些？
**答**：
- 语言层：核心用 Rust 编写并编译为原生二进制，没有 JS 解释执行开销，也不存在 V8 堆内存上限与 GC 抖动，大型项目数千模块场景下差距被放大。
- 并行层：模块解析、转换、压缩等阶段按模块粒度切分到 Rayon 线程池并行执行，充分利用多核；webpack 主要流程在 JS 单线程事件循环里跑。
- 算法层：内部用crate（如 swc 做转换、rayon 做并行、dashmap 做并发哈希）替代 webpack 的大量 JS 数据结构操作；模块图用 Rust 数据结构存储，访问无跨语言序列化成本。
- 缓存层：内置持久化缓存（memory + filesystem），冷启动后增量构建只重编变更模块。
- 兼容策略：Rspack 定位是 webpack 的"高性能子集"，不做全量 tapable 动态 hook 派发这类 JS 侧昂贵机制，把高频路径内置化（如内置 css、内置 tree shaking）。
- 追问钩子：快不等于万能——重度依赖 webpack 专属插件的项目迁移收益会被插件瓶颈吃掉。

```javascript
// 同一中型项目（约 3000 模块）构建时间量级对比（示意）
// webpack 5（无缓存冷启动）   ：~60s
// webpack 5（filesystem 缓存）: ~12s
// Rspack（冷启动）            ：~8s
// Rspack（持久缓存增量）      ：~1.5s
// 结论：冷启动快 5~10 倍来自 Rust+并行；增量快来自持久缓存，二者收益正交
console.log('选择顺序：先上缓存（两工具都受益），再考虑换 Rspack');
```
