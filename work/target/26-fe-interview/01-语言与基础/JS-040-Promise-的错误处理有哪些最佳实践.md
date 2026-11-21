---
title: [JS-040] Promise 的错误处理有哪些最佳实践？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-040：Promise 的错误处理有哪些最佳实践？

**答**：
- 每个 Promise 链尾部都接 catch，避免 unhandledrejection。
- 不要在 Promise 构造函数里写 async 回调，内部抛错无法被外层捕获。
- then 里的同步异常也会进入失败分支，不需要手动 try/catch。
- 全局兜底：window 的 `unhandledrejection` 事件上报监控。

```javascript
// 反例：构造函数里用 async
new Promise(async (resolve) => {
  throw new Error('lost');   // 无法被 then 的失败分支捕获
});

// 正例
function task() {
  return new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error('task failed')), 100);
  });
}
task()
  .then((r) => console.log(r))
  .catch((err) => console.error('caught:', err.message))
  .finally(() => console.log('cleanup'));

// 全局兜底（浏览器）
window.addEventListener('unhandledrejection', (e) => {
  reportToMonitor(e.reason);
  e.preventDefault();
});
// Node.js
process.on('unhandledRejection', (reason) => console.error(reason));
```
