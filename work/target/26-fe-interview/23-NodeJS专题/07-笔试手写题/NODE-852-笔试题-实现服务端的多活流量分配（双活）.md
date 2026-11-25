---
title: [NODE-852] 笔试题——实现多活流量分配（双活/单元化路由）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 面试题
---

## NODE-852：手写多活路由

**需求与边界**：
- 需求：多活路由（SCN-OPS-195 双活）——① 单元化路由（按用户归属单元——数据一致性，单元化 SCN-NODE-678）；② 流量分配（单元亲和——用户固定单元，SCN-OPS-195）；③ 故障切换（单元挂——流量切到备用单元 + 数据同步校验）；④ 切换的数据一致性（切单元后数据写入——跨单元同步语义）。
- 边界：① 单元路由键（userId hash——SCN-NODE-657 分布式 ID 基因联动）；② 切流的灰度（按百分比切——SCN-OPS-237 降档语义）；③ 切流后的数据校验（对账——SCN-NODE-682）。

**答**：
```javascript
function unitRoute(user) {
  const unit = unitOf(user);                           // 用户归属单元（基因/hash——SCN-NODE-657）
  const active = unitHealth[unit] ? unit : failoverUnit(unit);   // 故障切换
  return { unit: active, region: UNIT_REGION[active] };
}
// 故障切换（灰度切流——SCN-OPS-237）
async function failoverUnit(unit) {
  const target = UNIT_BACKUP[unit];
  for (const pct of [10, 50, 100]) {                   // 灰度切流（SCN-OPS-237）
    await shiftTraffic(unit, target, pct);
    await verifyDataSync(target, pct);                 // 数据同步校验（SCN-NODE-682 对账）
  }
  return target;
}
```

**评分点**:
- 单元化路由（用户归属——SCN-OPS-195/678）。
- 故障切换灰度 + 数据同步校验（SCN-OPS-237/682）。
- 单元亲和（数据一致性——SCN-NODE-654 读己之写单元化）。
- failover 的路由键工程化（基因——SCN-NODE-657）。
