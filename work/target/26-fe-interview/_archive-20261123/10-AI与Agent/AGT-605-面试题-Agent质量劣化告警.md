---
title: [AGT-605] 模型输出质量突然变差（上游模型悄悄升级/提示词回归），可观测体系如何第一时间发现？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-605：模型输出质量突然变差（上游模型悄悄升级/提示词回归），可观测体系如何第一时间发现

**答**：
- 质量代理指标先行（可实时算的）：负反馈率、重新生成率、引用命中率、工具调用失败率、平均轮次变长——任一指标 burn rate 超阈值即告警，不必等人工评测。
- 基线锚定：每次模型版本/提示词版本变更记录指纹，指标按版本分组对比；「同版本内漂移」说明上游悄悄变了（调价/升级），告警归因到版本。
- 告警降噪：多指标联合判定（单指标波动不告警，2+ 指标同向劣化才告警），并附自动下钻链接（topN 劣化样本）。

```javascript
const QUALITY_SIGNALS = ['dislikeRate', 'regenRate', 'citeHitRate', 'toolFailRate'];
function checkDegradation(window) {
  const bad = QUALITY_SIGNALS.filter(sig =>
    burnRate(window[sig], baseline[sig]) > 2);    // 2倍burn rate
  if (bad.length >= 2) {                           // 联合判定降噪
    alert({ type: 'quality_degrade', signals: bad,
      drilldown: topNSamples(window, bad),         // 自动下钻样本
      verFingerprint: currentVersionFP });
  }
}
```

