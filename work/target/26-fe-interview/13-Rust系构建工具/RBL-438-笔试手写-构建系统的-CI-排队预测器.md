---
title: [RBL-438] 笔试：手写 CI 排队时间预测器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-438：手写 CI 排队时间预测器
**需求**：实现 `predictQueueTime({ queueDepth, runningJobs, avgDuration, runnerCount })`：1) 模型：排队时间 ≈（queueDepth 中能并行启动的部分 + 正在跑任务的剩余时间期望）× 任务时长 / 可用 runner；2) 输出期望值与 P90（历史排队时长分布分位叠加）；3) 用途：提交前提示「预计等待 X 分钟」（开发者可错峰）与「是否值得优化排队」（排队占比高 → 扩容优先）；4) 历史数据采样：按 hour-of-day 分桶（早高峰与深夜排队差异大——统一平均会失真）；5) 预测校准：预测 vs 实际偏差跟踪（漂移告警）。

```javascript
export function createQueuePredictor(history) {
  function bucketOf(ts) { return new Date(ts).getHours() }       // hour-of-day 分桶

  function bucketStats(hour) {
    const samples = history.filter((h) => bucketOf(h.at) === hour)
    if (!samples.length) return null
    const sorted = samples.map((s) => s.queueMs).sort((a, b) => a - b)
    return { p50: sorted[Math.floor(sorted.length / 2)], p90: sorted[Math.floor(sorted.length * 0.9)] }
  }

  function predict({ queueDepth, runningJobs, avgDuration, runnerCount, now = Date.now() }) {
    const free = Math.max(0, runnerCount - runningJobs)
    const startWave = Math.min(queueDepth, free)                 // 立即启动的
    const waves = Math.ceil((queueDepth - startWave) / runnerCount)
    const mathMs = (waves * avgDuration)
    const stats = bucketStats(new Date(now).getHours()) ?? bucketStats(12) ?? { p50: mathMs, p90: mathMs * 1.5 }
    // 混合：模型值与历史分位加权
    const expected = Math.round(mathMs * 0.4 + stats.p50 * 0.6)
    return { expectedMs: expected, p90Ms: stats.p90, driver: waves > 0 ? 'queue-depth' : 'historical' }
  }

  function calibrate(predictions /* [{predicted, actual}] */) {
    const errors = predictions.map((p) => Math.abs(p.predicted - p.actual) / Math.max(p.actual, 1))
    const mape = errors.reduce((a, b) => a + b, 0) / errors.length
    return { mape: +mape.toFixed(3), reliable: mape < 0.3 }      // MAPE < 30% 可信
  }

  return { predict, calibrate, bucketStats }
}
```
**评分点**：
- 分桶建模（hour-of-day——排队高度依赖时段，统一平均失真）
- 模型 + 历史混合（纯模型无波动语义，纯历史无结构信息）
- 校准闭环（MAPE 追踪预测可信度——预测器要自证准确）
- 用途输出（错峰提示/扩容归因——预测要可行动）
