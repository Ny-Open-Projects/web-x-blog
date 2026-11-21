---
title: [PER-324] 缓存写入的原子性与并发：多标签页同时写 Cache/IDB 如何避免半写与覆盖丢失？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-324：缓存写入的原子性与并发：多标签页同时写 Cache/IDB 如何避免半写与覆盖丢失？

**答**：
- 半写问题：一次逻辑更新写多个 key（元数据+数据），中途失败/配额满会留下不一致状态。方案：IDB 用单事务包裹多写（原子）；Cache API 无事务——先写数据再写"提交标记"（两阶段：数据 key 带 `_staging` 前缀，全部成功后原子写 meta 指针切换，读侧只认 meta 指向的版本）。
- 并发覆盖丢失：多标签页对同一 key 的"读-改-写"会互相覆盖（last-write-wins 丢更新）。方案：Web Locks API 互斥临界区；或写时带版本号做 CAS（读到的版本不匹配则重读重试）；或广播合并（BroadcastChannel 传播变更让各页合并内存态）。
- IDB 自带同源多连接的读写隔离（事务隔离级别 readwrite 锁 objectStore 粒度），同一事务内不会交错；跨标签页的"先读后写"仍需应用层锁。
- 验证手段：模拟两标签页并发 1000 次读改写计数器，验证终值正确（无锁会丢更新）。

```javascript
// Cache API 两阶段提交：meta 指针切换保证读侧原子
async function stagedPut(cacheName, key, data) {
  const cache = await caches.open(cacheName);
  const stagingUrl = `${key}?_staging=${Date.now()}`;
  await cache.put(stagingUrl, data);                    // 1. 先写 staging（可失败重试）
  const meta = await cache.match(key + '?_meta');
  const versions = meta ? await meta.json() : { current: null, prev: null };
  await cache.put(key + '?_meta', new Response(JSON.stringify({
    current: stagingUrl, prev: versions.current,        // 2. 原子切指针（单 key 写）
  })));
}
async function stagedGet(cacheName, key) {
  const cache = await caches.open(cacheName);
  const meta = await cache.match(key + '?_meta');
  const { current } = meta ? await meta.json() : { current: null };
  return current ? cache.match(current) : null;         // 读侧永远读到完整版本
}
// 多标签页读改写互斥：
async function withLock(key, fn) {
  return navigator.locks.request(`rw:${key}`, async () => fn());
}
```
