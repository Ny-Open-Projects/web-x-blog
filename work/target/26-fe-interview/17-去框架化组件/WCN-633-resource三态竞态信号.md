---
title: [WCN-633] 笔试：实现 resource signal（三态 + epoch 竞态 + 手动 refresh + 自动 dispose）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-633：笔试：实现 resource signal（三态 + epoch 竞态 + 手动 refresh + 自动 dispose）

**答**：
- 需求：实现 createResource(source, fetcher)，返回 { state, refresh }；state 含 loading/error/data；source 变化自动请求，过期响应丢弃；元素断开时自动取消。
- 思路：effect 监听 source 触发请求；epoch 递增；AbortController 取消旧请求；返回 state signal 与 refresh 方法。
- 边界：并发请求只保留最新；重复 refresh 防抖；dispose 后不再更新状态。

```javascript
function createResource(source, fetcher) {
  const state = signal({ loading: false, error: null, data: null });
  let epoch = 0, disposed = false, ctrl = null, timer = null;
  function load() {
    const key = source.get(), cur = ++epoch;
    ctrl?.abort(); ctrl = new AbortController();
    state.set({ loading: true, error: null, data: null });
    fetcher(key, ctrl.signal).then(data => {
      if (!disposed && cur === epoch) state.set({ loading: false, error: null, data });
    }).catch(error => {
      if (!disposed && cur === epoch && error.name !== 'AbortError')
        state.set({ loading: false, error, data: null });
    });
  }
  effect(load);
  return {
    state,
    refresh: () => { clearTimeout(timer); timer = setTimeout(load, 50); },
    dispose: () => { disposed = true; ctrl?.abort(); },
  };
}
```

**评分点**：
- 三态（loading/error/data）完整且互斥更新。
- epoch + AbortController 双重处理竞态（过期响应与取消网络）。
- refresh 带防抖，避免重复请求。
- dispose 后不再 setState，且取消在途请求。
