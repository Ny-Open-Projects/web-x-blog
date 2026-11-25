---
title: [SCN-724] SLA 采集的采样策略与统计还原怎么保证可信？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-724：采样策略与统计还原怎么保证？
**答**：
- 分层采样：正常流量低采样（1%~10%）控成本，降级场景（错误率上升/新版本）自动提采样到 100%——采样率必须随事件记录（还原时按此加权）。
- 有偏防护：均匀随机采样而不是「首 N 条」采样（首 N 有时段偏差）；按用户稳定采样（同用户同采样桶）保证会话完整性分析。
- 还原计算：上报带 sampleRate，统计层按 1/rate 加权还原总量与分位数近似——采样率变化要记录，跨采样率区间不能直接对比。
- 置信度标注：小样本时段（凌晨低流量）分位数置信区间宽，看板显示置信带而非单线。
- 追问钩子：为什么按用户哈希采样——同一用户请求落同一采样决策，才能做「会话级旅程」分析；纯随机采样会切断用户路径。

```javascript
function sampleDecision(userId) {                    // 稳定采样：用户哈希分桶
  const bucket = murmurHash(userId) % 100;
  return { sampled: bucket < SAMPLE_RATE * 100, rate: SAMPLE_RATE, bucket };
}
function upsample(stats, rates) {                    // 按 1/rate 加权还原
  return stats.map(s => ({
    ...s, count: s.count / s.rate,
    p95CI: confidenceInterval(s.p95, s.count),       // 小样本置信带
  }));
}
```
