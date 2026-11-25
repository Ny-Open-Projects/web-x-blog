---
title: [SCN-723] SLA 看板的异常检测（自动发现劣化）怎么辅助值班？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-723：看板异常检测怎么辅助？
**答**：
- 三类检测：突增（STL 分解残差超 3σ）、缓变（7 天滑动基线回归斜率超阈值）、周期异常（同比同时刻偏离）——不同劣化形态不同检测器。
- 辅助而非替代：异常检测产出「建议关注」标注在看板（黄色标记），不直接告警（告警仍走 burn rate 规则）——避免检测误报污染值班信噪比。
- 基线学习：基线按「同时段历史」计算（周周期性），排除已知事件时段（大促/故障）学习，防污染。
- 反馈闭环：值班对每个标注点标记「有效/误报」，误报率高的检测器自动调参或下线。
- 追问钩子：为什么不直接用异常检测驱动告警——异常检测召回高精度低，告警要求精度优先；两者结合（检测提供线索、规则触发行动）才是成熟形态。

```javascript
function anomalyMark(series) {
  const baseline = seasonalBaseline(series, { period: 'week', exclude: EVENTS });
  const residual = series.map((p, i) => p.v - baseline[i].v);
  const std = stdOf(residual.filter((_, i) => !EVENTS.has(series[i].t)));
  return series.map((p, i) => ({
    ...p, anomaly: Math.abs(residual[i]) > 3 * std,
    kind: residual[i] > 3 * std ? 'spike' : Math.abs(residual[i]) > 1.5 * std && trending(residual, i) ? 'drift' : null,
  }));
}
// 值班反馈
board.on('mark-feedback', ({ t, useful }) => detector.adjust(useful ? 1 : -1));
```
