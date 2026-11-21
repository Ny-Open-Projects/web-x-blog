---
title: [PER-318] Web Storage 的配额体系全景：localStorage/IndexedDB/Cache API 各自限额与淘汰策略是什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-318：Web Storage 的配额体系全景：localStorage/IndexedDB/Cache API 各自限额与淘汰策略是什么？

**答**：
- localStorage：同源约 5MB（各浏览器略有差异），字符串存储，写满抛 QuotaExceededError，永不自动淘汰（除非用户清缓存）——所以只能放小状态，且要 try-catch 写入。
- IndexedDB：现代浏览器按"源总配额"管理，Chrome 系给磁盘可用空间的较大比例（如 60%，总配额由 StorageManager.estimate() 查询），Firefox 约 2GB 起步/按空间比例。存储压力大时可被 **eviction 淘汰**（除非标记 persistent storage）。
- Cache API（Service Worker）：与 IndexedDB 共享源配额池，存响应体，同样参与淘汰；配额紧张时整组 Cache 可被清理。
- 淘汰规则：浏览器在配额压力下按"最近最少使用 + 源维度"整源淘汰，`navigator.storage.persist()` 申请持久化（用户授予后不参与自动淘汰，Chrome 按站点参与度/通知权限/书签等信号决定授予）。
- 设计原则：本地缓存分层——必存小状态（localStorage）、结构化数据（IndexedDB）、HTTP 缓存（Cache API），各自预估用量并对超限做降级（清老数据、提示用户）。

```javascript
// 配额查询与持久化申请
async function storageReport() {
  const { usage, quota } = await navigator.storage.estimate();
  return { usedMB: +(usage / 1048576).toFixed(1), quotaMB: +(quota / 1048576).toFixed(1),
           percent: +(usage / quota * 100).toFixed(1) };
}
// 持久化：申请成功则本源数据不会被配额压力整源淘汰
const persisted = await navigator.storage.persisted?.() ?? false
  || await navigator.storage.persist?.();
// localStorage 写入兜底：
function safeSet(key, val) {
  try { localStorage.setItem(key, val); return true; }
  catch (e) {                                        // QuotaExceededError
    const keys = Object.keys(localStorage).sort();   // 简单策略：清最老的缓存键
    for (const k of keys.filter((k) => k.startsWith('cache:'))) localStorage.removeItem(k);
    try { localStorage.setItem(key, val); return true; } catch { return false; }
  }
}
```
