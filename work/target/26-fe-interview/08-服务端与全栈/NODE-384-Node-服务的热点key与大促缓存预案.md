---
title: [NODE-384] Node 服务的热点 key 与大促缓存预案如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-384：热点 key 与大促缓存预案
**答**:
- 热点问题：秒杀单品 QPS 万级全打一个 Redis key（单分片带宽/CPU 瓶颈）+ 过期击穿（NODE-378）。预案三层：本地缓存（L1 秒级 TTL 扛读）、key 分片（key#1~N 份冗余读）、读降级（Redis 挂时读本地兜底或静态快照）。
- 热点发现：访问日志实时统计 top key（分钟级滑动窗口），超阈值自动升热点（拉长 TTL + 加分片）；大促前手动预热点（活动商品清单提前预热与标记）。
- 大促预案清单：预热（活动商品提前全量进缓存与本地）、锁死（TTL 拉长到大促结束，禁用随机淘汰）、写削峰（库存扣减走 Redis 原子 + 异步落库，NODE-345）、限流兜底（超出容量的流量进排队页）。
- 故障演练：Redis 主从切换、缓存全灭（打 DB 的熔断与排队兜底）演练（ARC-426）。
- 恢复：大促后热点解除（TTL 恢复正常）、缓存回温策略。
```javascript
// 热点 key 升级：本地 + 分片
function goodsRead(id) {
  if (isHot(id)) {                                              // 热点标记（发现/预置）
    return localHot.get(id) ?? loadAndShare(id, { shards: 8 }); // L1 兜底 + 分片冗余
  }
  return normalCacheGet(id);
}
// 写分片：stock 拆 stock:0..7 各持 1/8 配额，扣减轮询分片（避免单 key 热点）
```
