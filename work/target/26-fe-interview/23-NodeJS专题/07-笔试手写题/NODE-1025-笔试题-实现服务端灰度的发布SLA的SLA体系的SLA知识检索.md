---
title: [NODE-1025] 笔试题——实现 SLA 知识检索（SLA 版 fe how）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1025：手写 SLA 检索

**需求与边界**：
- 需求：SLA 检索（SCN-SLA-1008/1025）——① SLA 案例/runbook 检索（SCN-SLA-1008）；② superseded 降权（SCN-ENG-332）；③ 零命中沉淀（SCN-OPS-248）；④ 检索的集成（SCN-ENG-332）。
- 边界：① 标题加权（SCN-ENG-332）；② 零命中（SCN-ENG-332）；③ 集成（SCN-ENG-332）。

**答**：
```javascript
function slaHow(query) {                               // SCN-SLA-1008 复用
  const terms = query.toLowerCase().split(/\s+/);
  const results = [...slaCases(), ...slaRunbooks()]
    .map(doc => ({ doc, score: terms.reduce((s, t) =>
      s + (doc.title.includes(t) ? 3 : 0) + (doc.body.includes(t) ? 1 : 0), 0) }))
    .filter(r => r.score > 0).sort((a, b) => b.score - a.score).slice(0, 5);
  return results.length ? results : { hint: '零命中——沉淀案例（SCN-OPS-248）' };
}
```

**评分点**:
- SLA 检索复用（SCN-SLA-1008）。
- 加权 + 零命中沉淀（SCN-ENG-332/OPS-248）。
