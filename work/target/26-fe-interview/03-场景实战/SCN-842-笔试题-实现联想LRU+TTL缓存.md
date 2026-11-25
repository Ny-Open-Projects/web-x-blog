---
title: [SCN-842] 笔试题——实现联想缓存（LRU + TTL + 版本失效 + 会话恢复）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-842：手写联想缓存

**需求与边界**：
- 需求：LRU 容量 20 + TTL 30s；服务端版本号不一致全量失效；个性化开关变化失效（登录态）；支持「序列化导出」供会话恢复。
- 边界：① 过期即视为 miss（不返回旧数据）；② touch 语义正确（命中移到末尾）；③ 版本检查惰性（读取时比对）+ 主动（广播失效）双通道。

**答**：
```javascript
function createSuggestCache({ cap = 20, ttl = 30_000 } = {}) {
  const store = new Map();                             // key -> {data, ts, ver, persona}
  let serverVersion = null;
  function get(key, { version, persona }) {
    const e = store.get(key);
    if (!e) return null;
    if (Date.now() - e.ts > ttl) { store.delete(key); return null; }   // TTL miss
    if (e.ver !== version || e.persona !== persona) {  // 版本/个性化不一致 = 失效
      store.delete(key); return null;
    }
    store.delete(key); store.set(key, e);              // LRU touch
    return e.data;
  }
  function set(key, data, { version, persona }) {
    if (store.size >= cap) store.delete(store.keys().next().value);
    store.set(key, { data, ts: Date.now(), ver: version, persona });
  }
  function onVersionChange(newVer) {                   // 主动失效（屏蔽词推送）
    serverVersion = newVer;
    for (const [k, e] of store) if (e.ver !== newVer) store.delete(k);
  }
  function serialize() { return [...store.entries()]; }        // 会话恢复
  function restore(entries) { entries.forEach(([k, v]) => store.set(k, v)); }
  return { get, set, onVersionChange, serialize, restore, get size() { return store.size; } };
}
```

**评分点**:
- TTL + LRU 双语义正确（过期即删、touch 移尾）。
- 版本与个性化双维失效键（persona 变化清缓存）。
- 主动失效（onVersionChange）+ 惰性校验双通道。
- serialize/restore 支持跨页面会话恢复。
