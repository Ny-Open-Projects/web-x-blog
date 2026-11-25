---
title: [NODE-522] Node 服务的网关熔断与舱壁隔离如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-522：网关熔断与舱壁隔离
**答**:
- 熔断器三态：closed（正常放行+统计）→ open（错误率/慢调用率超阈值——快速失败不再打下游）→ half-open（试探流量恢复探测）。参数：滑动窗口统计、错误率阈值、最小请求数（低流量不误熔断）、half-open 并发探测数。
- 舱壁隔离（bulkhead）：按下游隔离资源（每个下游独立并发上限——下游 A 挂不占 B 的并发额度；实现：per-dependency 信号量/连接池隔离 NODE-473）、按重要性隔离（核心/边缘独立资源池 NODE-418）。
- 网关层熔断语义：open 时返回降级响应（静态兜底/缓存数据——不是裸 503）、熔断事件广播（降级生效通知——观测与自动止损 ARC-446 联动）、half-open 恢复确认（连续 N 次成功才 closed——防抖）。
- 与重试协同：熔断打开期间重试直接跳过（NODE-471 重试预算联动——不浪费重试在必失败的调用上）。
- 观测：熔断器状态时间线（何时 open/half-open/closed——降级决策的依据）、按下游的熔断统计、误熔断率（下游健康但被熔——阈值调优依据）。
```javascript
class Breaker {
  async call(fn) {
    if (this.state === 'open') throw new CircuitOpen(this.name);  // 快速失败 → 降级
    try { const r = await fn(); this.onSuccess(); return r; }
    catch (e) { this.onFailure(e); throw e; }
  }
  onFailure() { if (++this.fails / this.counts.total > 0.5 && this.counts.total > 20)
    { this.state = 'open'; scheduleProbe(30e3); broadcast('open', this.name); } }
}
// bulkhead：per-dep semaphore——dep-a 挂满不占 dep-b 额度
```
