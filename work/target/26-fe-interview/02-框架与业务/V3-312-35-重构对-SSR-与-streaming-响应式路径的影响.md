---
title: [V3-312] Vue 3.5 响应式重构对 SSR 路径有什么影响？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-312：Vue 3.5 响应式重构对 SSR 路径有什么影响？
**答**：
- SSR 渲染时不建立依赖订阅（在 `renderToString` 内部会关闭 effect 收集），新链表结构让这条路径更轻：不创建 Link 节点，减少服务端 GC 压力。
- `useId`、懒水合等 3.5 特性配合 SSR：useId 生成同构稳定 ID，避免服务端/客户端 ID 不一致导致 hydration mismatch。
- computed 在 SSR 每次渲染都是「冷」状态：没有缓存复用的订阅者， getter 会被实际求值，注意 getter 里不要做重计算或副作用。
- SSR 场景 reactive 大对象只读不写，版本计数机制天然不影响渲染正确性。
- 迁移建议：自定义响应式工具库若 hack 过旧内部结构（如读 `_dirty`），3.5 下必须重写——内部 API 不再兼容。
