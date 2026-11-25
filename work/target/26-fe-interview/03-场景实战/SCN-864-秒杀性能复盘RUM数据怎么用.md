---
title: [SCN-864] 秒杀性能复盘（RUM 数据怎么读）怎么做的？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-864：性能复盘怎么读 RUM？
**答**：
- 关键切片：按「活动时段 vs 日常」对比（峰值负载下的真实体验）、按机型分层（低端机在峰值下是否崩）、按网络分层（弱网用户流失点）。
- 核心指标归因：秒杀页 TTI 超标 → 拆资源（图片/JS/接口排队）；点击到反馈超 1s → 接口限流排队（体验已由排队页承接）。
- 帧率与卡顿：峰值期长任务统计（JS 计算阻塞——倒计时/库存渲染），定位后进下轮优化。
- 复盘输出：性能劣化清单 → 与上一场活动基线对比（防劣化递进）→ 改进项带目标值（如秒杀页 TTI P95 从 4s 降到 2.5s）。
- 追问钩子：为什么按活动时段对比而不看全天平均——秒杀体验由峰值 10 分钟决定，全天平均被非活动时段稀释；峰值切片才反映真实战场。

```javascript
function perfReview(rum) {
  const peak = rum.sliceBy(activityWindow), daily = rum.sliceBy(normalWindow);
  return {
    ttiDelta: peak.tti.p95 - daily.tti.p95,
    byDevice: layerBy(peak, 'deviceTier'),            // 低端机是否崩
    longTasks: peak.longTasks.top10(),
    action: peak.tti.p95 > 3000 && {
      item: 'seckill-tti', owner: 'perf-team',
      from: peak.tti.p95, to: 2500 },                 // 带目标值的改进项
  };
}
```
