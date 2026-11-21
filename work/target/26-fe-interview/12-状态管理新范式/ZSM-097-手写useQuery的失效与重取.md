---
title: [ZSM-097] 笔试：手写 QueryClient 的 invalidateQueries（前缀匹配失效 + 活跃重取）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-097：手写 QueryClient 的 invalidateQueries（前缀匹配失效 + 活跃重取）

**题目要求**：
- 在 ZSM-096 基础上实现 `qc.invalidateQueries({ queryKey })`：把所有「以 queryKey 为前缀」的缓存标记 stale，并对当前有订阅者的 key 立即重取（调用其最近一次使用的 fn）。
- 要求 key 匹配是结构化前缀：`['goods']` 匹配 `['goods', 'detail', 1]`，不匹配 `['goodsx']`。

```javascript
const activeObservers = new Map() // kstr → { fn, staleTime, retry, subs: Set }

class QueryClient {
  invalidateQueries({ queryKey }) {
    const prefix = JSON.stringify(queryKey).slice(1, -1) // 去掉外层括号做前缀比较
    for (const [kstr, obs] of activeObservers) {
      const inner = kstr.slice(1, -1)
      // 前缀匹配：以 prefix 开头且下一字符是 , 或 ]（防止 'goods' 匹配 'goodsx'）
      if (inner === prefix || inner.startsWith(prefix + ',')) {
        const e = cache.get(kstr)
        if (e) e.stale = true
        if (obs.subs.size > 0) {
          fetchOnce({ kstr: kstr, key: queryKey.length ? kstr : null, fn: obs.fn,
                      staleTime: 0, retry: obs.retry }).catch(() => {})
        }
      }
    }
  }
  subscribeQuery(kstr, meta, cb) { /* 注册 activeObservers 与 subs 计数 */ }
}
```

**评分点**：
- 前缀匹配正确实现（空参、深层 key、防 'goodsx' 误匹配——考官重点看边界字符）。
- 无订阅者的 key 只标记 stale 不请求；有订阅者立即重取。
- 重取使用该查询最后一次的 queryFn 与参数。
- 能口述与真实 TanStack Query 的差异：真实实现按 query hash 精确比较 + observer 列表，这里用字符串前缀模拟。
