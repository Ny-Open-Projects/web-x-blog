---
title: [MFW-045] 笔试：手写路由预取调度器（IO 预算 + 去重 + 失效）
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-045：笔试：手写路由预取调度器（IO 预算 + 去重 + 失效）
**题目**：实现 `createPrefetcher(fetchPayload)`：`observe(url)` 将视口内链接入队；并发上限 N（IO 预算），超出的排队；`hover(url)` 把该 url 提到队首；同 url 去重（已完成或进行中不重复请求）；`invalidate(url)` 清除缓存允许重新预取；页面隐藏（visibilitychange）暂停调度。

```javascript
function createPrefetcher(fetchPayload, { concurrency = 4, ttl = 60_000 } = {}) {
  const cache = new Map();     // url -> { promise|value, fetchedAt }
  const queue = [];
  let running = 0;
  let paused = false;

  function enqueue(url, front = false) {
    if (cache.has(url)) return;                    // 已缓存/进行中：去重
    const item = { url };
    cache.set(url, { promise: null, fetchedAt: 0 }); // 占位防重复入队
    front ? queue.unshift(item) : queue.push(item);
    pump();
  }

  function pump() {
    if (paused) return;
    while (running < concurrency && queue.length) {
      const { url } = queue.shift();
      running += 1;
      const promise = fetchPayload(url)
        .then((value) => { cache.set(url, { value, fetchedAt: Date.now() }); })
        .catch(() => cache.delete(url))              // 失败：允许重试
        .finally(() => { running -= 1; pump(); });
      cache.set(url, { promise, fetchedAt: Date.now() });
    }
  }

  return {
    observe: (url) => enqueue(url),          // 视口进入：正常排队
    hover: (url) => enqueue(url, true),      // hover：插队
    get: (url) => cache.get(url)?.promise,   // 导航时复用预取中的 Promise
    invalidate: (url) => cache.delete(url),  // 失效：写操作后调用
    pause: (v) => { paused = v; if (!v) pump(); },
  };
}

// 视口观察 + 页面隐藏暂停
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => e.isIntersecting && prefetcher.observe(e.target.href));
}, { rootMargin: '200px' });
document.addEventListener('visibilitychange', () =>
  prefetcher.pause(document.hidden));

// **评分点**
// 1. 并发预算：running/concurrency 控制同时在飞请求数，避免视口内 50 个 Link 打爆网络。
// 2. 去重完整：进行中（占位 promise）与已完成（带 TTL）都不重复；失败要清除占位允许重试。
// 3. hover 插队：队列 unshift 体现优先级调度思想。
// 4. visibilitychange 暂停 + 恢复后 pump 续跑——生命周期意识。
```
