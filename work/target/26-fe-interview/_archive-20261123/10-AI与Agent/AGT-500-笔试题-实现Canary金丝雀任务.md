---
title: [AGT-500] 笔试题——实现 Canary 金丝雀任务（真实流量抽样验证+自动止损）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-500：手写 Canary 机制：真实流量抽样、双跑对比、指标门自动止损

**需求与边界**：
- 输入：新版本执行器、Canary 配置（抽样率/指标门/观察窗口）；输出：Canary 状态机（running/promote/rollback）。
- 边界要求：① 抽样真实流量双跑（影子对比，AGT-442 联动）；② 指标门（质量/成本/延迟三项阈值）连续达标 N 窗口才 promote；③ 任一指标破线→自动 rollback 并告警；④ 观察窗口内人工可强制决策（覆盖自动并留痕）。

**答**：
```javascript
class Canary {
  constructor({ candidate, prod, gates = {
    qualityDelta: -0.02, costDelta: 0.15, latencyDelta: 0.2 },
    stableWindows = 3, sampleRate = 0.2 }) {
    Object.assign(this, { candidate, prod, gates,
      stableWindows, sampleRate });
    this.state = 'running'; this.good = 0; this.bad = 0;
  }
  async onWindow(metrics) {                    // 每观察窗口调用
    if (this.state !== 'running') return this.state;
    // 1. 指标门判定
    const pass = metrics.qualityDelta >= this.gates.qualityDelta &&
      metrics.costDelta <= this.gates.costDelta &&
      metrics.latencyDelta <= this.gates.latencyDelta;
    if (pass) this.good++; else this.bad++;
    // 2. 硬破线自动止损（质量大跌或成本翻倍）
    if (metrics.qualityDelta < this.gates.qualityDelta - 0.05 ||
        metrics.costDelta > this.gates.costDelta * 2) {
      await this.rollback('gate_breach');
      return 'rollback';
    }
    // 3. 连续达标 → 放量；连续不达标 → 回滚
    if (this.good >= this.stableWindows) {
      this.state = 'promote';
      await traffic.set('candidate', 1.0);
      return 'promote';
    }
    if (this.bad >= 2) {
      await this.rollback('unstable');
      return 'rollback';
    }
    return 'running';
  }
  async rollback(reason) {
    this.state = 'rolledback';
    await traffic.set('candidate', 0);          // 流量归零
    await alert({ type: 'canary_rollback', reason,
      stats: { good: this.good, bad: this.bad } });
  }
  // 人工覆盖：观察窗口内强制决策（记录操作者，可审计）
  override(decision, by) {
    archive({ decision, by, state: this.state });
    this.state = decision;
    traffic.set('candidate', decision === 'promote' ? 1.0 : 0);
  }
}
// 与灰度控制器（AGT-418）衔接：Canary 通过 → 交灰度控制器放量；
// 影子对比（AGT-442）提供 metrics 输入。
```

**评分点**:
- 指标门三指标（质量/成本/延迟）+ 硬破线立即回滚（质量大跌或成本翻倍不等窗口）。
- 连续窗口 good/bad 计数判定升档与回滚，防单点波动。
- 人工覆盖强制决策且留痕（自动与人工边界清晰）。
- 与影子对比和灰度控制器衔接（机制组合而非孤立）。
