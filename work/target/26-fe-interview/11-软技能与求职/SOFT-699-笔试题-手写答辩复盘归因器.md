---
title: [SOFT-699] 手写 failureAttribution：反馈逐条归因（能力/呈现/时机）、再战策略输出、改进项清单？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-699：手写 failureAttribution：反馈逐条归因（能力/呈现/时机）、再战策略输出、改进项清单

**需求与边界**：
- 实现 attributeFailure(feedback)。
- 边界要求：① 反馈条目自动归因三类：能力差距（“不具备/未达到”类词）、呈现问题（“未体现/不清楚/口径”类词）、时机问题（“名额/竞争/本批”类词）；② 按归因占比输出再战策略（能力型→6-12月计划/呈现型→下窗口即战/时机型→换池或排队）；③ 每条反馈生成改进项（owner=self, deadline=下次窗口-2月）；④ 反馈为空抛错。

**答**：
```javascript
function attributeFailure(feedback) {
  if (!feedback?.length) throw new Error('无反馈无法归因');
  const RULES = [
    [/不具备|未达到|深度不够|欠缺/, 'capability'],
    [/未体现|不清楚|口径|呈现|自足/, 'presentation'],
    [/名额|竞争|本批|时机|统筹/, 'timing'],
  ];
  const rows = feedback.map(f => {
    const cause = (RULES.find(([re]) => re.test(f.text)) ?? [null, 'capability'])[1];
    return { text: f.text, cause,
      fix: { capability: '能力补齐计划（6-12月，逐条对标能力模型）',
        presentation: '呈现工程重做（自足性/口径三要素/演练×3）',
        timing: '换池子或排队策略（SOFT-633四象限）' }[cause] };
  });
  const dist = countBy(rows, 'cause');
  const dominant = maxBy(Object.entries(dist), ([, v]) => v)[0];
  return { rows, dist,
    strategy: { capability: '间隔6-12月再战，先补能力',
      presentation: '下个窗口即战（材料重做+mock×3）',
      timing: '评估转岗/排队（能力已达标）' }[dominant],
    actions: rows.map(r => ({ item: r.text, owner: 'self',
      deadline: '下次窗口前2个月' })) };
}
```

**评分点**:
- 词表归因三类（能力/呈现/时机）——失败反馈自动结构化。
- 按主导归因输出再战策略（不同归因不同打法）。
- 改进项带 owner 与 deadline（复盘可执行不空转）。

