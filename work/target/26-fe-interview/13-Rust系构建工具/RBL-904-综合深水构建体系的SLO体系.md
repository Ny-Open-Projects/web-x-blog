---
title: [RBL-904] 综合深水：构建体系的 SLO——把构建当服务运营的四个 SLI
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-904：综合深水：构建体系的 SLO——四个 SLI 与错误预算

**答**:
- 把构建平台当服务运营（SLO 化）：1) **可用性 SLI**（构建任务成功率 ≥ 99.5%——区分平台故障 vs 用户错误：平台故障才计错误预算）；2) **时延 SLI**（P95 构建时长 ≤ 基线 ×1.1）；3) **新鲜度 SLI**（缓存正确性：抽样校验产物与源码一致 RBL-702——0.1% 抽样 × 24h）；4) **正确性 SLI**（语义等价：产物行为测试通过率）。每个 SLI 有目标 + 错误预算（超支即冻结特性开发转向稳定性——Google SRE 的预算纪律）。
- 错误预算的分配：预算花在「变更」上（升级/新特性会消耗预算）——预算耗尽的应对不是停止变更而是「变更加速验证」（canary/影子构建 RBL-667）。
- SLI 的测量陷阱：成功率统计的「分母污染」（重复重试的成功算一次还是两次——重试语义 RBL-856 的口径）；时延的「输入可比性」（不同仓库不可比——按 preset 类型分桶）。
- 构建平台 SLO 与业务 SLO 的衔接：构建延迟影响「修复上线时间」（MTTR 的组成部分）——构建 P95 是「线上故障平均恢复时间」的上游变量——平台 SLO 的业务价值可以量化到 incident 修复链路。
- 追问钩子：为什么「新鲜度 SLI」最容易被遗漏却最致命？——可用性/时延坏了立刻可见（构建失败/变慢）；缓存新鲜度坏了是「静默错误」（旧产物正常部署 RBL-702 的 stale 危险）——SLI 体系的完整性由「最静默的失败模式」决定：可用性监控一堆、正确性抽样没有 = 半截 SLO。

```javascript
// SLO 定义与预算
const SLO = {
  availability: { sli: (r) => r.platformFailures === 0 ? 1 : 0, target: 0.995,
    note: '用户错误（代码编译失败）不计入平台故障' },
  latency: { sli: (r) => r.p95BuildMs, target: 'baseline*1.1',
    note: '按 preset 类型分桶（RBL-677）' },
  freshness: { sli: (r) => r.sampledStale / r.sampled, target: 0.001,
    note: '每日抽样校验产物新鲜度（RBL-702）' },
  correctness: { sli: (r) => r.behaviorPassRate, target: 1.0 },
};
function errorBudget(sli, target, windowDays = 28) {
  const actual = sli(windowStats(windowDays));
  const budgetLeft = (actual - target) / (1 - target);   // 剩余预算比例
  if (budgetLeft <= 0)
    return { status: 'budget-exhausted', action: '冻结特性变更，转向稳定性修复' };
  return { status: 'ok', budgetLeft: +budgetLeft.toFixed(2) };
}
```
