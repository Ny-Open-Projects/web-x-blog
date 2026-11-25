---
title: [PER-1067] 手写一个请求去重合并器（batch + inflight 双模式）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1067：手写一个请求去重合并器（batch + inflight 双模式）

**答**：
- 需求：实现 createFetcher() 返回 { get(url), batchGet(ids) }。get：同 URL 并发请求共享同一 Promise；batchGet：30ms 窗口收集 id 调用 batch API（POST /batch { ids }），按返回 id 映射 resolve/reject；两种模式各自独立工作。
- 边界：batch 返回缺 id 视为 404；请求失败整批 reject；窗口内空批次不触发；get 的缓存 Promise 失败后从 map 移除允许重试。
- 评分点：inflight 共享与清理；窗口合批；缺 id 404；失败整批

```javascript
function createFetcher() {
  const inflight = new Map();
  const get = url => {
    if (inflight.has(url)) return inflight.get(url);
    const p = fetch(url).then(r => {
      if (!r.ok) throw Object.assign(new Error('http ' + r.status), { status: r.status });
      return r.json();
    }).finally(() => inflight.delete(url));       // 失败也移除，允许重试
    inflight.set(url, p);
    return p;
  };
  let batch = [], timer = null;
  const batchGet = id => new Promise((resolve, reject) => {
    batch.push({ id, resolve, reject });
    clearTimeout(timer);
    timer = setTimeout(async () => {
      const b = batch; batch = [];
      if (!b.length) return;
      try {
        const r = await fetch('/batch', { method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ ids: b.map(x => x.id) }) });
        const list = await r.json();
        const map = new Map(list.map(x => [x.id, x]));
        for (const x of b) map.has(x.id) ? x.resolve(map.get(x.id)) : x.reject(new Error('404'));
      } catch (e) { b.forEach(x => x.reject(e)); }
    }, 30);
  });
  return { get, batchGet };
}
```
