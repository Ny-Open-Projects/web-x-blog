---
title: [WEB-492] 笔试：手写 localStorage 封装
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 存储]
type: 笔试题
---

## WEB-492：笔试：手写 localStorage 封装

**题目**：实现带过期时间、命名空间隔离、写入容量兜底的 storage 工具：`set/get/remove`；过期自动视为不存在；QuotaExceededError 时清理最旧数据后重试。

**答**：
```javascript
const NS = 'app:';
function set(key, value, ttlMs) {
  const rec = { v: value, e: ttlMs ? Date.now() + ttlMs : 0 };
  try {
    localStorage.setItem(NS + key, JSON.stringify(rec));
  } catch (e) {
    if (e.name !== 'QuotaExceededError') throw e;
    // 容量兜底：清掉带时间戳的旧数据后重试
    Object.keys(localStorage)
      .filter(k => k.startsWith(NS))
      .map(k => [k, JSON.parse(localStorage.getItem(k)).t || 0])
      .sort((a, b) => a[1] - b[1])
      .slice(0, Math.ceil(localStorage.length / 3))
      .forEach(([k]) => localStorage.removeItem(k));
    localStorage.setItem(NS + key, JSON.stringify(rec));
  }
}
function get(key) {
  const raw = localStorage.getItem(NS + key);
  if (!raw) return null;
  const { v, e, t } = JSON.parse(raw);
  if (e && Date.now() > e) { localStorage.removeItem(NS + key); return null; }
  return v;
}
function remove(key) { localStorage.removeItem(NS + key); }
```

**评分点**：
- 过期时间写在记录内部（元数据包裹），读取时惰性校验
- 命名空间前缀隔离，避免与其他业务互踩
- 容量兜底：捕获 QuotaExceededError、清理策略、重试写入，三步齐全
- try/JSON.parse 对脏数据的容错处理（可加分）
