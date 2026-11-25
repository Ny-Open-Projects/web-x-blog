---
title: [NODE-472] Node 服务的过载保护（load shedding）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-472：过载保护与负载卸载
**答**:
- 过载信号：事件循环延迟 P99 持续高（NODE-350）、队列堆积（连接池等待）、CPU 饱和——过载时正确做法是"少接活"（load shedding）而不是"硬扛"（扛住 = 全部变慢，雪崩更快）。
- 卸载策略：过载时按优先级卸载（核心/重要/边缘分级 NODE-418：先拒边缘流量，429 + Retry-After）、准入控制（并发信号量：在途请求超阈值直接拒绝新请求——fast fail 优于排队超时）、随机早丢（队列中随机丢一部分——公平且避免羊群效应同步超时）。
- 自适应：基于延时的准入控制（aimd：成功率高加并发、失败减——自适应探容量，避免静态阈值不准）；与上游配合：过载响应带 Retry-After 让上游退避（NODE-471）。
- 恢复期保护：过载恢复期不立即全开（恢复期限流爬坡——防恢复瞬间请求洪峰再次过载）。
- 演练：过载演练（压到过载点验证：卸载的是边缘、核心存活、恢复爬坡正常，NODE-408）。
```javascript
// 自适应准入（AIMD）
const admission = { limit: 100, inflight: 0 };
function tryAcquire() {
  if (admission.inflight >= admission.limit) return null;         // 拒绝 → 429 + Retry-After
  admission.inflight++;
  return () => { admission.inflight--;
    if (latency.ok()) admission.limit = Math.min(MAX, admission.limit + 1); // 加
    else admission.limit = Math.max(MIN, admission.limit >> 1);              // 减半
  };
}
```
