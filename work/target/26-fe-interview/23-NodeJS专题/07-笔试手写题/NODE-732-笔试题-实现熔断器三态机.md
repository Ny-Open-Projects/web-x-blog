---
title: [NODE-732] 笔试题——实现熔断器三态机（滑动窗口 + 半开探测）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-732：手写熔断器

**需求与边界**：
- 需求：三态熔断器（SCN-NODE-669）——① 滑动窗口失败率统计（含慢调用计入失败——慢也算）；② 最小样本（样本少不熔断）；③ half-open 并发探测（2 个试探请求）；④ fallback 集成 + 事件（状态变迁告警——SCN-OPS-276 纪律）。
- 边界：① 滑动窗口实现（环形桶按时间衰减——非全量计数）；② half-open 期间新请求拒绝（只有探测通过——不风暴）；③ 状态变迁持久（进程重启保留——Redis 状态，可选）。

**答**：
```javascript
class CircuitBreaker {
  constructor(fn, { threshold = 0.5, minSamples = 20, halfOpenMax = 2, slowMs = 3000 } = {}) {
    this.fn = fn; this.state = 'closed'; this.buckets = new Map();   // 桶：时间片 → {ok, fail, slow}
  }
  async call(...args) {
    if (this.state === 'open') throw new CircuitOpen();      // 快速失败（fallback 由调用方配）
    if (this.state === 'half-open' && this.probing >= this.halfOpenMax)
      throw new CircuitOpen();                         // half-open 并发限制
    this.probing = this.state === 'half-open' ? this.probing + 1 : 0;
    const start = Date.now();
    try {
      const r = await this.fn(...args);
      if (Date.now() - start > this.slowMs) this.record('slow');   // 慢也算失败
      else this.record('ok');
      this.maybeTrip();
      return r;
    } catch (e) { this.record('fail'); this.maybeTrip(); throw e; }
    finally { if (this.state === 'half-open') this.probing--; }
  }
  maybeTrip() {
    const { total, fail, slow } = windowStats(this.buckets, 10_000);
    if (total < this.minSamples) return;               // 样本少不熔断
    const failRate = (fail + slow) / total;
    if (failRate > this.threshold && this.state === 'closed') {
      this.state = 'open'; emit('open');
      setTimeout(() => { this.state = 'half-open'; this.probing = 0; }, this.openMs);   // 试探窗口
    } else if (this.state === 'half-open' && failRate <= this.threshold) {
      this.state = 'closed'; emit('closed');           // 探测通过恢复
    }
  }
}
```

**评分点**:
- 滑动窗口桶统计（时间片衰减——非全量计数）。
- 慢调用计入失败（slowMs——慢=失败语义）。
- 最小样本 + half-open 并发探测限制（恢复验证不风暴——SCN-NODE-669）。
- 状态变迁事件（可观测——降级联动 SCN-NODE-690）。
