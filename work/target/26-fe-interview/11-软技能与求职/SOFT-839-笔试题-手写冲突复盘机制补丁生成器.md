---
title: [SOFT-839] 手写 conflictPostmortem：冲突复盘→机制缺口提取→补丁项生成（owner/deadline/验证方式）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-839：手写 conflictPostmortem：冲突复盘→机制缺口提取→补丁项生成（owner/deadline/验证方式）

**需求与边界**：
- 实现 conflictPostmortem(conflict, timeline, rootCauses)。
- 边界要求：① 缺口分类：rootCauses 每条映射机制补丁（分工不清→RACI/信息不对称→同步契约/决策漂移→ADR/表达越界→沟通公约——SOFT-811 清单）；② 每补丁 { item, owner, deadline, verify }（验证方式必填——闭环 SOFT-553）；③ 无责基调校验：rootCauses 含人格归因（“某人态度差”）→拒绝并要求重述为机制归因；④ 输出复盘报告。

**答**：
```javascript
const PATCH = {
  '分工不清': { item: '补RACI矩阵', verify: '下迭代RACI覆盖率检查（SOFT-830）' },
  '信息不对称': { item: '补变更通知契约（48h前置）', verify: '下月漏同步事件数=0' },
  '决策漂移': { item: '关键决策补ADR', verify: 'ADR归档率检查（SOFT-811）' },
  '表达越界': { item: '沟通公约（对事激烈对人温和）', verify: '下季度人际冲突数' },
};
function conflictPostmortem(conflict, timeline, rootCauses) {
  const report = [];
  const actions = [];
  for (const c of rootCauses) {
    if (/态度差|人品|这人不行/.test(c))
      throw new Error(`人格归因违规：「${c}」——重述为机制归因（无责基调 SOFT-817）`);
    const patch = PATCH[c] ?? { item: `机制补丁：${c}`,
      verify: '下季度同型冲突数对比' };
    actions.push({ ...patch, owner: 'TL', deadline: '+2周' });
    report.push(`- 根因：${c} → 补丁：${patch.item}（验证：${patch.verify}）`);
  }
  return { conflict,
    timelineSummary: timeline.length + '个事件节点',
    actions, report: report.join('\n'),
    note: '无责基调：对事不对人（SOFT-817）' };
}
```

**评分点**:
- 根因→补丁映射表（冲突的产出=机制升级 SOFT-811 落地）。
- 人格归因拒绝机制（无责基调的工具化防线）。
- 每补丁带验证方式（复盘闭环不空转）。

