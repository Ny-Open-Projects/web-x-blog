---
title: [ALG-111] 手写 Promise.race，并基于它实现 `withTimeout(promise, ms)` 接口超时降级——超时就放弃请求改用本地缓存数据？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-111：手写 Promise.race，并基于它实现 `withTimeout(promise, ms)` 接口超时降级——超时就放弃请求改用本地缓存数据？
**答**：race 让所有 Promise 竞争，第一个 settle 的决定整体结果（成功或失败都算）。withTimeout 构造一个 ms 后 reject 的定时器 Promise 与业务 Promise 同跑；注意超时后要 `clearTimeout` 防泄漏，且 race 不会取消败者，真正的请求中断需要 AbortController 配合（见 ALG-166）。时间 O(1)，空间 O(n)。

```javascript
MyPromise.race = function (list) {
  return new MyPromise((resolve, reject) => {
    for (const p of list) MyPromise.resolve(p).then(resolve, reject); // 第一个 settle 定胜负
  });
};
// 接口超时降级：3s 拿不到数据就用本地缓存
function withTimeout(p, ms, fallback) {
  let timer;
  const timeout = new MyPromise((_, reject) => {
    timer = setTimeout(() => reject(new Error('timeout')), ms);
  });
  return MyPromise.race([p, timeout])
    .catch(e => (e.message === 'timeout' ? fallback : Promise.reject(e)))
    .finally(() => clearTimeout(timer)); // 防定时器泄漏
}
// withTimeout(fetchBanner(), 3000, cachedBanner)
```
