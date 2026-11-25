---
title: [WCN-411] 笔试：实现异步派生的竞态防护（epoch 校验）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-411：笔试：实现异步派生的竞态防护（epoch 校验）。
**答**：computed.async(fn)：fn 返回 promise；订阅者拿到「最新一次请求的结果」；旧请求返回被丢弃。实现状态机（loading/data/error）。

```javascript
function asyncComputed(fn) {
  let epoch = 0;
  const state = signal({ state: 'loading', data: null, error: null });
  effect(() => {
    const ep = ++epoch;
    state.set({ state: 'loading', data: state.get().data, error: null });
    fn().then(data => { if (ep === epoch) state.set({ state: 'data', data, error: null }); })
        .catch(e => { if (ep === epoch) state.set({ state: 'error', data: null, error: e }); });
  });
  return state;
}

```

**评分点**：
- epoch 计数：每次依赖变更 ++，请求完成时校验。
- 状态信号：{state, data, error}。
- in-flight 合并：相同输入未完成请求复用。
- 过期响应丢弃不写信号（防覆盖新数据）。
