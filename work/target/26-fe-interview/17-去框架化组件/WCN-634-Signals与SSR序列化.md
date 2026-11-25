---
title: [WCN-634] Signals 在 SSR 场景如何序列化与恢复？hydration 时要注意什么？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-634：Signals 在 SSR 场景如何序列化与恢复？hydration 时要注意什么？

**答**：
- 结论：服务端把 signal 当前值序列化进 HTML（如 <script type=application/json>），客户端用同值初始化信号，保证首屏 DOM 一致。
- 做法：序列化只取 data 而非订阅关系；客户端先 hydrate 值再绑定 effect；避免在 effect 中做仅客户端才有的副作用（否则服务端/客户端不一致）。
- 追问钩子：为什么不能序列化 effect/订阅？因为函数不可序列化且订阅关系要在客户端重建——考察对「状态可序列化、行为需重建」的理解。

```javascript
// 服务端：产出初始状态快照
const initial = { count: 42, user: { id: 7 } };
const html = `<script id="__DS_STATE__" type="application/json">${
  JSON.stringify(initial)
}</script>`;
// 客户端：先恢复值，再绑定副作用
function hydrateSignals() {
  const data = JSON.parse(document.getElementById('__DS_STATE__').textContent);
  const count = signal(data.count);
  const user = signal(data.user);
  effect(() => {
    document.querySelector('#count').textContent = count.get();
  });
  return { count, user };
}
// 首屏 DOM 由服务端按 count=42 输出，客户端 hydrate 后值一致 → 无闪烁
```
