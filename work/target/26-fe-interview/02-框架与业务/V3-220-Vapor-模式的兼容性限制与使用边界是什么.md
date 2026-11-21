---
title: [V3-220] Vapor 模式的兼容性限制与使用边界是什么？哪些写法吃不到收益？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-220：Vapor 模式的兼容性限制与使用边界是什么？哪些写法吃不到收益？
**答**：
- 前提：组件必须是**模板驱动**（SFC template）。手写渲染函数、运行时编译（`v-html` 动态模板、runtime `h()`）无法静态分析，享受不到 Vapor。
- 宏限制：部分依赖运行时 vnode 结构的写法需调整，如直接操作 `$refs` 内部、依赖 vnode 字段的第三方渲染库。
- 混用成本：Vapor 与 VDOM 组件互引需要兼容层转换（vdom-in-vapor / vapor-in-vapor），有薄层开销，避免在热点路径频繁跨界。
- 生态：依赖 vnode 的组件库（自定义 render table 等）需要适配版本，引入前查库的 Vapor 支持度。
- 决策建议：新项目页面级组件用 Vapor，复杂动态渲染（低代码画布）保留 VDOM 模式，两者按页面粒度隔离。

```javascript
// 判定清单：以下写法会退回或报错
// 1. 渲染函数组件（无模板）→ 保持 VDOM
const Comp = () => h('div', 'runtime'); // 不参与 Vapor
// 2. 动态组件名运行时解析 → 编译期无法定位，需显式声明分支或 keep VDOM
// 3. 第三方库直接 patch vnode：
const vnode = createVNode(Table, props); // Vapor 下不存在 vnode 实例
// 建议目录结构：src/views/vapor/...（新页面）src/views/legacy/...（依赖 vnode 的页面）
```
