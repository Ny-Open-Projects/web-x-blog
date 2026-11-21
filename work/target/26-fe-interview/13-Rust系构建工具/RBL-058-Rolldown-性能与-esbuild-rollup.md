---
title: [RBL-058] Rolldown 的构建性能与 esbuild/Rollup 对比如何？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-058：Rolldown 的构建性能与 esbuild/Rollup 对比如何？
**答**：
- 对 Rollup：同语义下 rolldown 通常快 10~30 倍（官方基准），主要来自 Rust 并行（解析/转换按模块并行）与零拷贝 AST；模块数越多差距越大。
- 对 esbuild：纯打包吞吐 esbuild 略快或持平（esbuild 极简管线），但 rolldown 补齐了 tree shaking 质量、插件生态、chunk 控制能力；综合"质量/速度"比 esbuild 更均衡。
- 瓶颈规律一致：JS 插件越多越慢（FFI 边界），原生插件为主时接近上限速度。
- 内存：rolldown 内存占用低于 rollup（AST 共享），大项目（万级模块）差异显著。
- 参考 data：官方 repo 基准（如 three.js/antd 类项目）——rollup 数十秒，rolldown 秒级；esbuild 秒级但产物 tree shaking 粒度粗。
- 追问钩子：性能数字会随版本变化，面试答题给量级与原因（并行化/零拷贝/无 GC）比背具体倍数更稳。

```javascript
// 三工具同配置打包（约 5000 模块前端应用，示意量级）
// rollup   : ~45s（tree shaking 精细，JS 单线程）
// esbuild  : ~4s（快，但 tree shaking/插件能力弱）
// rolldown : ~5s（快 + rollup 级语义 + 内置压缩）
console.log('选型：库打包 & 生态兼容 → rolldown；极简脚本 → esbuild；');
console.log('Vite 用户 → 等 rolldown-vite 默认化，无需自行切换。');
```
