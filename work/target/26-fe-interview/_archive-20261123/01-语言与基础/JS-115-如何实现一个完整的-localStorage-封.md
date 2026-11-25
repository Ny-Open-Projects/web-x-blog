---
title: [JS-115] 如何实现一个完整的 localStorage 封装？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-115：如何实现一个完整的 localStorage 封装？

**答**：
- 必备能力：命名空间前缀防冲突、JSON 序列化安全、TTL 过期、写满降级、跨页同步。
- 过期策略：value 包一层 `{ value, expire }`，读取时判断时间戳，过期即删并返回 null。
- `storage` 事件只在“其他”标签页触发（本页写入不触发本页监听），是跨页通信的标准通道。
- 容量超限（QuotaExceededError）要做淘汰或提示，序列化损坏要安全降级为 null。

```javascript
const store = {
  prefix: 'app:',
  _key(k) { return this.prefix + k; },

  set(key, value, expireMs = 0) {
    const item = { value, expire: expireMs ? Date.now() + expireMs : 0 };
    try {
      localStorage.setItem(this._key(key), JSON.stringify(item));
    } catch (e) {
      if (e.name === 'QuotaExceededError') {
        this._evictExpired();               // 先清本前缀的过期项再试一次
        try { localStorage.setItem(this._key(key), JSON.stringify(item)); } catch {}
      }
    }
  },

  get(key) {
    const raw = localStorage.getItem(this._key(key));
    if (raw === null) return null;
    try {
      const { value, expire } = JSON.parse(raw);
      if (expire && Date.now() > expire) { this.remove(key); return null; }
      return value;
    } catch {
      this.remove(key);                     // 数据损坏安全降级
      return null;
    }
  },

  remove(key) { localStorage.removeItem(this._key(key)); },

  _evictExpired() {
    for (let i = localStorage.length - 1; i >= 0; i--) {
      const k = localStorage.key(i);
      if (!k.startsWith(this.prefix)) continue;
      try {
        const { expire } = JSON.parse(localStorage.getItem(k));
        if (expire && Date.now() > expire) localStorage.removeItem(k);
      } catch { localStorage.removeItem(k); }
    }
  },
};

store.set('theme', 'dark');
store.set('token', 'abc', 60_000);          // 1 分钟过期
console.log(store.get('theme'));            // 'dark'

// 跨页同步：只在其他标签页触发
window.addEventListener('storage', (e) => {
  if (e.key === 'app:theme') {
    console.log('其他页面改了主题：', e.oldValue, '→', e.newValue);
  }
});
```
