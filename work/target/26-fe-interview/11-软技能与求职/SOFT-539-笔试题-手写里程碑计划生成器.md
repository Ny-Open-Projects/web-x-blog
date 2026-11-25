---
title: [SOFT-539] 手写 genMilestones：阶段拆分、交付物与验证方式强制、依赖倒排检查、缓冲位？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-539：手写 genMilestones：阶段拆分、交付物与验证方式强制、依赖倒排检查、缓冲位

**需求与边界**：
- 实现 genMilestones(stages, deps, { endDate })。
- 边界要求：① 每阶段强制 deliverable 与 verify 字段（缺则抛错）；② 依赖倒排检查：依赖方 deadline 必须 ≤ 其被需要的里程碑起点，违反报 conflict；③ 阶段间自动插入缓冲（联调窗口，总时长 10%，不超 1 周）；④ 输出时间线与冲突清单。

**答**：
```javascript
function genMilestones(stages, deps, { endDate }) {
  const conflicts = [];
  for (const d of deps) {
    const need = stages.find(s => s.needs?.includes(d.id));
    if (need && d.deadline > need.start)
      conflicts.push({ dep: d.id, deadline: d.deadline,
        neededBy: need.name, action: '倒排催办或换路径' });
  }
  const totalDays = stages.reduce((a, s) => a + s.days, 0);
  const buffer = Math.min(Math.ceil(totalDays * 0.1), 5); // 缓冲
  const timeline = [];
  let cursor = endDate;
  for (const s of [...stages].reverse()) {          // 倒排
    cursor = addDays(cursor, -(s.days));
    timeline.unshift({ name: s.name, start: cursor,
      deliverable: s.deliverable, verify: s.verify });
    if (buffer && stages.indexOf(s) < stages.length - 1) {
      cursor = addDays(cursor, -buffer);
      timeline.unshift({ name: '联调缓冲', start: cursor, days: buffer });
    }
  }
  return { timeline, conflicts, buffer };
}
```

**评分点**:
- deliverable/verify 强制（里程碑=验收标准不是日历）；缺则抛错。
- 依赖倒排冲突检测（deadline ≤ 所需起点）；冲突带行动建议。
- 缓冲放阶段间（封顶 1 周），倒排日期计算正确。

