---
title: [HW-189] 手写路由数据预取——hover/触摸触发 prefetch + 去重 + TTL 缓存与命中率上报
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-189：手写路由数据预取——hover/触摸触发 prefetch + 去重 + TTL 缓存与命中率上报
**答**：路由数据预取的完整工程化：触发（hover 100ms 阈值防误滑 + touchstart 触摸设备）→ 去重（在途 Map 共享 Promise）→ TTL 缓存（预取数据 30s 有效，过期即弃）→ 命中率上报（X-Prefetch 标记，PER-391）→ 弱网/saveData 禁用。

```javascript
class RoutePrefetcher {
  #cache = new Map();                                     // url -> { promise, at }
  #inflight = new Set();
  constructor({ ttl = 30000, hoverDelay = 100 } = {}) { Object.assign(this, { ttl, hoverDelay }); }
  attach(links) {
    for (const a of links) {
      let timer = null;
      const url = a.href;
      const go = () => {
        if (this.#shouldSkip()) return;
        this.#prefetch(url);
      };
      a.addEventListener('mouseenter', () => { timer = setTimeout(go, this.hoverDelay); });   // 100ms 防误滑
      a.addEventListener('mouseleave', () => clearTimeout(timer));
      a.addEventListener('touchstart', go, { passive: true });   // 触摸设备无 hover：立即预取
    }
  }
  #shouldSkip() {
    return navigator.connection?.saveData || networkTier() === 'slow' || this.#inflight.size >= 2;
  }
  #prefetch(url) {
    if (this.#cache.has(url)) return;                     // 已缓存/在途：共享
    this.#inflight.add(url);
    const promise = fetch(url, { headers: { 'X-Prefetch': '1' } })
      .then((r) => r.json())
      .then((data) => { this.#cache.set(url, { data, at: Date.now() }); return data; })
      .finally(() => this.#inflight.delete(url));
    this.#cache.set(url, { promise, at: Date.now() });    // 在途 Promise 缓存（HW-088 语义）
  }
  async get(url) {                                        // 路由组件取数：命中秒回，未命中现场拉
    const hit = this.#cache.get(url);
    if (hit?.data && Date.now() - hit.at < this.ttl) { trackPrefetchHit(url, true); return hit.data; }
    const data = await (hit?.promise ?? fetch(url).then((r) => r.json()));
    trackPrefetchHit(url, !!hit?.data);
    return data;
  }
}
// 命中率上报：X-Prefetch 请求 5min 内被真实使用 → 命中；< 50% 命中率的预取策略下线（PER-391）
// TTL 30s：过期即弃（陈旧预取数据比无数据危险——用户看到 5 分钟前的列表还以为是最新的）
```

**评分点**：
- hover 100ms 阈值 + touchstart 触摸设备双触发。
- 在途 Promise 缓存去重（HW-088 语义）+ TTL 过期即弃。
- 弱网/saveData/并发上限三重禁用条件。
- 命中率上报闭环（PER-391）——本题核心。
