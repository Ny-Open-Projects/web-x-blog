---
title: [SOFT-658] 手写 perfCalendar：六阶段时间线、关键动作提醒、截止倒计时？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-658：手写 perfCalendar：六阶段时间线、关键动作提醒、截止倒计时

**需求与边界**：
- 实现 perfCalendar(cycle)：cycle 含 { start, selfReviewDue, reviewAt, nextCycleStart }。
- 边界要求：① 六阶段动作清单按日期排布（目标对齐/周记/中段校准/弹药包/自评/面谈准备）；② 每个动作带提前量（自评截止前 2 周开始写）；③ deadline 倒计时（距今 N 天——紧急动作标红）；④ 中段校准自动落在周期中点；⑤ 输出按时间排序的可执行日历。

**答**：
```javascript
function perfCalendar(cycle, { today = Date.now() } = {}) {
  const mid = (cycle.start + cycle.selfReviewDue) / 2; // 中点
  const actions = [
    { at: cycle.start, act: '三问对齐+邮件锚定', prio: 1 },
    { at: cycle.start + 7 * 864e5, act: '周记证据链启动（每周五）', prio: 1 },
    { at: mid, act: '中段校准1:1（进度/方向对齐）', prio: 2 },
    { at: cycle.selfReviewDue - 14 * 864e5,
      act: '弹药包给领导（辩护材料）', prio: 1 },
    { at: cycle.selfReviewDue - 7 * 864e5, act: '自评定稿', prio: 1 },
    { at: cycle.reviewAt - 3 * 864e5,
      act: '面谈准备（材料/三问/演练）', prio: 1 },
  ];
  return actions.map(a => {
    const days = Math.round((a.at - today) / 864e5);
    return { ...a, inDays: days,
      flag: days >= 0 && days <= 7 ? '🔴本周' :
            days < 0 ? '⚠️已过' : '📅待办' };
  }).sort((a, b) => a.at - b.at);
}
```

**评分点**:
- 中段校准自动落在周期中点（校准时机不靠自觉）。
- 弹药包/自评的提前量设计（deadline 前 2 周开始写）。
- 倒计时分级标注（本周/已过/待办）。

