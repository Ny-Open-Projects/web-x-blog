---
title: [ARC-829] 笔试：手写架构演进 AB 验证
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 笔试题, 迁移]
type: 笔试题
---

## ARC-829：手写演进 AB 验证

**题目**：实现架构演进（新架构 vs 旧架构）的 AB 验证框架 `EvolutionABTest`：① 实验设计：假设声明（「新架构将使交互延迟降低 30%」——可证伪）+ 指标定义（主指标/护栏指标）；② 分流：按用户一致性哈希分 A/B 组（A=旧架构 B=新架构——同用户稳定同组）；③ 护栏监控：B 组的错误率/崩溃率不得高于 A 组 +X%（护栏破 = 立即中止）；④ 主指标判定：实验结束的统计检验（样本量估算前置——最少运行多少天）；⑤ 结论输出：假设验证结果 + 各指标对比表 + 决策建议（全量/回滚/延长）。写出实现。

```javascript
class EvolutionABTest {
  constructor({ hypothesis, primaryMetric, guardrails, minSample }) {
    this.h = hypothesis; this.primary = primaryMetric; this.guard = guardrails; this.min = minSample;
    this.groups = { A: [], B: [] };
    this.metrics = { A: {}, B: {} };
  }
  assign(userId) {
    const group = stableHash(userId) < 0.5 ? 'A' : 'B';
    this.groups[group].push(userId);
    return group;                                      // 同用户稳定同组
  }
  ingest(group, metrics) {
    for (const [k, v] of Object.entries(metrics)) {
      (this.metrics[group][k] ??= []).push(v);
    }
  }
  checkGuardrails() {
    const violations = [];
    for (const [metric, maxDiff] of Object.entries(this.guard)) {
      const a = mean(this.metrics.A[metric] ?? []);
      const b = mean(this.metrics.B[metric] ?? []);
      if (b > a * (1 + maxDiff)) violations.push({ metric, a, b, maxDiff });
    }
    return { violations, shouldAbort: violations.length > 0 };
  }
  conclude() {
    const n = Math.min(this.groups.A.length, this.groups.B.length);
    if (n < this.min) return { verdict: 'insufficient-sample', need: this.min, have: n };
    const guard = this.checkGuardrails();
    if (guard.shouldAbort) return { verdict: 'aborted-guardrail', guard };
    const a = median(this.metrics.A[this.primary] ?? []);
    const b = median(this.metrics.B[this.primary] ?? []);
    const improvement = +(((a - b) / a) * 100).toFixed(1);
    const hypothesisMet = improvement >= this.h.expectedImprovement;
    return { verdict: hypothesisMet ? 'hypothesis-confirmed' : 'hypothesis-rejected',
      primary: { a, b, improvement }, recommendation: hypothesisMet ? 'full-rollout' : 'rollback-or-iterate' };
  }
}
// 用法: new EvolutionABTest({ hypothesis: { expectedImprovement: 30 },
//   primaryMetric: 'inp', guardrails: { errorRate: 0.2 }, minSample: 10000 })
```

**评分点**：
- 可证伪假设前置（预期改善 30%——避免事后找理由）
- 护栏指标（B 组错误率不得劣化——护栏破立即中止）
- 样本量前置估算（不足不结论）
- 决策建议输出（全量/回滚/延长——闭环）
