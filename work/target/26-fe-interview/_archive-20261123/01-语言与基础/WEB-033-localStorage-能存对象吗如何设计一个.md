---
title: [WEB-033] localStorage 能存对象吗？如何设计一个带过期时间的封装？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-033：localStorage 能存对象吗？如何设计一个带过期时间的封装？
**答**：
- localStorage 只存字符串，对象需 JSON 序列化；读取时要 try/catch 防止脏数据导致解析异常。
- 原生没有过期机制，封装时在值里塞 `expires` 字段，读取时校验，过期即删除返回 null。
- 生产封装还应统一 namespace、容量异常（QuotaExceededError）兜底、SSR 环境判空。

```javascript
// 带过期时间与异常兜底的 storage 封装，贴近真实工程
const NS = 'app:';
const storage = {
  set(key, value, ttlMs) {
    const record = {
      value,
      expires: ttlMs ? Date.now() + ttlMs : null,
    };
    try {
      localStorage.setItem(NS + key, JSON.stringify(record));
    } catch (e) {
      // 存储已满：清理过期项后重试一次
      if (e.name === 'QuotaExceededError') {
        this.sweep();
        localStorage.setItem(NS + key, JSON.stringify(record));
      }
    }
  },
  get(key) {
    try {
      const raw = localStorage.getItem(NS + key);
      if (!raw) return null;
      const record = JSON.parse(raw);
      if (record.expires && Date.now() > record.expires) {
        localStorage.removeItem(NS + key);
        return null; // 已过期
      }
      return record.value;
    } catch {
      return null; // 脏数据兜底
    }
  },
  sweep() {
    Object.keys(localStorage)
      .filter((k) => k.startsWith(NS))
      .forEach((k) => {
        try {
          const r = JSON.parse(localStorage.getItem(k));
          if (r.expires && Date.now() > r.expires) localStorage.removeItem(k);
        } catch {
          /* ignore */
        }
      });
  },
};

storage.set('search-history', ['vue', 'http'], 24 * 60 * 60 * 1000); // 一天后自动失效
console.log(storage.get('search-history'));
```

## 六、同源策略与跨域
