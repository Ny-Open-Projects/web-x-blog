---
title: [SOFT-857] 手写 supportDecision：紧急支援请求的四问决策（紧急度/不可替代度/义务/预算）→四档输出？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-857：手写 supportDecision：紧急支援请求的四问决策（紧急度/不可替代度/义务/预算）→四档输出

**需求与边界**：
- 实现 supportDecision(req, mine)。
- 边界要求：① req 含 { urgency, alternatives: [] , askedBy }；mine 含 { deadlineFlexibility, budgetLeft }（SOFT-725 互助预算余额）；② 四问评分→四档输出：全支援（真紧急+唯一能+预算内）/部分支援（方案+1h）/延迟（给确定时间）/拒绝（超预算非紧急+替代路径 SOFT-564）；③ 规划失败型请求（非真危机）降档处理（SOFT-558 区分）；④ 支援记账条目输出（SOFT-558）。

**答**：
```javascript
function supportDecision(req, mine) {
  const real = req.urgency === 'crisis' && !req.selfInflicted; // 规划失败降档
  const unique = req.alternatives.length === 0;   // 唯一能救
  const free = mine.deadlineFlexibility !== 'hard';
  const inBudget = mine.budgetLeft > 0;
  let mode, detail;
  if (real && unique && free) { mode = '全支援';
    detail = '放下手上事（当前任务deadline需已协调——SOFT-586同步）'; }
  else if (real && inBudget) { mode = '部分支援';
    detail = '给方案+远程1小时（性价比模式）'; }
  else if (real) { mode = '延迟支援';
    detail = `明早10点我来（给确定性——SOFT-558）`; }
  else { mode = '拒绝';
    detail = '礼貌拒绝+替代路径（SOFT-564话术）'; }
  return { mode, detail,
    ledger: { helpedBy: 'me', to: req.askedBy,
      cost: mode === '全支援' ? '4h' : '1h',
      date: new Date().toISOString().slice(0, 10) },  // 记账SOFT-558
    note: real ? '' : '规划失败型请求——非真危机，降档处理（SOFT-558）' };
}
```

**评分点**:
- 四问决策→四档输出（SOFT-849 框架工具化）。
- 规划失败型降档（真危机与自造紧急的区分）。
- 支援记账输出（互惠与信用账本落地 SOFT-558）。

