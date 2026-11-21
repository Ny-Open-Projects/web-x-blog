---
title: [H5-286] Worker 里的异常怎么传回主线程：onerror/message
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-286：Worker 里的异常怎么传回主线程：onerror 与 message

**答**：
- 两条通道：worker.onerror（线程级未捕获异常，ErrorEvent 带 filename/lineno/message，线程仍活着）与 message.error（业务级，自己序列化回传）
- 线程级错误：只含字符串信息，丢上下文——业务代码应在 try/catch 内 postMessage 错误详情
- 致命错误：Worker 内 importScripts 失败等会导致线程不可用，需要重建 worker 实例（池化框架里处理）
- 序列化限制：Error 对象经 structured clone 会丢失自定义属性，回传 { message, code, stack 字符串 } 的普通对象
- 最佳实践：业务层约定 `{ ok, data | error }` 信封格式，主线程统一 unwrap

```javascript
// worker.js
self.onmessage = async ({ data }) => {
  try {
    const result = await heavy(data);
    self.postMessage({ ok: true, data: result });
  } catch (e) {
    self.postMessage({ ok: false, error: { message: e.message, code: e.code, name: e.name } });
  }
};
// main.js
worker.onmessage = ({ data }) => data.ok ? resolve(data.data) : reject(Object.assign(new Error(data.error.message), data.error));
worker.onerror = (e) => { e.preventDefault(); report({ type: 'worker-fatal', msg: e.message }); };
```
