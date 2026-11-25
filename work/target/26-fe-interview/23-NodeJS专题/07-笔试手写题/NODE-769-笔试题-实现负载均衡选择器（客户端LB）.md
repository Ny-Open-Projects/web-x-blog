---
title: [NODE-769] 笔试题——实现客户端负载均衡器（健康感知 + 平滑轮询）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-769：手写客户端 LB

**需求与边界**：
- 需求：客户端 LB（SCN-NODE-703）——① 实例列表动态更新（watch——SCN-NODE-703）；② 健康感知摘流（实例错误率——SCN-NODE-706 粒度）；③ 平滑加权轮询（权重分布平滑——不突发）；④ 连接级与请求级模式（长连接场景——SCN-NODE-703）。
- 边界：① 摘流的恢复探测（半开——SCN-NODE-669）；② 全摘兜底（全部不健康回退任一——保底）；③ LB 状态持久（重启不重置学习到的健康状态——可选）。

**答**：
```javascript
class ClientLB {
  constructor(instances, { errorThreshold = 0.5 } = {}) {
    this.set(instances);
    discovery.watch('order-svc', (list) => this.set(list));   // 动态更新（SCN-NODE-703）
  }
  pick() {
    const healthy = this.instances.filter(i => i.errRate < this.errorThreshold);
    const pool = healthy.length ? healthy : this.instances;   // 全摘兜底（SCN-NODE-706）
    return smoothWeightedRoundRobin(pool);             // 平滑加权（Nginx 算法）
  }
  report(instance, ok) {                               // 请求结果反馈（健康学习）
    instance.stats.push(ok);
    instance.errRate = windowErrorRate(instance.stats);
    if (instance.errRate >= this.errorThreshold) probeHalfOpen(instance);   // 半开探测
  }
}
// 平滑加权轮询：每实例 currentWeight += weight，选最大者后减 totalWeight
function smoothWeightedRoundRobin(pool) {
  let best = null;
  pool.forEach(i => { i.cw += i.weight; if (!best || i.cw > best.cw) best = i; });
  best.cw -= pool.reduce((s, i) => s + i.weight, 0);
  return best;
}
```

**评分点**:
- 动态实例列表（discovery watch——SCN-NODE-703）。
- 健康感知摘流 + 半开探测（SCN-NODE-669/706 粒度）。
- 平滑加权轮询（Nginx 算法——权重不突发）。
- 全摘兜底（保底——SCN-NODE-706）。
