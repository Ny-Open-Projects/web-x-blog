---
title: [RBL-093] Turbopack 的 dev 架构与 Vite 的 dev 架构有何本质差异？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-093：Turbopack 的 dev 架构与 Vite 的 dev 架构有何本质差异？
**答**：
- Vite dev：无打包，基于原生 ESM——浏览器请求模块 → dev server 即时转换单个文件返回；依赖预构建（esbuild）把 node_modules 打成少数几个大文件。
- Turbopack dev：仍然打包（bundle）+ 函数级增量——产物是 chunk，只是"按需计算"。
- 差异根源：Vite 早期靠"不打包"避开全量构建成本，但请求瀑布（深层依赖链）与依赖预构建是代价；Turbopack 用增量打包兼得 bundle 优势（无瀑布）与 dev 速度。
- 演进：Vite 也在走向"全量打包 dev"（rolldown-vite 的 full bundle mode 实验方向），殊途同归。
- 网络行为差异：Vite dev 首次加载某深层依赖链会有串行请求瀑布；Turbopack 返回 chunk，请求数少。
- 追问钩子：本质是"按需编译 vs 按需计算"的路线之争，两者都在靠增量技术解决，趋势是融合。

```text
Vite dev（no-bundle ESM）
浏览器 import '/src/App.tsx'
  → server 转换单文件返回
  → 浏览器继续 import 下一层 → …（请求瀑布）
  node_modules → esbuild 预构建产物（少量大文件）

Turbopack dev（bundled + lazy）
浏览器请求 chunk → turbo 按需计算该 chunk 子图 → 返回打包产物
  无瀑布，但计算引擎必须做函数级增量才扛得住
```
