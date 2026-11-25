---
title: [SCN-837] 笔试题——实现联想输入引擎（防抖 + seq 竞态 + LRU 缓存 + IME 守护）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-837：手写联想输入引擎

**需求与边界**：
- 需求：整合防抖（150ms）、seq 竞态守卫、LRU+TTL 缓存（上限 20，TTL 30s）、IME composing 守护、abort 取消。
- 边界：① composing 期间不请求但缓存上屏后的查询；② 缓存命中同步返回；③ abort 后 seq 守卫仍生效（双保险）；④ minLen=2 以下不请求返回空。

**答**：
```javascript
function createSuggestEngine(api, { debounceMs = 150, ttl = 30_000, cap = 20 } = {}) {
  const cache = new Map();                             // LRU：插入序
  let seq = 0, ctrl = null, timer = null, composing = false;
  function onInput(q) {
    if (composing) return { skipped: 'composing' };    // IME 守护
    if (q.length < 2) return { items: [] };            // 短前缀不请求
    clearTimeout(timer);
    timer = setTimeout(() => fire(q), debounceMs);
    return { pending: true };
  }
  async function fire(q) {
    const hit = cache.get(q);
    if (hit && Date.now() - hit.ts < ttl) {            // 命中：LRU touch
      cache.delete(q); cache.set(q, hit);
      return { items: hit.data, cached: true };
    }
    ctrl?.abort();
    ctrl = new AbortController();
    const my = ++seq;
    try {
      const res = await api.get('/suggest', { params: { q }, signal: ctrl.signal });
      if (my !== seq) return null;                     // 竞态守卫
      cache.set(q, { data: res.items, ts: Date.now() });
      if (cache.size > cap) cache.delete(cache.keys().next().value);   // LRU 淘汰
      return { items: res.items };
    } catch (e) {
      if (e.name === 'AbortError') return null;        // 被新输入取消：正常
      throw e;
    }
  }
  function onCompositionEnd() {                        // IME 上屏立即触发（跳过防抖）
    return fire(currentQuery());
  }
  return { onInput, onCompositionEnd, markComposing: (v) => { composing = v; } };
}
```

**评分点**:
- 四机制完整集成且互不干扰（防抖/seq/缓存/IME）。
- LRU touch 语义 + cap 淘汰正确。
- IME 上屏后跳过防抖立即请求（体验细节）。
- abort 与 seq 双保险（乱序响应兜底）。
