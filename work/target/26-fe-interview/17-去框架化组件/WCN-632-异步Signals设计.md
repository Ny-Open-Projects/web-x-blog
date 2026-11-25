---
title: [WCN-632] 异步 Signal（async computed / resource）如何设计才能正确处理 loading/error/竞态？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-632：异步 Signal（async computed / resource）如何设计才能正确处理 loading/error/竞态？

**答**：
- 结论：把异步结果建模为「三态资源」{ loading, error, data }，并用请求序号（epoch）丢弃过期响应，避免竞态。
- 做法：source signal 变 → 触发 fetch；发起时 epoch++；响应回来时比对 epoch，过期则忽略；状态写入独立 signal 供 UI 消费。
- 追问钩子：为什么要 epoch 而不是 AbortController？两者常配合——epoch 处理逻辑竞态，Abort 取消网络；面试官想听组合方案。

```javascript
function resource(source, fetcher) {
  const state = signal({ loading: false, error: null, data: null });
  let epoch = 0;
  effect(() => {
    const key = source.get();
    const cur = ++epoch;
    state.set({ loading: true, error: null, data: null });
    fetcher(key).then(data => {
      if (cur === epoch) state.set({ loading: false, error: null, data });
    }).catch(error => {
      if (cur === epoch) state.set({ loading: false, error, data: null });
    });
  });
  return state;
}
const userId = signal(1);
const user = resource(userId, id => fetch(`/u/${id}`).then(r => r.json()));
effect(() => console.log(user.get())); // 三态消费
userId.set(2); // 旧请求响应会被 epoch 丢弃
```
