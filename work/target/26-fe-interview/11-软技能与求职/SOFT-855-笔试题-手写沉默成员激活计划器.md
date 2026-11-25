---
title: [SOFT-855] 手写 silenceActivation：沉默成员的激活计划（诊断/结构化邀请/书面渠道/小会优先/放大归功）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-855：手写 silenceActivation：沉默成员的激活计划（诊断/结构化邀请/书面渠道/小会优先/放大归功）

**需求与边界**：
- 实现 silenceActivation(member)。
- 边界要求：① member 含 { id, silenceReasons: [] }（被忽视史/资历压力/性格/冲突恐惧——多选）；② 激活计划按原因生成（SOFT-844 四法映射：冲突恐惧→心理安全建设先行/性格→书面渠道/资历压力→小会优先/被忽视史→发言放大归功）；③ 每条动作带验收指标（发言频率/被采纳率——SOFT-844 度量）；④ 4 周计划表输出。

**答**：
```javascript
function silenceActivation(member) {
  const R = member.silenceReasons ?? [];
  if (!R.length) throw new Error('需先诊断沉默原因（SOFT-844四因）');
  const M = {
    '冲突恐惧': { act: '团队心理安全建设：资深者示范认错+坏消息零惩罚（SOFT-818）',
      metric: '该成员开始提出异议（8周内）' },
    '性格': { act: '书面渠道补充：异步讨论先请他书面发言（SOFT-822）',
      metric: '书面发言≥1次/周' },
    '资历压力': { act: '小会优先：3人小会让其发言成功后再上大会',
      metric: '小会发言≥1次/周' },
    '被忽视史': { act: '发言放大：采纳时公开归功（SOFT-762）',
      metric: '被归功≥1次/月' },
  };
  const plan = R.flatMap(r => M[r] ? [{ reason: r, ...M[r] }] : []);
  if (!plan.length)
    plan.push({ reason: '综合', act: '1:1深谈诊断（SOFT-591结构）',
      metric: '完成1次深度对话' });
  return { member: member.id, plan,
    weeks: plan.map((p, i) => ({ week: i + 1, focus: p.reason,
      action: p.act, verify: p.metric })),
    note: '激活成功标志：发言频率与被采纳率趋势上升（SOFT-844度量）' };
}
```

**评分点**:
- 按沉默原因映射差异化激活法（SOFT-844 四法落地）。
- 每动作带可验证指标（发言频率/采纳率——激活可度量）。
- 无诊断先 1:1 深谈兜底（不瞎激活）。

