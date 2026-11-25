---
title: [AGT-471] 笔试题——实现任务状态机引擎（状态定义+非法迁移拒绝+持久化）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-471：手写状态机引擎：状态/迁移定义、非法迁移拒绝、持久化恢复

**需求与边界**：
- 输入：状态机定义（states/transitions/onEnter）、任务实例；输出：状态管理服务。
- 边界要求：① 迁移表驱动（非法迁移直接拒绝并留痕）；② onEnter 钩子（进入状态自动动作：通知/计费）；③ 状态变更持久化（崩溃恢复到最后合法状态）；④ 并发迁移互斥（同任务同时迁移串行化）。

**答**：
```javascript
class StateMachine {
  constructor({ states, transitions, onEnter = {}, persist }) {
    this.states = states;
    this.transitions = transitions;      // {from: {to: guardFn}}
    this.onEnter = onEnter; this.persist = persist;
    this.locks = new Map();             // 任务级互斥
  }
  async transition(taskId, from, to, payload) {
    // 1. 互斥（同任务串行化）
    const release = await acquire(this.locks, taskId);
    try {
      const legal = this.transitions[from]?.[to];
      if (!legal) {
        await this.persist.audit({ taskId, from, to,
          rejected: true, reason: 'ILLEGAL_TRANSITION' });
        throw new Error(`${from} → ${to} 非法迁移`);
      }
      // 2. guard 条件
      if (legal.guard && !await legal.guard(payload))
        throw new Error(`迁移条件不满足: ${from}→${to}`);
      // 3. 持久化新状态（先落库后钩子）
      await this.persist.save(taskId, { state: to, from,
        ts: Date.now(), payload });
      // 4. onEnter 钩子（失败不回滚状态但告警）
      const hook = this.onEnter[to];
      if (hook) await hook(taskId, payload)
        .catch(e => alert('HOOK_FAILED', { taskId, to, e }));
      return { state: to };
    } finally { release(); }
  }
  async recover(taskId) {               // 崩溃恢复
    const s = await this.persist.load(taskId);
    return s.state;                     // 最后合法状态
  }
}
// 定义示例：
// transitions: {
//   pending:   { running: {guard: hasQuota}, cancelled: {} },
//   running:   { done: {}, failed: {}, paused: {} },
//   paused:    { running: {}, cancelled: {} },
// }
// paused→done 为非法迁移（跳过恢复），自动拒绝。
```

**评分点**:
- 迁移表驱动+guard 条件，非法迁移拒绝且审计留痕。
- onEnter 钩子失败不回滚状态但告警（状态一致性优先）。
- 崩溃恢复到最后合法状态（先落库后钩子的顺序保障）。
- 任务级互斥（并发迁移串行化）。
