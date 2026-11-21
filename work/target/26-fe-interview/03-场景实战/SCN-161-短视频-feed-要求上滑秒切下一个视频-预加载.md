---
title: [SCN-161] 短视频 feed 要求上滑秒切下一个视频，预加载策略怎么设计？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-161：短视频 feed 要求上滑秒切下一个视频，预加载策略怎么设计？
**答**：
- 预加载分三档：当前视频完整播放、下一个视频预取元数据与首段（Range 请求前 1~2MB）、下下个仅预解析 id。带宽是零和的，预取过多反而挤占当前播放。
- 滑动意图预判：用户手指上滑超过 30% 屏高或速度超阈值，立即把"下一个"升级为完整预加载；滑回则取消。
- MSE 场景把预取的分片直接喂给下一个播放器实例（预建 player），切换时几乎零等待；src 直连场景用 `video.preload='auto'` 的隐藏实例。
- 全局并发与流量控制：预取队列并发 1，弱网（navigator.connection）下调预取档位。

```javascript
// 短视频预加载：三档策略 + 滑动意图升级 + 弱网降级
const LEVELS = { CURRENT: 2, NEXT_META: 1, NONE: 0 };

export class ShortVideoPreloader {
  cache = new Map();                                   // id -> mediaSource/segments
  constructor(feed) {
    this.feed = feed;
    this.bandwidth = navigator.connection?.effectiveType ?? '4g';
  }
  levelFor(index) {
    if (index === this.feed.current) return LEVELS.CURRENT;
    if (index === this.feed.current + 1) {
      // 弱网只预 metadata，好网络预取首段
      return ['slow-2g', '2g'].includes(this.bandwidth) ? LEVELS.NEXT_META : LEVELS.CURRENT;
    }
    return LEVELS.NONE;
  }
  sync() {
    for (let i = this.feed.current - 1; i <= this.feed.current + 2; i++) {
      const item = this.feed.get(i);
      if (!item) continue;
      const level = this.levelFor(i);
      if (level === LEVELS.CURRENT && !this.cache.has(item.id)) this.prefetch(item);
      if (level === LEVELS.NEXT_META) this.prefetchMeta(item);
    }
  }
  async prefetch(item) {
    if (this.inflight) return;                         // 全局并发 1：不挤占当前播放带宽
    this.inflight = true;
    try {
      // Range 请求只拉首段，MSE 交给预建 player
      const head = await fetch(item.url, { headers: { Range: 'bytes=0-1572864' } }); // 前 1.5MB
      this.cache.set(item.id, await head.arrayBuffer());
    } finally { this.inflight = false; }
  }
  prefetchMeta(item) {
    const v = document.createElement('video');
    v.preload = 'metadata';
    v.src = item.url;
    v.load();
    this.cache.set(`meta:${item.id}`, v);
  }
  // 滑动意图：上滑速度超阈值立即升级预取
  onDrag(dy, velocity) {
    if (dy < -screen.height * 0.3 || velocity > 1.2) {
      const next = this.feed.get(this.feed.current + 1);
      next && !this.cache.has(next.id) && this.prefetch(next);
    }
  }
}
```
