---
title: [SOFT-737] 手写 knowledgeSpillover：四通道记录（结对/培训/文档/review）、外溢度量化、“没有我也能做”覆盖检查？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-737：手写 knowledgeSpillover：四通道记录（结对/培训/文档/review）、外溢度量化、“没有我也能做”覆盖检查

**需求与边界**：
- 实现 SpilloverMeter：log(channel, target, note)/coverage(criticalTasks)。
- 边界要求：① 四通道记录（channel ∈ pair/training/doc/review，非法抛错）；② 外溢度 = 各通道季度计数加权（doc×2 因可复用）；③ coverage：关键任务清单逐项检查“是否有第二人可做”（single-point 任务列出——单点依赖清单）；④ 输出改进建议（单点任务→结对/文档化建议）。

**答**：
```javascript
class SpilloverMeter {
  constructor() { this.logs = []; }
  log(channel, target, note) {
    if (!['pair', 'training', 'doc', 'review'].includes(channel))
      throw new Error(`非法通道：${channel}`);
    this.logs.push({ channel, target, note, q: curQuarter() });
  }
  score() {
    const W = { doc: 2, training: 1.5, pair: 1, review: 0.5 };
    const q = this.logs.filter(l => l.q === curQuarter());
    return Object.entries(W).map(([c, w]) => ({
      channel: c, count: q.filter(l => l.channel === c).length,
      weighted: q.filter(l => l.channel === c).length * w }));
  }
  coverage(criticalTasks, teamSkills) {
    const single = criticalTasks.filter(t =>
      !teamSkills.some(p => p.skills.includes(t) && p.id !== ME));
    return { singlePoint: single,
      advice: single.map(t => `${t}：单点依赖——建议结对1次+文档化1篇（本月）`) };
  }
}
```

**评分点**:
- 四通道非法值抛错；doc 加权最高（可复用知识外溢最值钱）。
- 单点依赖清单 + 逐项改进建议（“没有我也能做”的量化检查）。

