---
title: [WEB-504] 笔试：手写 stale-while-revalidate 语义的缓存请求
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 缓存]
type: 笔试题
---

## WEB-504：笔试：手写 stale-while-revalidate 语义的缓存请求

**题目**：实现 `swrFetch(url)`：有新鲜缓存（<60s）直接返回；有过期缓存立即返回旧值、后台刷新、下次拿到新值；无缓存走网络。

**答**：
```javascript
const store = new Map(); // url -> { data, at, refreshing }

async function swrFetch(url) {
  const rec = store.get(url);
  const FRESH = 60_000;

  if (rec && Date.now() - rec.at < FRESH) {
    return { data: rec.data, stale: false };
  }

  if (rec && !rec.refreshing) {
    rec.refreshing = fetch(url)
      .then(r => r.ok ? r.json() : Promise.reject(r.status))
      .then(data => { store.set(url, { data, at: Date.now() }); })
      .finally(() => { rec.refreshing = false; });
    return { data: rec.data, stale: true }; // 立即返回旧值
  }
  if (rec?.refreshing) return { data: rec.data, stale: true };

  // 无缓存：走网络
  const data = await fetch(url).then(r => { if (!r.ok) throw r.status; return r.json(); });
  store.set(url, { data, at: Date.now() });
  return { data, stale: false };
}
```

**评分点**：
- 三分支语义完整：新鲜直返 / 过期先返旧值再后台刷新 / 无缓存走网络
- refreshing 标志防止并发后台刷新重复发请求
- 返回 stale 标记让 UI 可提示「数据可能过期」
- 后台刷新失败要清理 refreshing，且不覆盖旧缓存（降级语义）
