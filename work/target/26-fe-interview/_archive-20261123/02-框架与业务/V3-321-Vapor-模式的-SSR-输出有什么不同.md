---
title: [V3-321] Vapor 模式的 SSR 输出有什么不同？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-321：Vapor 模式的 SSR 输出有什么不同？
**答**：
- SSR 端 Vapor 编译成直接拼字符串的渲染函数（同 VDOM SSR 的 ssrRender 思路），不创建 DOM、不建依赖。
- 水合阶段：Vapor 的水合不是「拿服务端 vnode 注水」，而是客户端运行 Vapor 组件时把已有 DOM 节点「认领」为 block 里的元素（claim），跳过创建。
- 产物更小：服务端无需下载完整 VDOM 运行时再 diff，客户端无需重建 vnode 树。
- 风险点：claim 路径对模板结构一致性要求极高，任何 SSR/CSR 输出结构不一致都会水合失败，mismatch 排查比 VDOM 更早失败（好现象但信息更少）。
- 工程建议：开启 Vapor SSR 时把 hydration mismatch 检测纳入 CI（SSR 快照对比）。
