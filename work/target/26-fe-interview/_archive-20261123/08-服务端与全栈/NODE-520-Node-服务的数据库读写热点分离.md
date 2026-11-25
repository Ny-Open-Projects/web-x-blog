---
title: [NODE-520] Node 服务的读写热点分离（高频读路径专用化）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-520：读写热点分离
**答**:
- 场景：高频读（商品详情 10w QPS）与低频写（编辑 10 QPS）同表——读热点把 DB 打满拖累写。分离策略：读路径完全缓存化（详情页缓存为主 DB 只做回源——ARC-438 热点预案）、读写副本分离（NODE-385）+ 读投影宽表（NODE-486 CQRS-lite）。
- 热点读专用化：详情接口的专用读模型（宽表/缓存快照——查询简单化：单 key 取回不做 join）、读路径禁止重查询（分页 join/聚合——进读模型预计算）。
- 写路径保护：写库连接池独立配额（读回源打不进写池——资源隔离 ARC-418）、写峰值保护（大促改价等写操作限流——读优先保命）。
- 一致性管理：读模型的更新延迟可接受度（详情页价格延迟 5s 可接受 → 缓存 TTL 5s + 失效广播 NODE-507）、关键读（下单时价格）不读热点缓存（走强一致通道——读下单专用接口直查）。
- 验证：读写隔离压测（读 10w QPS 时写 P99 无劣化——分离有效性证明）。
```javascript
// 读写路径分离
async function getDetail(id) { return detailCache.get(id) ?? rebuild(id); }   // 读：缓存化
async function placeOrder(cmd) { return writePool.tx(t => orderTx(t, cmd)); } // 写：独立池
// 下单价格校验走强一致：const price = await strongRead(skuId)  // 不读热点缓存
```
