---
title: [1119] 笔试手写：实现 useQueryPrefetchOnHover
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 预取]
type: 笔试题
---

## 1119：笔试手写：实现 useQueryPrefetchOnHover

**答**：实现 createPrefetcher(fetcher)：prefetch(key) 悬停预取。规则：冷却窗 cooldownMs 内同 key 不重复预取；预取结果缓存 hitMs 内后续 request(key) 直接命中；request 走缓存-未命中再取数；未完成的预取被 request 复用（in-flight 合流）；组件卸载 cancelAll() 取消所有 in-flight。

```js
function createPrefetcher(fetcher, { cooldownMs = 500, hitMs = 5000 } = {}) {
  const cache = new Map(), last = new Map(), inflight = new Map();
  return {
    prefetch(key, now = Date.now()) {
      if (now - (last.get(key) || 0) < cooldownMs) return; // 冷却窗
      last.set(key, now);
      if (cache.has(key) || inflight.has(key)) return; // 已缓存/已在途
      const p = fetcher(key).then(v => { cache.set(key, { v, at: now }); inflight.delete(key); })
        .catch(e => { inflight.delete(key); throw e; });
      inflight.set(key, p);
    },
    async request(key, now = Date.now()) {
      const c = cache.get(key);
      if (c && now - c.at < hitMs) return c.v; // 命中窗口
      if (inflight.has(key)) return inflight.get(key); // 复用在途
      const v = await fetcher(key);
      cache.set(key, { v, at: now });
      return v;
    },
    cancelAll: () => inflight.clear(),
  };
}
```

**评分点**：
- 冷却窗 + 命中窗双时间参数（预取节流与新鲜度分离）
- in-flight 合流（预取与正式请求共用）
- cancelAll 对应组件卸载清理
- 能讨论：预取的取消语义——fetch 无法真取消时至少丢弃结果
