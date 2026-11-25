---
title: [AGT-494] 笔试题——实现 deadline 传播（全链路死线+节点预算扣减+到期降级）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-494：手写 deadline 传播：总死线、各段预算扣减、剩余时间决策

**需求与边界**：
- 输入：总 deadline、各阶段预估；输出：每步的剩余预算与决策。
- 边界要求：① deadline 随上下文传播（每步可知剩余时间）；② 节点超支决策（快到期→跳过可选步骤/降级产出）；③ 关键步骤保护（预留最低预算）；④ 到期强制收尾（部分结果+缺口声明）。

**答**：
```javascript
class Deadline {
  constructor({ totalMs, startedAt = Date.now() }) {
    this.end = startedAt + totalMs;
  }
  remaining() { return Math.max(0, this.end - Date.now()); }
  // 每步调用：决定执行策略
  plan(step, { critical = false, estMs }) {
    const left = this.remaining();
    // 1. 关键步骤保护：剩余不足最低预算 → 直接收尾
    const MIN = 2000;
    if (left < MIN)
      return { action: 'finalize', reason: 'deadline 临近' };
    // 2. 可选步骤：剩余时间不够预估 → 跳过
    if (!critical && estMs > left * 0.6)
      return { action: 'skip', reason: `预计 ${estMs}ms > 剩余 ${left}`,
        degraded: true };
    // 3. 正常执行但带子预算（防止一步吃光）
    return { action: 'run',
      subBudget: Math.min(estMs * 1.2,
        critical ? left : left * 0.6),           // 可选步骤限 60%
      onSubTimeout: critical ? 'best_effort' : 'skip' };
  }
  async runWith(step, budget, fn) {
    const r = await Promise.race([
      fn(), sleep(budget).then(() => ({ timeout: true }))]);
    if (r.timeout)
      return step.critical
        ? { partial: true, note: '尽力产出部分结果' }   // 关键步骤尽力而为
        : { skipped: true };
    return r;
  }
}
// finalize 出口：聚合已完成+缺口声明（AGT-489 联动）。
```

**评分点**:
- deadline 全链路传播（每步可查剩余时间）。
- 三档决策：finalize（最低保护预算）/skip（可选步骤时间不够）/run（子预算限制）。
- 关键步骤 best_effort（尽力产出）vs 可选步骤直接跳过。
- 与部分结果聚合联动收尾。
