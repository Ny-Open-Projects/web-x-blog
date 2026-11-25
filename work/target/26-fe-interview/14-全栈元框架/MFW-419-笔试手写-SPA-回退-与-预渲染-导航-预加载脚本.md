---
title: [MFW-419→MFW-419] 笔试：手写导航预加载调度脚本（Speculation Rules 数据源）
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-419：预加载调度
**答**：实现 `createLinkPrefetcher({Budget = 4} = {})`：1) 意图分层：hover(200ms 防抖)/touchstart/viewport(IntersectionObserver) 三触发器；2) 全局并发预算（同时 ≤4 在途预取——优先级队列：viewport > hover；新意图抢占最低优先者 abort）；3) 预取内容协商（Accept: text/html——仅当服务端该路由可缓存才存——响应头 no-store 直接弃）；4) 命中率统计上报（预取数/导航命中数——低于 20% 自动收紧触发器等级）；5) 单飞（同 URL 在途共享 Promise）。

```javascript
export function attachPreloader(router, { budget = 4, report }) {
  const inflight = new Map(), stats = { p: 0, h: 0 }
  const prio = new Map()                                          // url → 0|1

  function maybeFetch(url, level) {
    if (inflight.has(url) || servedRecently(url)) return
    if (activeCount() >= budget) preempts Lowest(priority < level)  // 抢占最低档
    const c = new AbortController()
    inflight.set(url, { c, level })
    fetch(speculateUrl(url), { signal: c.signal, priority: level ? 'low' : 'high' })
      .then((r) => { if (!cacheableByHeaders(r)) return           // no-store 弃
        cachePut(fetchBody(r)) })
      .finally(() => inflight.delete(url))
  }
  bindHover(200), bindViewport()                                   // 触发器注册
  // 导航命中：导航到 url 时若 cache.has(url) → stats.h++；上报 hitRate = h/p
  return { stats, setBudget: (n) => (budget = n),
    autoTune: () => { if (hitRate() < 0.2) raiseTriggerBar() } }    // <20% 收紧
}
```
**评分点**：
- 三触发器 + 优先级抢占（预算内保高价值——viewport 压过 hover）
- 服务端头协商（no-store 路由预取白费——读头弃缓存）
- 命中率自调参（<20% 收紧——预取不是越多越好）
- 单飞 + recently 去重（同 URL 风暴防护）
