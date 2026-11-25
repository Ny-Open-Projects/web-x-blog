---
title: [NODE-834] 笔试题——实现容量弹性伸缩控制器（HPA 增强版）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-834：手写弹性伸缩

**需求与边界**：
- 需求：弹性伸缩控制器（SCN-NODE-699/665）——① 多指标伸缩（QPS/事件循环延迟/CPU——Node 特有指标，SCN-NODE-721 ELD）；② 预扩容（定时/事件驱动——大促 warm-up，SCN-NODE-699）；③ 伸缩与下游联动（扩容后下游容量校验——SCN-NODE-699 全局）；④ 伸缩风暴防御（缩容冷却期——抖动防御）。
- 边界：① ELD 作为伸缩指标（事件循环延迟——CPU 之外的 Node 真实信号，SCN-NODE-721）；② 缩容的冷却期（5 分钟——SCN-OPS-237 抖动防御同源）；③ 扩容上限与下游对齐（SCN-NODE-699）。

**答**：
```javascript
class ElasticController {
  async tick() {
    const { qps, eldP99, cpu } = await currentLoad();
    const pressure = Math.max(qps / targetQps, eldP99 / 100, cpu / 0.7);   // 多指标取最大（SCN-NODE-721）
    const desired = Math.ceil(instances * pressure);
    const capped = Math.min(desired, downstreamSafeMax());   // 下游对齐（SCN-NODE-699）
    if (capped > instances) scaleUp(capped);           // 扩容（含 warm-up——SCN-NODE-699 预扩容）
    else if (capped < instances && coolingDown() === false) {
      scaleDown(capped);                               // 缩容冷却期（SCN-OPS-237 抖动防御）
      setCooldown(5 * 60_000);
    }
  }
}
// 预扩容（定时/事件）
cron('0 18 * * *', () => scaleUp({ to: preSaleInstances }));   // 大促 warm-up（SCN-NODE-699）
```

**评分点**:
- 多指标伸缩（QPS/ELD/CPU 取最大——SCN-NODE-721 ELD Node 特有）。
- 下游对齐上限（SCN-NODE-699 全局校验）。
- 缩容冷却期（抖动防御——SCN-OPS-237）。
- 预扩容事件驱动（warm-up——SCN-NODE-699）。
