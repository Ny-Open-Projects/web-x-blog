---
title: [V3-318] Vapor 模式与动态组件、KeepAlive、Teleport 的兼容现状如何？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-318：Vapor 模式与动态组件、KeepAlive、Teleport 的兼容现状如何？
**答**：
- Vapor 是逐步对齐内建组件的过程：KeepAlive（需要缓存 DOM 块而非 vnode）、Teleport（挂载点动态化）、Transition（动画钩子接在 block 生命周期上）都需专门的 Vapor 实现。
- 动态组件 `<component :is>` 编译为动态 block 切换，语义接近 createIf 但以组件为单位。
- 兼容策略：未被 Vapor 内建组件覆盖的场景回退到 VDOM interop，用起来无感但享受不到全部收益。
- 工程建议：Vapor 目前定位实验/渐进启用，新页面用 Vapor、存量页面不动；上线前用 e2e 覆盖内建组件组合场景。
- 追问钩子：与 KeepAlive 组合时缓存的是 DOM 块 + 作用域暂停，激活时恢复 effect，而非重新 mount。
