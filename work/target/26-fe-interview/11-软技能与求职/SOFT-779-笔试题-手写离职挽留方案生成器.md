---
title: [SOFT-779] 手写 retentionPlan：离职原因归因（成长/关系/方向/薪酬）、48h 方案生成、兑现跟踪？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-779：手写 retentionPlan：离职原因归因（成长/关系/方向/薪酬）、48h 方案生成、兑现跟踪

**需求与边界**：
- 实现 retentionPlan(person, reason)。
- 边界要求：① reason 归因四类（growth/relation/direction/pay——按主诉分类）；② 48h 方案：每类对应具体动作（growth→新角色+项目/relation→关系修复动作/direction→方向调整/pay→合规范围内的薪酬复核——不合规承诺不生成）；③ 方案每条带兑现 deadline 与 owner（空头承诺拒绝生成）；④ 输出 2 周后的兑现核查清单。

**答**：
```javascript
function retentionPlan(person, reason, { today = Date.now() } = {}) {
  const T = {
    growth: { act: [`新角色：${person.aspireRole}方向的项目owner位`,
      `导师资源：${person.mentorWish}`],
      note: '成长型离职——钱解决不了，给位子给舞台' },
    relation: { act: ['与冲突方的三方对齐会（本周）',
      '调整协作接口减少摩擦面'], note: '关系型——修复要具体到事件' },
    direction: { act: ['方向调整：转入其认同的业务线评估',
      '过渡期安排：现项目交接+新线shadow'],
      note: '方向型——强留无意义，帮找内部路径' },
    pay: { act: ['按合规流程提交薪酬复核（走HR通道，2周内出结果）'],
      note: '薪酬型——只走合规通道，不口头许钱' },
  };
  const plan = T[reason.type];
  if (!plan) throw new Error('归因必须为growth/relation/direction/pay');
  const actions = plan.act.map(a => ({ action: a,
    owner: 'TL', deadline: new Date(today + 2 * 864e5).toISOString().slice(0, 10) }));
  return { note: plan.note, actions,
    verifyAt: new Date(today + 14 * 864e5).toISOString().slice(0, 10),
    verifyChecklist: actions.map(a => `${a.action}——兑现了吗？（未兑现=二次伤害）`) };
}
```

**评分点**:
- 四类归因对应差异化动作（成长型给位子而非加钱）。
- 每条动作带 deadline+owner（48h 具体方案——空头挽留词拒绝生成）。
- 2 周兑现核查清单（承诺不兑现=二次伤害的防线）。

