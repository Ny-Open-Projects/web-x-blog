---
title: [SOFT-695] 手写 mockCollector：预答辩问题记录、致命度分级、清零状态跟踪、答案卡关联？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-695：手写 mockCollector：预答辩问题记录、致命度分级、清零状态跟踪、答案卡关联

**需求与边界**：
- 实现 MockCollector：record(q, asker)/classify()/cleared()。
- 边界要求：① 问题记录含场次与提问者；② 致命度分级（材料穿帮=2/答不上=1/细节=0——按"是否影响通过"标准）；③ cleared()：所有致命度 ≥1 的问题都有答案卡才算清零；④ 重复问题合并计数（多场都被问=高频必背）；⑤ 输出按致命度排序清单。

**答**：
```javascript
class MockCollector {
  constructor() { this.qs = new Map(); }
  record(q, asker, session) {
    const k = normalize(q);                          // 归一化合并
    const rec = this.qs.get(k) ?? { q, askers: [], sessions: [],
      fatal: null, answered: false };
    rec.askers.push(asker); rec.sessions.push(session);
    rec.freq = rec.sessions.length;
    this.qs.set(k, rec);
    return rec;
  }
  classify(q, verdict) {                             // verdict: 2|1|0
    const rec = this.qs.get(normalize(q));
    rec.fatal = Math.max(rec.fatal ?? 0, verdict);
  }
  markAnswered(q, cardNo) {
    this.qs.get(normalize(q)).answered = cardNo;
  }
  cleared() {
    const open = [...this.qs.values()]
      .filter(r => (r.fatal ?? 0) >= 1 && !r.answered);
    return { cleared: open.length === 0, open: open.length,
      list: open.sort((a, b) => (b.fatal ?? 0) - (a.fatal ?? 0)) };
  }
  highFreq() {                                       // 多场都被问=必背
    return [...this.qs.values()].filter(r => r.freq >= 2);
  }
}
```

**评分点**:
- 致命度三级（穿帮>答不上>细节）排序清零（致命问题清单闭环）。
- 跨场合并计数（高频问题浮出为必背）。
- cleared 判定只看致命级（细节问题不阻塞上场）。

