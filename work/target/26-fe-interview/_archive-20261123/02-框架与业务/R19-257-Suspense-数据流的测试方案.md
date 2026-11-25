---
title: [R19-257] Suspense 数据流的组件怎么测试？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-257：Suspense 数据流的组件怎么测试？
**答**：
- 手动控制 promise：测试中创建 deferred（外部 resolve/reject 的 promise），先断言 fallback、再 resolve 断言内容、reject 断言错误 UI。
- 工具：@testing-library/react 的 act + waitFor；React 19 支持 `act(() => promise)` 等待 suspense 完成。
- MSW：网络层 mock 慢响应（延迟配置）模拟真实 pending。
- 断言重点：fallback 顺序、错误边界触发、重试后恢复、并发组件间不互相阻塞。
- e2e：节流网络（CDP）验证真实慢网下的 fallback 表现。
```javascript
function deferred() { let resolve, reject; const p = new Promise((r, j) => { resolve = r; reject = j }); return { p, resolve, reject } }
```
