---
title: [NODE-640] Node 服务的缓存层次（内存/Redis）怎么设计？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-640：缓存层次怎么设计？
**答**：
- 两级缓存：进程内存 LRU（微秒级、不跨实例、容量小）→ Redis（毫秒级、跨实例共享、容量大）→ 源（DB/下游）——读路径逐层回源。
- 一致性策略：写路径「先写源 + 删缓存」（cache-aside）优于「更新缓存」（并发写竞态）；内存级缓存短 TTL（秒级）容忍陈旧——两级 TTL 分层（内存 5s / Redis 5min）让不一致窗口可控。
- 击穿/穿透/雪崩：热 key 过期击穿 → 单飞重建（per-key 锁，SCN-BLD-304 单飞同构）；空值穿透 → 空值短缓存；同时过期雪崩 → TTL 加随机抖动。
- 内存缓存纪律：容量上限 + 淘汰策略（LRU）、大对象不进进程内存（Buffer 泄漏——SCN-NODE-635 堆外）、进程重启即失效（可接受——它是加速层不是存储层）。
- 追问钩子：为什么内存级缓存 TTL 要「短到能容忍陈旧」而 Redis 可以更长——进程内存缓存不可主动失效（跨实例无广播时），TTL 是唯一一致性手段——TTL = 可容忍的不一致窗口；Redis 有 pub/sub 失效广播能力，可以主动失效所以 TTL 可以长——「失效能力决定 TTL 策略」。

```javascript
const mem = new LRUCache({ max: 5000, ttl: 5_000 });  // L1：5s
async function get(key) {
  const l1 = mem.get(key); if (l1) return l1;
  const l2 = await redis.get(key); if (l2) { mem.set(key, l2); return l2; }
  const fresh = await loadSource(key);
  await redis.set(key, fresh, 'EX', 300 + jitter(60)); // L2：5min + 抖动防雪崩
  mem.set(key, fresh);
  return fresh;
}
```
