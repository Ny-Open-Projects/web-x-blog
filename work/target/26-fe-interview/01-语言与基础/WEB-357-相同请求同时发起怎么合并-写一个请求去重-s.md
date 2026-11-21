---
title: [WEB-357] 相同请求同时发起怎么合并？写一个请求去重（same-flight）实现
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 笔试题
---

## WEB-357：相同请求同时发起怎么合并？写一个请求去重（same-flight）实现
**答**：
- key 用 URL+参数序列化（注意对象键顺序，用稳定序列化），在飞请求存 Promise，后续同 key 复用。
- 请求结束删除 key，保证下一轮可重新发起；失败也要删除并 reject 所有等待者。
- 扩展：带 TTL 的"短期缓存"= 去重 + 过期；注意不要对带副作用的 POST 去重。

```javascript
const inflight = new Map();
const stableKey = (url, params) => url + JSON.stringify(sortKeys(params || {}));
function dedupeFetch(url, params, opts) {
  const key = stableKey(url, params);
  if (inflight.has(key)) return inflight.get(key);
  const p = fetch(url + '?' + qs(params), opts)
    .then(r => r.json())
    .finally(() => inflight.delete(key)); // 成功失败都释放
  inflight.set(key, p);
  return p;
}
const sortKeys = o => Object.fromEntries(Object.entries(o).sort(([a], [b]) => a < b ? -1 : 1));
dedupeFetch('/api/goods', { page: 1 });
dedupeFetch('/api/goods', { page: 1 });   // 同一 Promise，只发一次
```

**评分点**：
- 结论先行，机制一句话讲透
- 覆盖攻击面/异常分支与边界条件
- 代码可运行、命名清晰、有防御性处理
- 主动给出工程取舍与常见坑
