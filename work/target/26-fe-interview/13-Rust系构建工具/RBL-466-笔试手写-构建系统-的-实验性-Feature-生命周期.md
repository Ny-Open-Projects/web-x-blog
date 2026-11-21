---
title: [RBL-466] 笔试：手写实验性 Feature 生命周期管理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-466：手写实验性 Feature 生命周期管理
**需求**：实现 `createFeatureLifecycle(registry)`：1) 注册：`register({ name, stage: 'experimental', owner, eolDate, docs })`——experimental 必须有 owner 与 EOL（无主人不进主干）；2) 阶段流转：experimental → stable（需采纳数据：使用者 ≥3 团队）→ deprecated（映射替代 + 期限）→ removed；3) 流转校验：跳阶段拒绝（experimental 不能直接 removed——要 deprecated 通知期）；4) 定期审计：experimental 超过 eolDate 未流转 → 告警（孤儿实验清理）；5) 输出生命周期看板（各阶段数量与即将 EOL 清单）。

```javascript
const FLOW = { experimental: ['stable', 'deprecated'], stable: ['deprecated'], deprecated: ['removed'] }

export function createFeatureLifecycle() {
  const features = new Map()

  function register(f) {
    if (f.stage === 'experimental' && (!f.owner || !f.eolDate))
      throw new Error(`experimental feature ${f.name} 需要 owner + eolDate`)
    features.set(f.name, { ...f, adoptedBy: [] })
  }

  function transition(name, to, adoptedData) {
    const f = features.get(name)
    if (!FLOW[f.stage]?.includes(to))
      throw new Error(`非法流转 ${f.stage} → ${to}（需按 ${FLOW[f.stage]} 顺序）`)
    if (to === 'stable' && (adoptedByCount(f) < 3 || !adoptedData?.evidence))
      throw new Error('stable 需要 ≥3 团队采纳证据')
    if (to === 'deprecated') {
      if (!adoptedData?.replacement) throw new Error('deprecated 必须声明 replacement')
      f.replacement = adoptedData.replacement
      f.removalDate = adoptedData.removalDate
    }
    f.stage = to
  }

  function audit() {
    const now = Date.now()
    const orphans = [...features.values()].filter((f) =>
      f.stage === 'experimental' && new Date(f.eolDate) < now)
    const eolSoon = [...features.values()].filter((f) =>
      f.eolDate && new Date(f.eolDate) - now < 30 * 86400_000)
    return { stages: groupByStage(), orphans, eolSoon }
  }

  function adoptedByCount(f) { return f.adoptedBy.length }
  function groupByStage() {
    const out = {}
    for (const f of features.values()) (out[f.stage] ??= []).push(f.name)
    return out
  }

  return { register, transition, audit, markAdopted: (name, team) => features.get(name)?.adoptedBy.push(team) }
}
```
**评分点**：
- 注册强制 owner + EOL（无主实验不进主干——孤儿实验的根源治理）
- 流转校验（跳阶段拒绝 / stable 需采纳证据 / deprecated 必须有替代——每步有门槛）
- 采纳数据驱动晋升（≥3 团队——不是作者自说自话）
- 审计看板（orphans/EOL 临近——生命周期的运营闭环）
