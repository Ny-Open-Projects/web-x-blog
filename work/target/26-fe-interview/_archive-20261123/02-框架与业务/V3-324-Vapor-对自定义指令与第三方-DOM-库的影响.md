---
title: [V3-324] Vapor 模式对自定义指令和第三方 DOM 库有什么影响？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-324：Vapor 模式对自定义指令和第三方 DOM 库有什么影响？
**答**：
- 自定义指令生命周期（mounted/updated/…）在 Vapor 下语义对齐为 block 的挂载/更新钩子，但「updated」不再有 vnode 对比语义，指令里依赖 vnode 信息的写法要改。
- 第三方 DOM 库（GSAP、地图、编辑器）通常拿 ref 操作 DOM，这套在 Vapor 下天然可用——ref 语义不变，`useTemplateRef` 继续有效。
- 需要小心的是「包装 vnode」类库：渲染管线不同，它们假设存在 vnode 树；适配方式是改成包装 DOM block 或通过 interop 回退 VDOM。
- v-html/v-text 类动态内容在 Vapor 编译为对应 helper（setHtml/setText），实现层不同但模板写法不变。
- 结论：绝大多数「拿 ref + 直接 DOM」的集成零成本迁移；少数 vnode 侵入型库需要等适配或用 interop。
