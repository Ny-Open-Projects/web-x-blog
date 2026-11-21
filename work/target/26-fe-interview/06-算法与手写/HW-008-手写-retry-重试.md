---
title: [HW-008] 手写 retry 重试
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-008：手写 retry 重试

**答**：
- 评分点：重试次数语义要清晰（total 次尝试还是额外重试 total 次，面试时先说清约定）；失败后延迟重试用 setTimeout 包一层 Promise；最终失败要 reject **最后一次**的错误，而不是 undefined；每次重试都要重新调用 `fn()`（重新发起请求），绝不能复用同一个已 reject 的 Promise；能扩展「指数退避 backoff」是加分项。

```javascript
// ===== 5 分钟速写版 =====
function retry(fn, times = 3, delay = 0) {
  return new Promise((resolve, reject) => {
    const attempt = left => {
      fn().then(resolve, err => {
        if (left <= 0) return reject(err);   // reject 最后一次的真实错误
        setTimeout(() => attempt(left - 1), delay);
      });
    };
    attempt(times); // 约定：times 为额外重试次数，总尝试 = times + 1
  });
}

// ===== 标准完整版（含边界处理）=====
function retryPro(fn, { retries = 3, delay = 0, backoff = 1, shouldRetry = () => true } = {}) {
  return new Promise((resolve, reject) => {
    let attemptCount = 0;
    const attempt = () => {
      attemptCount++;
      Promise.resolve()
        .then(() => fn(attemptCount))          // 每次重试都重新调用，可把第几次传给业务
        .then(resolve)
        .catch(err => {
          // 可定制哪些错误才值得重试：如 4xx 参数错误重试无意义
          if (attemptCount > retries || !shouldRetry(err)) return reject(err);
          // 指数退避：delay * backoff^(n-1)，避免打挂下游
          const wait = delay * Math.pow(backoff, attemptCount - 1);
          setTimeout(attempt, wait);
        });
    };
    if (typeof fn !== 'function') return reject(new TypeError('fn must be a function'));
    attempt();
  });
}
// 用法：网络抖动重试 + 指数退避
// retryPro(() => fetch(url), { retries: 3, delay: 500, backoff: 2,
//   shouldRetry: e => !e.response || e.response.status >= 500 })
```

---
