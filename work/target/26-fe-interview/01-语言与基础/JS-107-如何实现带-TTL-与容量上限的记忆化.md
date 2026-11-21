---
title: [JS-107] 如何实现带 TTL 与容量上限的记忆化？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-107：如何实现带 TTL 与容量上限的记忆化？

**答**：
- 基础记忆化：Map 以 `keyFn(args)` 为键缓存返回值，命中直接返回。
- TTL：记录写入时间戳，超过有效期作废重算，适合 token、配置等会过期的数据。
- 容量上限：超出 max 时按 Map 插入序淘汰最旧条目（简易 LRU 语义）。
- 异步函数注意：失败的结果不能缓存，Promise reject 后要清除对应缓存键。

```javascript
function memoize(fn, { ttl = Infinity, max = 100, keyFn = (args) => JSON.stringify(args) } = {}) {
  const cache = new Map(); // key → { value, expire }
  return function (...args) {
    const key = keyFn(args);
    const now = Date.now();
    const hit = cache.get(key);
    if (hit && (hit.expire === Infinity || now < hit.expire)) return hit.value;
    if (hit) cache.delete(key); // 过期条目清理

    const value = fn.apply(this, args);
    cache.set(key, { value, expire: ttl === Infinity ? Infinity : now + ttl });

    if (cache.size > max) cache.delete(cache.keys().next().value); // 淘汰最旧

    // 异步函数：失败不缓存，避免错误被"记住"
    if (value && typeof value.then === 'function') {
      value.catch(() => cache.delete(key));
    }
    return value;
  };
}

let calls = 0;
const getUser = memoize(
  async (id) => { calls++; return { id, at: Date.now() }; },
  { ttl: 500, max: 10 }
);

(async () => {
  const a = await getUser(1);
  const b = await getUser(1);        // 命中缓存
  console.log(a === b, calls);       // true 1
  await new Promise((r) => setTimeout(r, 600));
  await getUser(1);                  // TTL 过期重算
  console.log(calls);                // 2
})();
```
