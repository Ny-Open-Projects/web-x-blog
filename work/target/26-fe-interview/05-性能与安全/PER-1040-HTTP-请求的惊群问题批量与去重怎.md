---
title: [PER-1040] HTTP 请求的"惊群"问题：批量与去重怎么实现
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1040：HTTP 请求的"惊群"问题：批量与去重怎么实现

**答**：
- 惊群场景：列表 100 个卡片各自请求详情、重复挂载组件重复请求同接口——同时打爆服务器。
- 去重：同 URL 同参数的并发请求共享一个 Promise（in-flight map）。
- 合并：微任务窗口内收集同型请求合并成批量接口（batch API），服务端拆分处理。
- 预取节制：预取也会惊群（列表滚动 prefetch 全部），配额 + 只预取可视区附近。

```javascript
const inflight = new Map();
function dedupeFetch(url, init) {
  const key = url + JSON.stringify(init?.body ?? '');
  if (inflight.has(key)) return inflight.get(key);
  const p = fetch(url, init).finally(() => inflight.delete(key));
  inflight.set(key, p);
  return p;
}
// 批量合并：30ms 微任务窗口收集
let batch = [], timer = null;
function batchedGet(id) {
  return new Promise((resolve, reject) => {
    batch.push({ id, resolve, reject });
    clearTimeout(timer);
    timer = setTimeout(async () => {
      const b = batch; batch = [];
      try {
        const r = await fetch('/batch', { method: 'POST',
          body: JSON.stringify({ ids: b.map(x => x.id) }) });
        const map = Object.fromEntries((await r.json()).map(x => [x.id, x]));
        b.forEach(x => map[x.id] ? x.resolve(map[x.id]) : x.reject(new Error('404')));
      } catch (e) { b.forEach(x => x.reject(e)); }
    }, 30);
  });
}
```
