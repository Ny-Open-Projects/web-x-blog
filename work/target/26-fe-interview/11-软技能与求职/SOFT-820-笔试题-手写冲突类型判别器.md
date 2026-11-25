---
title: [SOFT-820] 手写 conflictClassify：冲突描述自动判型（任务/流程/人际）、处理路径路由、升级判定？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-820：手写 conflictClassify：冲突描述自动判型（任务/流程/人际）、处理路径路由、升级判定

**需求与边界**：
- 实现 conflictClassify(conflict, history)。
- 边界要求：① 三型判别：任务（含“方案/选型/技术”词）/流程（含“分工/接口/谁负责/排期”词）/人际（含“态度/尊重/情绪/人格”词）——多重命中按最高优先级（人际>流程>任务：人际需最先处理）；② 处理路径路由（SOFT-803 框架：任务→引导五步/流程→机制化/人际→降温修复）；③ 升级判定：history 显示同类冲突 ≥2 次（复发→机制补丁优先或第三方介入）；④ 未知描述兜底为任务型（数据化辩论最安全）。

**答**：
```javascript
const RULES = [
  { type: 'interpersonal', re: /态度|尊重|情绪|人格|针对我|看不起/,
    path: '人际→一对一降温修复（SOFT-805），公开场合冷却' },
  { type: 'process', re: /分工|接口|谁负责|排期|职责|流程/,
    path: '流程→机制化：RACI/接口契约（SOFT-550/544）' },
  { type: 'task', re: /方案|选型|技术|架构|实现/,
    path: '任务→引导五步：共识/分歧/数据/选项/留痕（SOFT-804）' },
];
function conflictClassify(conflict, history = []) {
  const hits = RULES.filter(r => r.re.test(conflict.text));
  const type = hits.length
    ? hits[0].type                 // 人际>流程>任务优先级
    : 'task';                      // 兜底：数据化辩论最安全
  const rule = RULES.find(r => r.type === type) ?? RULES[2];
  const recurrence = history.filter(h => h.type === type).length;
  return {
    type, path: rule.path,
    recurrence,
    escalation: recurrence >= 2
      ? { action: type === 'task'
          ? '复发任务冲突：补机制而非再辩论（SOFT-811）'
          : '复发：第三方介入/机制补丁（SOFT-805升级线）' }
      : null,
    note: '多重命中按人际优先（需最先处理）' };
}
```

**评分点**:
- 三型判别规则+优先级（人际>流程>任务——需最先处理的优先）。
- 复发检测与升级路由（≥2 次同型冲突→机制补丁或第三方）。
- 未命中兜底为任务型（数据化辩论最安全的默认）。

