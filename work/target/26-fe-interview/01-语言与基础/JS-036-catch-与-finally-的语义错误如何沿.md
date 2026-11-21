---
title: [JS-036] catch 与 finally 的语义？错误如何沿链条冒泡？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-036：catch 与 finally 的语义？错误如何沿链条冒泡？

**答**：
- catch 等价于 `then(null, onRejected)`，捕获链条上游任意一步的错误。
- 错误会跳过中间所有成功回调，直到最近的失败处理器；处理完链条恢复正常。
- catch 本身也可能抛错，需要后续再接 catch。
- finally 不接收参数、返回值透传，用于清理（关闭 loading、释放句柄）。

```javascript
function fetchData(fail) {
  return new Promise((resolve, reject) => {
    setTimeout(() => (fail ? reject(new Error('network')) : resolve('data')), 100);
  });
}

fetchData(true)
  .then((d) => console.log('A', d))      // 跳过
  .then((d) => console.log('B', d))      // 跳过
  .catch((err) => { console.error(err.message); return 'fallback'; })
  .then((d) => console.log('C', d))      // C fallback，链条恢复
  .finally(() => console.log('cleanup'))
  .catch(() => console.error('recovered from catch itself'));
```
