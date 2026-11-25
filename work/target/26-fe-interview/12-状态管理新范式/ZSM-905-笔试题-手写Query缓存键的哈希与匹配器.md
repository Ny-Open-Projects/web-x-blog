---
title: [905] 笔试手写：实现 QueryKey 的哈希与前缀匹配失效
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 笔试题, TanStack Query, 缓存]
type: 笔试题
---

## 905：笔试手写：实现 QueryKey 的哈希与前缀匹配失效

**答**：实现 QueryCache：buildKey(parts)（对象键按字母序稳定序列化，数组保持顺序）与 invalidate(prefix)（prefix 为部分数组——命中所有以此为前缀的 key）。输出被失效的 key 列表。

```js
function hashKey(parts) {
  return JSON.stringify(parts.map(p =>
    p && typeof p === 'object' && !Array.isArray(p)
      ? Object.keys(p).sort().reduce((o, k) => (o[k] = p[k], o), {})
      : p));                              // 对象键排序保证稳定哈希
}
class QueryCache {
  constructor() { this.map = new Map(); }   // hash -> { key, data }
  set(key, data) { this.map.set(hashKey(key), { key, data }); }
  get(key) { return this.map.get(hashKey(key))?.data; }
  invalidate(prefix) {
    const p = hashKey(prefix);
    const hit = [];
    for (const [h, entry] of this.map) {
      if (h.startsWith(p.slice(0, -1) + ',')) {   // 前缀按「序列化段」匹配
        entry.stale = true;
        hit.push(entry.key);
      }
    }
    return hit;
  }
}
const c = new QueryCache();
c.set(['user', 'detail', 1], { name: 'a' });
c.set(['user', 'list'], [{}, {}]);
c.set(['order'], {});
console.log(c.invalidate(['user']));   // 两个 user key
```

**评分点**：
- 对象键字母序稳定序列化（键顺序无关哈希）
- 前缀匹配按序列化段边界（user 不能匹配 userX——漏边界是经典 bug）
- invalidate 标 stale 而非删除（保留数据做 fallback）
- 能讨论：真实 TanStack 用结构化深比较而非字符串前缀（性能与正确性取舍）

