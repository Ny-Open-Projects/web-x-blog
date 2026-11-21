---
title: [DP-234] 源码识别：Fetch/AbortController 的命令与取消模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-234：源码识别：Fetch/AbortController 的命令与取消模式？
**答**：
- 命令模式：Request 对象封装"一次请求"的全部参数（命令对象），fetch 执行它；signal 是命令的取消句柄。
- 观察者（abort 信号）：AbortSignal 是可观察对象（addEventListener('abort')），多个消费者订阅同一 signal（请求、流、事件监听都能被同一信号取消）。
- 状态机：signal.readyState 语义（open → aborted），abort 后 errno 转 DOMException 'AbortError'——取消不是异常丢失而是结构化状态。
- 识别要点：组合取消（AbortSignal.any([...])）与超时取消（AbortSignal.timeout）是"命令取消"的编排能力。

```javascript
// signal 即观察者 + 取消句柄
async function fetchWithTimeout(url, ms = 5000) {
  const signal = AbortSignal.any([AbortSignal.timeout(ms), userAbortSignal]);  // 组合取消源
  return fetch(url, { signal });
}
// 多消费者共享：
const ac = new AbortController();
fetch('/a', { signal: ac.signal });
fetch('/b', { signal: ac.signal });
document.addEventListener('keydown', handler, { signal: ac.signal });   // DOM API 也接入同一 signal
ac.abort();                                              // 三者同时取消 → AbortError 结构化
// 组件卸载取消模式：
useEffect(() => { const ac = new AbortController();
  fetch('/data', { signal: ac.signal });
  return () => ac.abort();                               // 卸载即取消（防竞态 setState）
}, []);
```
