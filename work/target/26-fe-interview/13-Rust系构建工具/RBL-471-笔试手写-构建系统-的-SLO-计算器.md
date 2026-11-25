---
title: [RBL-471] 笔试：手写构建平台 SLO 计算器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-471：手写构建平台 SLO 计算器
**答**：实现 `createSlo({ targets })`：1) 多 SLO 并行追踪：构建成功率/缓存命中率/P95 时长——各自独立滑窗；2) 分母规则：成功率排除用户代码错误（用户错误是正常信号）——分母分类是 SLO 设计核心；3) 错误预算：每 SLO 独立预算，burn rate 分级（>14x 冻结合流）；4) 按维度切片：按分支（main 与 feature SLO 分开）/按团队（谁在消耗预算）；5) report() 输出各 SLO 达成/预算余量/烧速率/建议动作。

```javascript
export function createSlo({ targets }) {
  const windows = new Map()       // sloName → { good, bad, byTeam: Map, byBranch: Map }
  for (const name of Object.keys(targets)) windows.set(name, { good: 0, bad: 0, byTeam: new Map(), byBranch: new Map() })

  function record(name, { ok, team, branch, userError = false }) {
    const w = windows.get(name)
    if (!w) return
    // 分母规则：用户代码错误不算 bad（不计入 SLO 分母）
    if (name.includes('success') && userError) return
    w[ok ? 'good' : 'bad']++
    for (const dim of [w.byTeam, w.byBranch]) {
      const key = dim === w.byTeam ? team : branch
      const b = dim.get(key) ?? { good: 0, bad: 0 }
      b[ok ? 'good' : 'bad']++
      dim.set(key, b)
    }
  }

  function burnRate(name, windowMin = 60) {
    const w = windows.get(name)
    const total = w.good + w.bad
    if (!total) return 0
    const actualBadRate = w.bad / total
    const ideal = 1 - targets[name]
    return +(actualBadRate / ideal).toFixed(2)
  }

  function report() {
    return Object.fromEntries(Object.entries(targets).map(([name, t]) => {
      const w = windows.get(name)
      const total = w.good + w.bad
      const burn = burnRate(name)
      return [name, {
        compliance: total ? +(w.good / total).toFixed(4) : 1,
        budgetLeft: +( (1 - t) * total - w.bad ).toFixed(1),
        burnRate: burn,
        action: burn > 14 ? 'freeze-merges' : burn > 6 ? 'reduce-risk' : 'normal',
        byTeam: Object.fromEntries([...w.byTeam].map(([k, v]) => [k, v.bad])),
      }]
    }))
  }

  return { record, report }
}

// 用法
// slo.record('build-success', { ok: false, team: 'growth', branch: 'main', userError: false })
// slo.record('build-success', { ok: false, team: 'growth', branch: 'main', userError: true }) ← 不计入
```
**评分点**：
- 分母规则核心（用户代码错误不计入 SLO——口径设计最容易错的点）
- 多 SLO 独立窗口 + 维度切片（byTeam 预算消耗归因）
- burn rate 分级动作（>14x 冻结合流——SRE 标准实践）
- 空窗口返回 1（无数据不误报）
