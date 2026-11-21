---
title: [NODE-459] Node 服务多活的数据同步与冲突处理如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-459：多活数据同步与冲突
**答**:
- 多活分层：单元化（set 化：用户归属单元，同用户请求固定单元——数据不跨单元写，无冲突最简）、全局强一致数据（库存/账户）跨单元同步（冲突不可避免）。
- 同步机制：异步复制（DTS/自研 binlog 同步，最终一致，延迟监控 ARC-459 前端配合）、冲突处理策略（版本号最后写入胜 / 业务合并 / 冲突进人工队列）。
- 关键设计：单元归属路由（网关按 uid 路由到归属单元——防止跨单元写导致冲突源头）、全局数据的单元亲和（库存按单元分片预分配——扣各自配额，冲突最小化 ARC-384 分片思想）。
- 容灾切换：单元故障 → 切流（流量切到备单元，数据差异补偿：切流前 diff 补偿同步 NODE-437 对账）、切换演练（ARC-459）。
- 一致性验证：跨单元数据抽检（定时 diff 两侧数据，不一致告警）——同步链路的健康监控。
```javascript
// 单元路由 + 全局分片
function routeUnit(uid) { return unitOf(hash(uid) % UNITS); }    // 用户固定单元
// 全局库存：unitStock[uid] = totalStock * share[unit]             // 预分配配额
async function decStock(uid, qty) {
  const u = routeUnit(uid);
  if (!await luaDecr(`stock:${u}`, qty))                          // 本单元配额不足
    return borrowFromNeighbor(u, qty) ?? reject();               // 借邻单元配额（预分配兜底）
}
```
