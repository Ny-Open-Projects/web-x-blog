---
title: [NODE-526] Node 服务的缓存预热与回温（冷启动/大促/扩容后）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-526：缓存预热与回温
**答**:
- 预热场景：服务冷启动（发布/扩容新实例——缓存全空，回源风暴打 DB NODE-375）、大促前（热点数据提前入缓存 NODE-438）、Redis 故障恢复（全缓存重建风暴）。
- 预热策略：启动预热（实例启动时按热 key 清单拉取——readiness 延迟 ready 接流 NODE-389）、流量爬坡（预热完成前限流部分流量——缓存边建边服务的渐进放开）、定时预热（夜间低峰预跑高频接口——NODE-437 编排）。
- 热 key 清单：预热范围声明（高频接口/热点商品清单——运营配置 + 自动统计 topN NODE-438 热点发现）。
- 回温（故障恢复后）：限流爬坡（恢复期流量逐步放大——缓存边回填边接流量 NODE-472 恢复期保护）、预热完成判定（命中率回基线 → 解除爬坡）。
- 观测：预热耗时/命中率爬坡曲线、预热期间的 DB 回源量（预热不能反过来打挂 DB——预热本身限速）。
```javascript
// 启动预热 + 爬坡
async function warmup() {
  for (const key of await hotKeys()) await cache.rebuild(key, { throttle: 50 }); // 限速回源
  ready = true;                                                  // 预热完才 ready
}
// 扩容实例：readiness 直到 warmup 完成 → LB 缓慢加权（爬坡接流量）
```
