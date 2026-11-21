---
title: [WCN-193] 笔试：手写组件级 fetch 重试包装器（指数退避 + 熔断 + 请求去重）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-193：笔试：手写组件级 fetch 重试包装器

**题目**：实现 `retryFetch(url, opts)`：① 网络错误/5xx 重试，4xx 不重试；② 指数退避（base 500ms，jitter ±30%），最多 3 次；③ 同一 URL 并发去重：进行中的相同请求共享同一 Promise；④ 连续失败 5 次后熔断 30s（期间直接 reject 'circuit-open'）；⑤ 成功重置熔断计数；⑥ 支持 AbortSignal 透传。

**答**：

```javascript
const inflight = new Map();
const breaker = new Map(); // url -> { fails, openUntil }

export async function retryFetch(url, { retries = 3, base = 500, signal, ...init } = {}) {
  // 并发去重：同 URL 共享 in-flight Promise
  if (inflight.has(url)) return inflight.get(url);

  const exec = (async () => {
    const b = breaker.get(url);
    if (b && b.openUntil > Date.now()) throw new Error('circuit-open');
    for (let attempt = 0; attempt <= retries; attempt++) {
      try {
        const res = await fetch(url, { ...init, signal });
        if (res.ok || (res.status >= 400 && res.status < 500)) {
          breaker.delete(url);                      // 成功重置熔断
          return res;
        }
        if (res.status < 500) return res;           // 4xx 语义错误不重试
        throw new Error(`http ${res.status}`);
      } catch (e) {
        if (e.name === 'AbortError') throw e;       // 用户取消不重试
        if (attempt === retries) {
          const b2 = breaker.get(url) ?? { fails: 0 };
          b2.fails++;
          if (b2.fails >= 5) b2.openUntil = Date.now() + 30000;  // 熔断 30s
          breaker.set(url, b2);
          throw e;
        }
        const jitter = 1 + (Math.random() * 0.6 - 0.3);          // ±30%
        await new Promise((r) => setTimeout(r, base * 2 ** attempt * jitter));
      }
    }
  })().finally(() => inflight.delete(url));

  inflight.set(url, exec);
  return exec;
}
// 组件用法：const res = await retryFetch('/api/list', { signal: this.#ac.signal });
```

**评分点**：
- 重试边界正确：5xx/网络错误重试、4xx 不重试、Abort 不重试。
- 指数退避带抖动（防雪崩同步重试）。
- 并发去重（inflight Map + finally 清理）。
- 熔断：连续失败计数、开路 30s、成功重置。
