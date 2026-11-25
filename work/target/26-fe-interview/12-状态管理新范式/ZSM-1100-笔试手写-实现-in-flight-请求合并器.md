---
title: [1100] 笔试手写：实现 in-flight 请求合并器
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, TanStack Query]
type: 笔试题
---

## 1100：笔试手写：实现 in-flight 请求合并器

**答**：实现 createDedupe(fetcher)：返回 request(key) => Promise。同 key 的并发请求共享同一个 in-flight Promise（第一个调用发起取数，后续调用直接挂到同一 Promise）；完成后 in-flight 记录清除（下次重新请求）；失败的 Promise 对所有等待者一致 reject 且同样清除。

```js
function createDedupe(fetcher) {
  const inflight = new Map();
  return {
    request(key) {
      if (inflight.has(key)) return inflight.get(key); // 共享
      const p = fetcher(key).finally(() => inflight.delete(key)); // 成败都清
      inflight.set(key, p);
      return p;
    },
    size: () => inflight.size,
  };
}
```

**评分点**：
- in-flight Map 存 Promise 本体（后续调用直接挂）
- finally 清除——失败也不能让坏 Promise 永久缓存
- 所有等待者共享同一结果（成功与错误一致传播）
- 能讨论：与 SWR dedupingInterval 的差异——这是时间窗去重之外的并发去重
