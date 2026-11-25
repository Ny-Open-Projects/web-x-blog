---
title: [V3-358] Suspense 与错误边界组合时怎么治理重试风暴？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-358：Suspense 与错误边界组合时怎么治理重试风暴？
**答**：
- 组合结构：外层 ErrorBoundary 包内层 Suspense；异步依赖 reject 时错误冒泡给边界渲染错误 UI，重试按钮 re-trigger 数据层。
- 重试风暴成因：错误 UI 里自动重试 + 多个 Suspense 边界同时失败，触发并发请求风暴打挂弱后端。
- 治理一：重试加退避（1s/2s/4s）与最大次数，数据层实现而非组件层。
- 治理二：按域收敛错误——同一 API 域的失败共享「熔断状态」，熔断期间请求直接拒绝，UI 展示统一降级。
- 治理三：错误边界只做一次「兜底渲染」，不承担重试逻辑；重试入口必须显式点击或经过退避。
```javascript
async function loadWithRetry(fn, max = 3) {
  for (let i = 0; i < max; i++) {
    try { return await fn() } catch (e) { if (i === max - 1) throw e; await sleep(2 ** i * 500) }
  }
}
```
