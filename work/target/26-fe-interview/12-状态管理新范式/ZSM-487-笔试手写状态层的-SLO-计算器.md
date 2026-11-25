---
title: [ZSM-487] 笔试：手写状态层 SLO 计算器
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-487：手写状态层 SLO 计算器
**答**：实现 `createSloTracker({ target })`：1) `recordGood()/recordBad()`：滑动窗口事件流（保留最近 28 天按分钟桶压缩：每桶 good/total 计数）；2) `compliance()`：good/total 比率与 target 比较；3) `errorBudget()`：剩余错误预算 =（1-target）× total - bad，可透支为负；4) `burnRate(windowMin)`：近期错误预算消耗速率 vs 理想速率（快烧告警依据：>14x 快烧）；5) `report()` 输出 compliance/budget/burnRate 与建议动作（快烧→冻结发布）。

```javascript
export function createSloTracker({ target = 0.999, windowMin = 28 * 24 * 60 } = {}) {
  const buckets = new Map()    // minuteIdx → { good, bad }

  function idx() { return Math.floor(Date.now() / 60_000) }

  function bump(kind) {
    const i = idx()
    const b = buckets.get(i) ?? { good: 0, bad: 0 }
    b[kind]++
    buckets.set(i, b)
    for (const k of buckets.keys()) if (idx() - k >= windowMin) buckets.delete(k)   // 滚动
  }

  function totals() {
    let good = 0, bad = 0
    buckets.forEach((b) => { good += b.good; bad += b.bad })
    return { good, bad, total: good + bad }
  }

  return {
    recordGood: () => bump('good'),
    recordBad: () => bump('bad'),
    compliance() {
      const { good, total } = totals()
      return total ? good / total : 1
    },
    errorBudget() {
      const { total, bad } = totals()
      return (1 - target) * total - bad                       // 可为负（透支）
    },
    burnRate(windowMin = 60) {
      const now = idx()
      let bad = 0, total = 0
      for (let i = now - windowMin + 1; i <= now; i++) {
        const b = buckets.get(i)
        if (b) { bad += b.bad; total += b.good + b.bad }
      }
      if (!total) return 0
      const actualBadRate = bad / total
      const idealBadRate = 1 - target
      return actualBadRate / idealBadRate                     // >14x 快烧
    },
    report() {
      const burn = this.burnRate()
      return {
        compliance: this.compliance(), budget: this.errorBudget(), burnRate: burn,
        action: burn > 14 ? 'freeze-release' : burn > 6 ? 'reduce-risk' : 'normal',
      }
    },
  }
}
```
**评分点**：
- 分钟桶压缩的滑动窗口（28 天窗口内存恒定）
- 错误预算公式正确（(1-target)×total - bad，可透支为负）
- burnRate 语义（实际坏率/理想坏率）与分级动作（>14x 冻结发布——SRE 标准实践）
- 滚动清理 + 全量 report 可观测
