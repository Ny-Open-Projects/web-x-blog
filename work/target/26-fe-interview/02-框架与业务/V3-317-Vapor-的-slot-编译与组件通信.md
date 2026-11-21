---
title: [V3-317] Vapor 模式的 slot 编译与父子组件通信是怎么做的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-317：Vapor 模式的 slot 编译与父子组件通信是怎么做的？
**答**：
- 传 slot 不再传「返回 vnode 的函数」而是传「返回 DOM block 的函数」，子组件用 `createSlot(name, fallback?)` 取块并挂载。
- 作用域插槽照旧是闭包：父组件作用域的数据在函数闭包里，子组件渲染时调用父传的函数即可，响应式依赖仍然按读取位置收集。
- props/emits/provide-inject 语义与 VDOM 模式一致，Vapor 只换渲染层，不换组件协议。
- 向下兼容：VDOM 组件与 Vapor 组件可以互相嵌套（interop 层做转换），这给了混合迁移空间。
- 注意第三方「渲染 vnode」的库（如某些动态渲染 UI）在 Vapor 下需要适配层，因为它期望的是 vnode 而非 DOM。
