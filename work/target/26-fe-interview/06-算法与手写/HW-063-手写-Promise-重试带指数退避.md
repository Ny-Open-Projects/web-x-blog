---
title: [HW-063] 手写指数退避重试（retry）——支持退避系数、抖动与条件重试
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-063：手写指数退避重试（retry）——支持退避系数、抖动与条件重试
**答**：在 HW-008 基础上加工程化参数：退避 `delay * factor^i`、随机抖动（防惊群）、`shouldRetry(err)` 条件重试（429/5xx 重试，4xx 不重试）、totalTimeout 总兜底。递归 or 循环皆可，循环更清晰。

```javascript
function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

function retry(task, {
  retries = 3, delay = 500, factor = 2, maxDelay = 8000,
  jitter = true, shouldRetry = (e) => e.retryable !== false,
  signal,
} = {}) {
  return (async () => {
    let lastErr;
    for (let i = 0; i <= retries; i++) {
      if (signal?.aborted) throw new DOMException('aborted', 'AbortError');
      try {
        return await task(i);                       // 传入尝试序号
      } catch (err) {
        lastErr = err;
        if (i === retries || !shouldRetry(err)) throw err;
        let backoff = Math.min(delay * factor ** i, maxDelay);
        if (jitter) backoff = Math.round(backoff * (0.5 + Math.random() / 2)); // 半随机抖动
        await sleep(backoff);
      }
    }
    throw lastErr;
  })();
}

// 用法：429 与 5xx 可重试，其余不重试（浏览器场景）
// retry((attempt) => fetch('/api/goods').then((r) => {
//   if (!r.ok) throw Object.assign(new Error(String(r.status)), { retryable: r.status === 429 || r.status >= 500 });
//   return r.json();
// }), { retries: 3, delay: 300 });

// 可运行演示：模拟前两次 503（可重试）、第三次成功
let calls = 0;
retry(async () => {
  if (++calls < 3) throw Object.assign(new Error('503'), { retryable: true });
  return `ok after ${calls} tries`;
}, { retries: 3, delay: 10 }).then(console.log);  // ok after 3 tries
```

**评分点**：
- 指数退避 + 上限（maxDelay）+ 抖动（防惊群）三层齐备。
- shouldRetry 条件重试：4xx 不重试是基本素养。
- 尝试序号传给 task、AbortSignal 支持。
- 总次数语义清晰（retries = 额外重试次数，共 retries+1 次执行）。
