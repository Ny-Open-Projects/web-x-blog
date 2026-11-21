---
title: [BAS-146] Promise 的 finally 什么时候执行？会改变结果吗？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-146：Promise 的 finally 什么时候执行？会改变结果吗？
**答**：
- 无论 fulfill 还是 reject 都会执行，且回调不接收参数，适合放清理逻辑。
- finally 的返回值默认被忽略，结果原样向下传递；但如果回调内部 throw，会替换为新的失败。
- 常用场景：loading 开关、关闭弹窗、释放资源，成功失败两条路只写一份。

```javascript
Promise.resolve('ok')
  .finally(() => 'ignored')       // 返回值被忽略，不改变结果
  .then(v => console.log(v));     // ok

Promise.reject(new Error('x'))
  .finally(() => console.log('清理资源')) // 成功失败都执行
  .catch(e => console.log(e.message));    // x，失败状态继续向下透传
```
