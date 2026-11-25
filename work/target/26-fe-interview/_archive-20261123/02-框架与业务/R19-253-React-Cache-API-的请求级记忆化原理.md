---
title: [R19-253] React 的 cache() 请求级记忆化是什么原理？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-253：React 的 cache() 请求级记忆化是什么原理？
**答**：
- `cache(fn)` 返回包装函数：同一渲染请求内（服务端同请求、客户端同渲染批次）相同参数调用只执行一次，结果共享。
- 实现基于 AsyncLocalStorage 的请求级作用域 Map：每个请求一个独立缓存，请求结束销毁——不会跨请求泄漏。
- 典型场景：RSC 树中多个组件调用 getUser(id)，数据只查一次；Server Action 与渲染层共享同请求缓存。
- 与外部缓存（Redis）的层级关系：cache() 管请求内去重，跨请求缓存靠 Data Cache/CDN——两层各司其职。
- 注意：cache 只在 React 运行时环境生效（RSC/SSR），纯 Node 脚本里是普通函数。
