---
title: [V3-319] Vapor 模式的 tree-shaking 收益有多大？怎么分析 bundle？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-319：Vapor 模式的 tree-shaking 收益有多大？怎么分析 bundle？
**答**：
- 收益来源：VDOM patch/diff、createVnode、组件更新调度等运行时分支在 Vapor 应用里不再被引用，可整体摇掉。
- helper 按需引入：产物只 import 用到的 helper（template/setText/createFor…），模板越简单运行时越小；官方口径是运行时可压到几 KB 级。
- 分析方法：`rollup-plugin-visualizer` / vite-bundle-visualizer 出 treemap；对比同一组件 VDOM 与 Vapor 产物，看 @vue/runtime-dom 部分占比变化。
- 注意收益边界：业务代码通常远大于框架运行时， Vapor 省 10-20KB 对首屏是锦上添花，真正收益在**运行时更新开销**（无 diff）。
- 验证方式：除体积外用性能面板对比交互吞吐（如 60fps 下每帧 JS 时间）。
