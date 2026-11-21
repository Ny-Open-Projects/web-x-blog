---
title: [R19-260] 怎么把第三方数据层（Apollo/Relay）接入 use/Suspense？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-260：怎么把第三方数据层接入 use/Suspense？
**答**：
- 关键是拿到「可共享的 promise」：Apollo 的 observableToPromise、Relay 的 fetchQuery 返回 promise，缓存由库内建（同一 query 去重）。
- 封装：`function useGraphQL(query, vars) { const p = client.getPromise(query, vars); return use(p) }`。
- 失效衔接：mutation 后 invalidate 库内缓存并重新创建 promise，触发 Suspense 更新。
- 迁移路径：老组件用 hook 三态，新组件逐步换 use + 边界，两者共存期注意 fallback 视觉一致性。
- 风险：第三方库的 promise 缓存生命周期与 React 渲染周期不完全对齐（取消/过期），需在 adapter 层处理。
