---
title: [ALG-160] 发新版后用户 localStorage 里还躺着旧数据结构，直接读会字段错乱。如何用构建版本号做缓存失效与数据迁移？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-160：发新版后用户 localStorage 里还躺着旧数据结构，直接读会字段错乱。如何用构建版本号做缓存失效与数据迁移？
**答**：缓存 key 带构建 hash（构建时注入），读取时：① 当前版本命中直接用；② 未命中则扫描旧版本 key，按迁移函数转换字段（补默认值、改结构），写回新 key、删除旧 key；③ 无旧数据给默认值。要点：迁移要幂等且容错（try/catch 防脏数据），一次性迁移后清理，避免多版本残留。

```javascript
const BUILD_VERSION = 'a1b2c3';      // 构建时注入的 hash
const KEY = v => `cart:${v}`;
function loadCart() {
  const current = localStorage.getItem(KEY(BUILD_VERSION));
  if (current) return JSON.parse(current);
  // 版本迁移：扫描旧版本 key
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (k && k.startsWith('cart:') && k !== KEY(BUILD_VERSION)) {
      try {
        const old = JSON.parse(localStorage.getItem(k));
        // 迁移函数：补默认字段、结构转换（幂等）
        const migrated = {
          items: old.items || [],
          currency: old.currency || 'CNY', // 旧版没有的新字段
        };
        localStorage.setItem(KEY(BUILD_VERSION), JSON.stringify(migrated));
        localStorage.removeItem(k);        // 清理旧版本，防多版本残留
        return migrated;
      } catch { localStorage.removeItem(k); } // 脏数据直接丢
    }
  }
  return { items: [], currency: 'CNY' };
}
```
