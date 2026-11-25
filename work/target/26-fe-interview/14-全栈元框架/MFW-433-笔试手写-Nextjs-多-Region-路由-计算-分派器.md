---
title: [MFM-433→MFW→MFW-433] 笔试：手写多 Region 计算/数据分派器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-433：Region 分派
**答**：实现 `regionDispatch(req, { topology, { dataHomes: { orders: 'us-east', users: 'eu' } } })`：1) 判定函数：路由的数据归属（蓝图 deps 表→主 region）vs 用户接入点（geo header）→ 计算 region = argmin(数据RTT + 用户延迟)（读写分离：读可副本就近，写必主）；2) 输出 { computeRegion, dataMode: 'local'|'remote', proxyTo? }——边缘函数按此转发或本地执行；3) 缓存 key 含 computeRegion（同路由不同区渲染产物不互串——时区/合规差异）；4) 故障转移：主 region 不可用→读降级副本+写排队（MFW-496 语义复用）；5) 度量：跨区调用占比（应 <15%——架构漂移信号）。

```javascript
export function dispatch(req, { blue, health }) {
  const { userR, home } = geoOf(req)
  const needs = blue[routeOf(req)].tables
  const primary = dominant (needs.map((t) => home[t]))      // 多数数据所在区
  if (isRead (req) && replicas [primary]?.includes(userR) && freshEnough)
      return { compute: userR, mode: 'local-replica' }      // 读就近副本
  if (health[primary] !== 'up') return degradePlan(op, { queue: isWrite})   // 写排队读降级
  return { compute: primary, mode: 'remote', proxyFrom: userR }   // 写/无副本→就数据
}
// key: `${renderKey}+@${computeRegion}`；跨区率 >15% → 架构评审触发
```
**评分点**：
- 读写分派不同（读副本就近/写必主——一致性优先于延迟的明确序）
- 计算region=数据 argmin（计算就数据 MFW-311 公式化）
- 键含 region（时区合规渲染差异不互串）
- 跨区率阈值（架构漂移的可量化警戒线）
