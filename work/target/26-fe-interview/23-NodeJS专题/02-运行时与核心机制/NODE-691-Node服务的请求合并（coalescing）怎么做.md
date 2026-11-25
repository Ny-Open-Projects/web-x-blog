---
title: [NODE-691] 请求合并（request coalescing）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-691：请求合并怎么做？
**答**：
- 场景：热 key 的并发回源（缓存 miss 瞬间千请求打源——击穿）——合并为一次回源（in-flight 共享 Promise，SCN-FIN-541 单飞）。
- 实现：per-key in-flight map（第一个请求回源，后续请求 await 同一 Promise）——结果回填缓存（SCN-NODE-640 cache-aside 联动）。
- 变体：时间窗合并（短窗口内的请求合并批量——批量 RPC 合并，SCN-NODE-662 Dataloader 同构）；跨实例合并（Redis 锁——单飞跨实例，SCN-NODE-652）。
- 边界：合并的响应语义（同 key 同时刻——数据一致性可接受）；合并窗口内的首错传播（源失败——所有等待者同错，重试风暴防御——退避+抖动）。
- 追问钩子：为什么合并窗口内的「源失败」要带「抖动重试」而不是所有等待者同时重试——源失败时千个等待者同时重试 = 击穿风暴重演；抖动让重试时间分散（0~500ms 随机）——把瞬时并发摊平，源得到喘息窗口——这是合并机制自身的防雪崩配套。

```javascript
const inflight = new Map();
async function coalesce(key, loader) {
  if (inflight.has(key)) return inflight.get(key);     // 共享 in-flight
  const p = loader(key)
    .catch(e => { inflight.delete(key); throw e; })    // 失败清理
    .finally(() => setTimeout(() => inflight.delete(key), 50));   // 短窗口续用
  inflight.set(key, p);
  return p;
}
// 跨实例：Redis 锁单飞
const ok = await redis.set(`fly:${key}`, 1, 'PX', 3000, 'NX');
```
