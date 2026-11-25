---
title: [1102] 笔试手写：实现 store 变更时间线记录器
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 调试]
type: 笔试题
---

## 1102：笔试手写：实现 store 变更时间线记录器

**答**：实现 createTimeline(store) 返回包装后的 subscribe 记录器：每次变更记录 { ts, prev, next, changedKeys }（changedKeys 由 prev/next 浅比较得出）。提供 list() 返回最近 N=50 条（环形截断），filter(key) 按 key 过滤，summary() 输出各 key 变更次数 Top-5。

```js
function createTimeline(store, cap = 50) {
  const log = [];
  const push = entry => { log.push(entry); if (log.length > cap) log.shift(); }; // 环形截断
  return {
    record(prev, next) {
      const changedKeys = Object.keys(next)
        .filter(k => next[k] !== prev?.[k]);
      push({ ts: Date.now(), prev, next, changedKeys });
    },
    list: () => [...log],
    filter: key => log.filter(e => e.changedKeys.includes(key)),
    summary: () => Object.entries(
      log.flatMap(e => e.changedKeys).reduce((m, k) => ((m[k] = (m[k] || 0) + 1), m), {})
    ).sort((a, b) => b[1] - a[1]).slice(0, 5),
  };
}
```

**评分点**：
- 浅比较提取 changedKeys（变更归因最小单元）
- 环形缓冲 cap 限制（时间线不能无限膨胀）
- summary 聚合定位高频变更字段
- 能讨论：与 devtools 的时间旅行差异——这是轻量自建观测，跨字段 diff 需深比较
