---
title: [SOFT-538] 手写 RiskRegister：风险条目增改、概率影响评分、触发条件强制、检查点联动？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-538：手写 RiskRegister：风险条目增改、概率影响评分、触发条件强制、检查点联动

**需求与边界**：
- 实现 RiskRegister：add/update/checkpoints(milestones)。
- 边界要求：① add 强制 trigger 与 fallback 字段（缺失抛错——防形式化风险表）；② 评分 = 概率(1~3)×影响(1~3)，≥6 标红；③ 每条风险必须挂里程碑检查点；④ update 保留历史（变更留痕）；⑤ 红色风险清单单独输出。

**答**：
```javascript
class RiskRegister {
  constructor() { this.items = new Map(); this.seq = 0; }
  add({ name, probability, impact, trigger, fallback, milestone }) {
    if (!trigger || !fallback)
      throw new Error('风险必须含触发条件与兜底');   // 强制字段
    if (!milestone) throw new Error('必须挂检查点');
    const id = `R${++this.seq}`;
    const score = probability * impact;
    this.items.set(id, { id, name, probability, impact, score,
      trigger, fallback, milestone, history: [], status: 'open' });
    return id;
  }
  update(id, patch, by) {
    const r = this.items.get(id);
    r.history.push({ at: Date.now(), by, patch });   // 变更留痕
    Object.assign(r, patch);
    r.score = r.probability * r.impact;
  }
  redList() {
    return [...this.items.values()].filter(r => r.score >= 6);
  }
  checkpoints(milestones) {
    return milestones.map(m => ({
      milestone: m, risks:
        [...this.items.values()].filter(r => r.milestone === m) }));
  }
}
```

**评分点**:
- trigger/fallback/milestone 三强制（风险表反形式化的核心）。
- 评分矩阵 + ≥6 红色清单；update 历史留痕。

