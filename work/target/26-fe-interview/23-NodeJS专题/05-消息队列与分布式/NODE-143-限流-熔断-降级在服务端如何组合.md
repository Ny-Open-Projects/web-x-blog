---
title: [NODE-143] 限流、熔断、降级在服务端如何组合？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-143：限流、熔断、降级在服务端如何组合？
**答**：
- 分工：**限流挡量**（保护自己不被压垮）、**熔断止损**（下游病了快速失败防雪崩）、**降级兜底**（返回旧缓存/默认值保体验）、**舱壁隔离**（每下游独立连接池，互不拖累）。
- 熔断三态机：closed（正常计数）→ 失败率超阈值 open（直接快速失败）→ 冷却期后 half-open（放探针请求试探恢复）。
- 组合位置：网关限流（NODE-069/132）→ BFF 内熔断器包住每个下游调用 → 失败走 fallback → 每下游独立 agent/池。
- 度量：熔断器状态变化打点告警；fallback 命中率是"降级质量"的核心指标。

```javascript
class CircuitBreaker {
  constructor({ threshold = 5, cooldownMs = 10_000 } = {}) {
    Object.assign(this, { threshold, cooldownMs });
    this.state = 'closed'; this.failures = 0; this.openedAt = 0;
  }
  async exec(fn, fallback) {
    if (this.state === 'open') {
      if (Date.now() - this.openedAt < this.cooldownMs) return fallback?.(); // 快速失败走降级
      this.state = 'half-open';                      // 冷却结束，放探针试探
    }
    try {
      const r = await fn();
      this.state = 'closed'; this.failures = 0;
      return r;
    } catch (e) {
      this.failures++;
      if (this.state === 'half-open' || this.failures >= this.threshold) {
        this.state = 'open'; this.openedAt = Date.now();
        metrics.inc('breaker_open');                 // 状态变化打点告警
      }
      return fallback ? fallback() : Promise.reject(e);
    }
  }
}

const userBreaker = new CircuitBreaker();
const user = await userBreaker.exec(
  () => rpc.getUser(uid),
  () => cachedUser(uid),    // 降级：返回 Redis 旧值
);
// 舱壁：user 与 order 下游各用独立 http.Agent 与连接池，互不抢占（NODE-116/121）
```
