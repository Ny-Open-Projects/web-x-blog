---
title: [SOFT-883] 手写 interviewLog：面试问题全集记录、四层收获分类、三库更新（题库/话术库/情报库）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-883：手写 interviewLog：面试问题全集记录、四层收获分类、三库更新（题库/话术库/情报库）

**需求与边界**：
- 实现 InterviewLog：record(session)/classify()/syncLibs()。
- 边界要求：① session 记录 { company, round, questions: [{q, myAnswer, outcome}], notes }（1h 内录入约束提示）；② classify：问题分类（知识盲区/表达问题/命中话术——盲区进学习计划、表达问题修正话术 SOFT-865 四层）；③ syncLibs：盲区→题库、表达修正→话术库、公司信息→情报库（三库联动 SOFT-865）；④ 重复盲区计数（同题出现 ≥2 次标 HIGH_PRIORITY——SOFT-866 频率驱动）。

**答**：
```javascript
class InterviewLog {
  constructor() { this.sessions = []; this.blindspots = {}; }
  record(session) {
    if (!session.questions?.length)
      throw new Error('问题全集必须记录（1h内趁鲜活 SOFT-865）');
    this.sessions.push(session);
  }
  classify(session) {
    const out = { knowledge: [], expression: [], hit: [] };
    for (const q of session.questions) {
      if (q.outcome === 'failed') {
        out.knowledge.push(q.q);
        this.blindspots[q.q] = (this.blindspots[q.q] ?? 0) + 1;
        if (this.blindspots[q.q] >= 2)
          out.knowledge.push(`⚠️HIGH_PRIORITY：第${this.blindspots[q.q]}次出现（SOFT-866频率驱动）`);
      } else if (q.outcome === 'clumsy')
        out.expression.push(q.q);
      else out.hit.push(q.q);
    }
    return out;
  }
  syncLibs(session, classified) {
    return {
      questionBank: classified.knowledge
        .filter(k => !k.startsWith('⚠️')),
      scriptUpdates: classified.expression.map(q =>
        `话术修正：${q}（SOFT-867迭代机制）`),
      intelArchive: { company: session.company,
        round: session.round, notes: session.notes },
      note: '三库联动：题库/话术库/情报库（SOFT-865复利）' };
  }
}
```

**评分点**:
- 1h 内录入约束（趁记忆鲜活——SOFT-865 铁律工具化）。
- 四层收获分类自动化（知识/表达/命中——SOFT-865 分类落地）。
- 重复盲区 HIGH_PRIORITY 标注（频率驱动补齐 SOFT-866）。
- 三库同步（题库/话术库/情报库联动复利）。

