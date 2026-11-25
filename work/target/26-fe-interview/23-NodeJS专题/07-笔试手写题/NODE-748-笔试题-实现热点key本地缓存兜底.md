---
title: [NODE-748] 笔试题——实现热点 key 本地缓存兜底（打散 + L1）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-748：手写热点兜底

**需求与边界**：
- 需求：热点 key 兜底（SCN-NODE-689）——① 本地 L1 兜底（热点 key 进 L1——Redis 分片压力转移）；② key 打散（写时 N 份、读随机——单分片压力 ÷N）；③ 热点自动识别（QPS 采样——超阈值 key 进 L1）；④ L1 失效广播（SCN-NODE-727）。
- 边界：① 热点识别的滑动窗口（近 10s QPS 超阈值——即时性）；② 打散的读一致性（写全写——短暂不一致窗口容忍）；③ L1 容量（热点数量有限——LRU 上限可控）。

**答**：
```javascript
class HotKeyShield {
  constructor({ n = 10, hotThreshold = 1000 } = {}) { this.n = n; this.qps = new Map(); }
  async get(key, loader) {
    if (this.trackHot(key)) {                          // 热点自动识别（滑窗 QPS）
      const l1 = this.l1.get(key);
      if (l1 !== undefined) return l1;                 // L1 兜底（Redis 压力转移）
      const v = await loader(key);
      this.l1.set(key, v, { ttl: 2000 });              // L1 短 TTL（2s——一致性窗口）
      return v;
    }
    const shard = Math.floor(Math.random() * this.n);  // 打散读
    return redis.get(`k:${key}:${shard}`);
  }
  async set(key, value) {
    await Promise.all(Array(this.n).fill(0).map((_, s) =>
      redis.set(`k:${key}:${s}`, value)));             // 写全写（打散一致性）
    this.broadcastInvalid(key);                        // L1 失效广播（SCN-NODE-727）
  }
  trackHot(key) {                                      // 滑窗 QPS 识别
    const c = (this.qps.get(key) ?? 0) + 1; this.qps.set(key, c);
    return c > this.hotThreshold;                      // 超阈值 → 自动进 L1
  }
}
```

**评分点**:
- 热点自动识别（滑窗 QPS 超阈值——不靠人工报热点）。
- L1 短 TTL 兜底（2s 一致性窗口——SCN-NODE-640 分层 TTL 语义）。
- 打散读写（写全写——单分片压力 ÷N）。
- L1 失效广播（SCN-NODE-727 pub/sub 联动）。
