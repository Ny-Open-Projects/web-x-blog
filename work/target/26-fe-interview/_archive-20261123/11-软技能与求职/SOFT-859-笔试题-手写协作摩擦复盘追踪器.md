---
title: [SOFT-859] 手写 frictionLedger：摩擦事件的记录归因、机制补丁关联、复发检测、月度趋势？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-859：手写 frictionLedger：摩擦事件的记录归因、机制补丁关联、复发检测、月度趋势

**需求与边界**：
- 实现 frictionLedger：log(event, cause)/patch(cause, patchItem)/trend()。
- 边界要求：① 摩擦事件记录（SOFT-815 触发点清单的账本化）+归因（机制类原因映射补丁 SOFT-839）；② 复发检测：同因摩擦 ≥2 次→补丁失效告警（补丁是否真落地——SOFT-553 闭环检查）；③ 月度趋势：摩擦数按月统计与环比；④ 无责校验（人格归因拒绝 SOFT-839）。

**答**：
```javascript
class frictionLedger {
  constructor() { this.events = []; }
  log(event, cause) {
    if (/态度|人品|这人/.test(cause))
      throw new Error('人格归因违规——机制归因重述（SOFT-839）');
    this.events.push({ event, cause, at: Date.now() });
  }
  patch(cause, patchItem, verify) {
    this.patchOf = this.patchOf ?? {};
    this.patchOf[cause] = { item: patchItem, verify, at: Date.now() };
  }
  trend() {
    const byMonth = {};
    for (const e of this.events) {
      const m = new Date(e.at).toISOString().slice(0, 7);
      byMonth[m] = (byMonth[m] ?? 0) + 1;
    }
    const months = Object.keys(byMonth).sort();
    const recurrence = {};
    for (const e of this.events) {
      recurrence[e.cause] = (recurrence[e.cause] ?? 0) + 1;
      if (recurrence[e.cause] >= 2 && this.patchOf?.[e.cause])
        e.alert = `「${e.cause}」已打补丁仍复发——补丁落地检查（SOFT-553）`;
    }
    return { byMonth, trend: months.length >= 2 &&
        byMonth[months.at(-1)] >= byMonth[months.at(-2)]
      ? '环比未降——机制补丁需加强' : '改善中',
      recurrenceAlerts: this.events.filter(e => e.alert) };
  }
}
```

**评分点**:
- 摩擦账本化（SOFT-815 触发点清单的持续运营）。
- 复发检测（打补丁仍复发=补丁落地检查——SOFT-553 闭环工具化）。
- 月度趋势环比（协作摩擦的可运营化 SOFT-830）。

