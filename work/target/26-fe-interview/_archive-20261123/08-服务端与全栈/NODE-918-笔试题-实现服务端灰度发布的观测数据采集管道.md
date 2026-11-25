---
title: [NODE-918] 笔试题——实现灰度观测数据采集管道（版本维度全量采集）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-918：手写观测管道

**需求与边界**：
- 需求：灰度观测管道（SCN-OPS-850/231）——① 版本维度全量采集（指标/日志/trace——SCN-OPS-850 label）；② 采集的分级（canary 全量/stable 采样——SCN-SLA-724）；③ 采集管道的背压（SCN-NODE-636）；④ 采集完整性（SCN-OPS-850 100%）。
- 边界：① canary 全量采集的必要性（灰度判定需要精确数据——SCN-OPS-203）；② 采集管道故障的降级（本地缓冲——SCN-联想-592）；③ 采集的隐私（SCN-NODE-698）。

**答**：
```javascript
function grayObservabilityPipeline(release) {
  const rate = (v) => v === 'canary' ? 1.0 : 0.1;     // canary 全量（SCN-OPS-203）
  return pipeline(
    telemetrySource(rate),
    bufferWithBackpressure({ max: 50_000 }),           // 背压缓冲（SCN-NODE-636）
    enrich({ version: BUILD.commit, gray: bucket }),   // label 注入（SCN-OPS-850）
    sink({ batch: 100 }),
  ).catch(() => localBuffer.persist());                // 管道故障本地缓冲（SCN-联想-592）
}
```

**评分点**:
- canary 全量/stable 采样（SCN-OPS-203）。
- label 注入（版本+灰度桶——SCN-OPS-850/216）。
- 管道背压 + 故障本地缓冲（SCN-NODE-636/联想-592）。
- 隐私（SCN-NODE-698）。
