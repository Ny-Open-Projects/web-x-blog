---
title: [OPT-008] defer、async、type=module、modulepreload 如何组合使用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-008：defer、async、type=module、modulepreload 如何组合使用？

**答**：
- `defer`：并行下载，按出现顺序在 DOMContentLoaded 前执行——需要操作 DOM 且有顺序依赖的脚本用它。
- `async`：下载完立即执行、顺序不保证——独立无依赖的统计脚本用它。
- `type="module"`：默认行为等价 defer 且享受静态分析；`type="module" + async` 可做"下载即执行"的模块。
- `modulepreload` 比 `preload` 更进一步：不仅下载，还会解析模块并**递归预取依赖图**，是模块化应用首屏的主流组合。
- 典型落地：入口 module 用 `modulepreload`，统计类第三方用 `async`。

```html
<!-- 一一对应：几种 script 加载策略的组合落地 -->

<!-- 入口模块：modulepreload 递归预取整个依赖图，随后真正执行 -->
<link rel="modulepreload" href="/src/main.js" />
<link rel="modulepreload" href="/src/vendor.js" />
<script type="module" src="/src/main.js"></script>

<!-- 独立统计脚本：无依赖无顺序要求，下载完立即执行，不阻塞解析 -->
<script async src="https://analytics.example.com/collect.js"></script>

<!-- 传统 UMD 兜底脚本：需要 DOM 且按序执行 -->
<script defer src="/legacy/polyfill.js"></script>
```
