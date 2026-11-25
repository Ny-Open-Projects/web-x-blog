---
title: [V3-246] 手写：迷你 Suspense（异步依赖计数 + fallback 切换 + 超时）
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-246：手写：迷你 Suspense（异步依赖计数 + fallback 切换 + 超时）
**答**：实现 `createSuspense(childrenPromise, { fallback, timeout })`：收集子树异步依赖 promise；全部 resolve 前渲染 fallback；超过 timeout 未完成时提示降级（标记 timedOut）；任一 reject 时回调 onError 且支持通过返回的 retry() 重新进入 pending。不要求 vnode diff，可用字符串渲染函数模拟。
**评分点**：
- pending 计数归零判定（Promise.allSettled 思路 + reject 短路）
- timeout 与完成竞态处理（完成后清除定时器）
- retry 需重置计数与超时
- 边界：空依赖直接 resolve；timeout 后完成是否恢复展示（需要说明策略）

```javascript
function createSuspense(loadDeps, { timeout = 3000 } = {}) {
  const state = reactive({ phase: 'pending', timedOut: false });
  let timer = null;
  function enter() {
    state.phase = 'pending'; state.timedOut = false;
    clearTimeout(timer);
    timer = setTimeout(() => { state.timedOut = true; }, timeout);
    Promise.allSettled(loadDeps()).then((results) => {
      clearTimeout(timer);
      const rejected = results.find((r) => r.status === 'rejected');
      if (rejected) { state.phase = 'rejected'; state.error = rejected.reason; }
      else state.phase = 'resolved'; // timeout 后完成：默认恢复展示（timedOut 只是提示标记）
    });
  }
  enter();
  return { state, retry: enter };
}
function renderSuspense(susp, { fallback, error, children }) {
  if (susp.state.phase === 'rejected') return error?.(susp.state.error, susp.retry);
  if (susp.state.phase === 'pending') return fallback(susp.state.timedOut);
  return children();
}
// 验证
const susp = createSuspense(() => [fetch('/api/a'), fetch('/api/b')], { timeout: 3000 });
renderSuspense(susp, {
  fallback: (timedOut) => timedOut ? '网络较慢，仍在加载…' : '加载中…',
  error: (e, retry) => h(ErrorPanel, { msg: e.message, onRetry: retry }),
  children: () => h(Dashboard),
});
```
