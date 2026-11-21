---
title: [WEB-500] 笔试：手写带降级开关的 fetch 封装
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## WEB-500：笔试：手写带降级开关的 fetch 封装

**题目**：实现 `safeFetch(url, opts)`：失败时按优先级尝试缓存兜底（上次成功结果，TTL 5 分钟）→ 静态默认数据；开关可全局关闭降级（如调试时看真实错误）。

**答**：
```javascript
let fallbackEnabled = true;
const cache = new Map(); // url -> { data, at }

function setFallback(on) { fallbackEnabled = on; }

async function safeFetch(url, opts = {}) {
  try {
    const res = await fetch(url, opts);
    if (!res.ok) throw res.status;
    const data = await res.json();
    cache.set(url, { data, at: Date.now() });
    return { ok: true, data, degraded: false };
  } catch (err) {
    const hit = cache.get(url);
    if (!fallbackEnabled) throw err; // 调试模式直接抛
    if (hit && Date.now() - hit.at < 5 * 60_000) {
      return { ok: true, data: hit.data, degraded: 'stale' }; // 上次成功结果
    }
    const local = DEFAULTS[url];
    if (local) return { ok: true, data: local, degraded: 'default' };
    throw err; // 无兜底可降，仍要抛
  }
}
```

**评分点**：
- 降级三级链：新鲜缓存 → stale 缓存 → 默认数据，优先级明确
- 全局开关必须能关掉降级（否则调试时错误被吞，排查地狱）
- 返回结构带 degraded 标记，让 UI 能提示「展示的是缓存数据」
- 无兜底时的行为：仍抛错而不是返回 undefined
