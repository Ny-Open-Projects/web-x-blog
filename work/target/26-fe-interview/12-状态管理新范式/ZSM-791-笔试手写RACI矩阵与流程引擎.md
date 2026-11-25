---
title: [ZSM-791] 笔试：手写治理流程引擎（RACI 分发 + 工单流转 + 逾期升级）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-791：手写治理流程引擎（RACI 分发 + 工单流转 + 逾期升级）
**答**：实现 `createGovernanceFlow()`：1) `open(kind, payload)`：开单（store-proposal / alert / debt）按流程定义分发给对应角色（RACI 表驱动）；2) `transition(ticketId, action, byRole)`：状态机流转——校验「该角色是否有权执行该动作」（RACI Responsible/Accountable 校验）；3) 逾期升级：deadline 过期未完成自动升级到上级角色（按 ESCALATION 链）；4) `audit()`：流转历史与逾期统计；5) 附用例：越权流转拒绝 + 逾期升级链。

```javascript
const RACI = {
  'store-proposal': {
    steps: ['review-adr', 'registry', 'lint-enable'],
    roles: { 'review-adr': ['架构Owner'], registry: ['架构Owner'], 'lint-enable': ['门禁Keeper'] },
  },
  alert: { steps: ['ack', 'mitigate', 'postmortem'], roles: { ack: ['业务Owner'], mitigate: ['业务Owner'], postmortem: ['架构Owner'] } },
  debt: { steps: ['assess', 'schedule', 'repay'], roles: { assess: ['架构Owner'], schedule: ['业务Owner'], repay: ['业务Owner'] } },
}
const ESCALATION = { '业务Owner': '架构Owner', '架构Owner': 'CTO', CTO: null }

function createGovernanceFlow({ now = Date.now } = {}) {
  const tickets = new Map()     // id -> { kind, step, assigned, deadline, history, done }
  const listeners = new Set()
  let seq = 0

  function open(kind, payload, { deadlineMs = 14 * 864e5 } = {}) {
    const def = RACI[kind]
    const id = `T-${++seq}`
    const first = def.steps[0]
    const t = {
      id, kind, step: first,
      assigned: def.roles[first][0],
      deadline: now() + deadlineMs,
      history: [{ ts: now(), action: 'open', by: payload.by ?? 'system', step: first }],
      done: false, payload,
    }
    tickets.set(id, t)
    return t
  }

  function transition(id, action, byRole) {
    const t = tickets.get(id)
    const def = RACI[t.kind]
    // RACI 校验：当前步骤的授权角色
    const allowed = def.roles[t.step] ?? []
    if (!allowed.includes(byRole)) {
      return { ok: false, reason: `角色 ${byRole} 无权执行 ${t.step}（需 ${allowed.join('/')}）` }
    }
    t.history.push({ ts: now(), action, by: byRole, step: t.step })
    const nextIdx = def.steps.indexOf(t.step) + 1
    if (nextIdx >= def.steps.length) {
      t.done = true
      listeners.forEach((fn) => fn({ type: 'closed', id }))
      return { ok: true, closed: true }
    }
    t.step = def.steps[nextIdx]
    t.assigned = def.roles[t.step][0]
    return { ok: true, next: t.step, assigned: t.assigned }
  }

  // 逾期升级
  function escalateOverdue() {
    const escalated = []
    for (const t of tickets.values()) {
      if (t.done || now() <= t.deadline) continue
      const next = ESCALATION[t.assigned]
      if (next) {
        t.history.push({ ts: now(), action: 'escalate', from: t.assigned, to: next })
        t.assigned = next
        t.deadline = now() + 3 * 864e5          // 升级后新期限
        escalated.push(t.id)
        listeners.forEach((fn) => fn({ type: 'escalated', id: t.id, to: next }))
      }
    }
    return escalated
  }

  function audit() {
    const all = [...tickets.values()]
    return {
      open: all.filter((t) => !t.done).length,
      done: all.filter((t) => t.done).length,
      overdue: all.filter((t) => !t.done && now() > t.deadline).length,
      byKind: all.reduce((a, t) => ((a[t.kind] = (a[t.kind] ?? 0) + 1), a), {}),
    }
  }

  return { open, transition, escalateOverdue, audit, subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)) }
}

// 用例
const flow = createGovernanceFlow()
const t1 = flow.open('store-proposal', { name: 'wizardStore' })
// 越权：业务Owner 不能评审 ADR
console.log(flow.transition(t1.id, 'approve', '业务Owner'))
// { ok: false, reason: '角色 业务Owner 无权执行 review-adr（需 架构Owner）' }
console.log(flow.transition(t1.id, 'approve', '架构Owner'))   // → registry
console.log(flow.transition(t1.id, 'register', '架构Owner'))  // → lint-enable
console.log(flow.transition(t1.id, 'enable', '门禁Keeper'))   // closed

// 逾期升级
const t2 = flow.open('alert', { level: 'P1' }, { deadlineMs: -1000 })   // 已过期
console.log(flow.escalateOverdue())           // ['T-2']：升级到 架构Owner
console.log(flow.audit())
```
**评分点**：
- RACI 驱动的角色校验（越权流转拒绝，错误信息含授权角色）
- 流程定义外置（RACI 表配置化，新增流程不改引擎）
- 逾期升级链（ESCALATION 链 + 新期限）
- audit 统计（open/done/overdue/byKind）
