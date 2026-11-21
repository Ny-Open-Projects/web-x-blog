---
title: [JS-189] 设计一个缓存层？内存 + storage 两级、TTL、版本失效怎么实现？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-189：设计一个缓存层？内存 + storage 两级、TTL、版本失效怎么实现？

**答**：
- 两级结构：L1 内存 Map（同步、快、刷新即失）→ L2 localStorage/IndexedDB（持久、慢、跨刷新）；读取 L1 miss 才穿透 L2 并回填 L1。
- 值包装为 { v, expireAt, ... }，采用懒过期：读取时才判断 TTL，写路径顺带删过期项，避免全量扫描。
- 版本失效：key 统一带版本前缀（如 `c:v2:user:1`），发版升版本号即整体失效；旧版本数据由 clearVersion 惰性清扫，不做启动时全删。
- 容错三件套：JSON 解析失败视为 miss、QuotaExceededError 降级纯内存、同 key 并发加载共享 inflight Promise 防击穿。
- 对外只暴露 get/set/del/clearVersion，业务侧传入 loader 即"读缓存 → 未命中取数 → 回填"。

```javascript
// 1. 两级缓存：内存 L1 + localStorage L2，TTL + 版本号
function createCache({ prefix = 'c:', version = 'v1', storage = localStorage } = {}) {
  const mem = new Map();
  const inflight = new Map();                       // 防击穿：同 key 并发共享加载 Promise
  const key = (k) => `${prefix}${version}:${k}`;

  const readL2 = (k) => {
    try {
      const raw = storage.getItem(key(k));
      if (!raw) return null;
      const item = JSON.parse(raw);
      if (item.expireAt && item.expireAt < Date.now()) {  // 懒过期
        storage.removeItem(key(k));
        return null;
      }
      return item.v;
    } catch { return null; }                        // 解析失败视为 miss
  };
  const writeL2 = (k, v, ttl) => {
    try {
      storage.setItem(key(k), JSON.stringify({ v, expireAt: ttl ? Date.now() + ttl : 0 }));
    } catch { /* 容量满：降级为纯内存缓存，不抛错 */ }
  };

  async function get(k, loader, { ttl = 5 * 60_000 } = {}) {
    if (mem.has(k)) return mem.get(k);              // L1
    const hit = readL2(k);                          // L2
    if (hit !== null) { mem.set(k, hit); return hit; }
    if (inflight.has(k)) return inflight.get(k);    // 并发去重
    const p = Promise.resolve()
      .then(loader)                                 // 穿透取数
      .then((v) => { mem.set(k, v); writeL2(k, v, ttl); return v; })
      .finally(() => inflight.delete(k));
    inflight.set(k, p);
    return p;
  }
  const set = (k, v, ttl) => { mem.set(k, v); writeL2(k, v, ttl); };
  const del = (k) => { mem.delete(k); storage.removeItem(key(k)); };
  function clearVersion() {                         // 清扫旧版本残留（发版后调一次）
    Object.keys(storage)
      .filter((k) => k.startsWith(prefix) && !k.startsWith(`${prefix}${version}:`))
      .forEach((k) => storage.removeItem(k));
  }
  return { get, set, del, clearVersion };
}

// 2. 使用：接口结果缓存，穿透才发请求，二次读取零请求
const cache = createCache({ version: 'v2' });
async function getUser(id) {
  return cache.get(
    `user:${id}`,
    () => fetch('/api/user/' + id).then((r) => r.json()),
    { ttl: 60_000 },
  );
}
getUser(1).then((u) => console.log('首次网络', u));
getUser(1).then((u) => console.log('二次命中', u));
```
