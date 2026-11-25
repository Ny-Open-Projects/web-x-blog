---
title: [SOFT-656] 手写 PipTracker：目标拆解、周自核、双周同步生成、达标预测？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-656：手写 PipTracker：目标拆解、周自核、双周同步生成、达标预测

**需求与边界**：
- 实现 PipTracker(goals, deadline)：goals 每条含 { name, criteria, weeks }。
- 边界要求：① 逐条周自核 record(week, status)（status: done/on-track/at-risk）；② at-risk 连续 2 周自动升级告警（建议求助）；③ 双周同步报告生成（每条状态+数据+需求支持）；④ 达标预测：按当前速率外推 deadline 前能否全达标；⑤ deadline 前一周生成最终评估材料。

**答**：
```javascript
class PipTracker {
  constructor(goals, deadline) {
    this.goals = goals.map(g => ({ ...g, history: [] }));
    this.deadline = deadline;
  }
  record(week, updates) {                          // {goalName: status}
    for (const g of this.goals) {
      const s = updates[g.name];
      if (s) g.history.push({ week, status: s });
      const h = g.history.slice(-2);
      if (h.length === 2 && h.every(x => x.status === 'at-risk'))
        alert({ type: 'pip-risk', goal: g.name,
          action: '连续2周at-risk——立即求助或调整方法' });
    }
  }
  report(biweekly) {
    return this.goals.map(g => {
      const last = g.history.at(-1)?.status ?? 'not-started';
      return `- ${g.name}：${last}（验收：${g.criteria}）`;
    }).join('\n') + '\n需要支持：…';              // 双周同步
  }
  forecast(currentWeek) {
    const left = this.deadline - currentWeek;
    const done = this.goals.filter(g =>
      g.history.at(-1)?.status === 'done').length;
    const rate = done / Math.max(currentWeek, 1);
    const projected = Math.round(done + rate * left);
    return { projected,
      verdict: projected >= this.goals.length ? 'on-track' : 'at-risk',
      note: '按当前速率外推；at-risk时加倍投入或协商范围' };
  }
}
```

**评分点**:
- at-risk 连续 2 周自动升级（PIP 期的求助时机自动化）。
- 双周同步报告直接可发（沟通线纪律落地）。
- 速率外推达标预测（早知道赶不上早动作）。

