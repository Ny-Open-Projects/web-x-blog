---
title: [SOFT-540] 手写 preAlignPlan：干系人分级、定制沟通包、意见台账结构、会前截止？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-540：手写 preAlignPlan：干系人分级、定制沟通包、意见台账结构、会前截止

**需求与边界**：
- 实现 preAlignPlan(doc, stakeholders)。
- 边界要求：① 干系人分级（决策人/受影响方/专家）按角色生成定制沟通包（决策人：摘要+决策点；受影响方：影响+缓解；专家：技术决策点）；② 每人分配时隙与截止（评审前 48h 完成全部预沟通）；③ 意见台账结构生成（采纳/不采纳双栏）；④ 决策人最后沟通（吸收完意见再定稿）；⑤ 输出执行清单。

**答**：
```javascript
function preAlignPlan(doc, stakeholders, { reviewAt }) {
  const cutoff = new Date(reviewAt - 48 * 3600e3);  // 前48h
  const order = { influencer: 0, expert: 1, decision: 2 }; // 决策人最后
  const pack = {
    decision: (s) => ({ summary: doc.oneline,
      ask: doc.decisionPoints, schedule: doc.milestones }),
    influencer: (s) => ({ impact: doc.impactOf(s.team),
      mitigation: doc.mitigations?.[s.team] ?? '待补' }),
    expert: (s) => ({ decisions: doc.decisions,
      ask: '帮看技术决策点有没有坑' }),
  };
  const plan = stakeholders
    .sort((a, b) => order[a.role] - order[b.role])
    .map((s, i) => ({
      who: s.name, role: s.role,
      pack: pack[s.role](s),
      slot: `评审前第${3 - i}天`,                   // 时隙分配
      due: cutoff.toISOString().slice(0, 10),
    }));
  return { plan,
    ledger: { columns: ['意见', '来自', '采纳/不采纳', '理由'],
      rule: '每条意见24h内回应' },
    gate: plan.every(p => new Date(p.due) <= cutoff)
      ? '可进评审' : '预沟通未完成，评审应延期' };
}
```

**评分点**:
- 三角色定制沟通包内容差异化；决策人排序最后（先吸收意见）。
- 48h 截止 gate（预沟通未完成评审延期——流程有牙齿）。
- 意见台账双栏结构（含不采纳理由）。

