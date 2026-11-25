---
title: [NODE-1008] 笔试题——实现 SLA 知识库检索（SLA 案例/runbook 查询）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1008：手写 SLA 检索

**需求与边界**：
- 需求：SLA 知识检索（SCN-ENG-332/OPS-248）——① SLA 案例检索（SCN-OPS-329）；② runbook 检索（SCN-OPS-851）；③ superseded 降权（SCN-ENG-332）；④ 零命中沉淀（SCN-OPS-248）。
- 边界：① 标题加权（SCN-ENG-332）；② 零命中（SCN-ENG-332）；③ 检索集成（CLI/IM——SCN-ENG-332）。

**答**：
```javascript
function slaHow(query) {
  const terms = query.toLowerCase().split(/\s+/);
  const results = [...slaCases(), ...slaRunbooks()]
    .map(doc => ({ doc, score: terms.reduce((s, t) =>
      s + (doc.title.includes(t) ? 3 : 0) + (doc.body.includes(t) ? 1 : 0), 0),   // SCN-ENG-332
      note: doc.supersededBy ? `已被 ${doc.supersededBy} 取代` : null }))
    .filter(r => r.score > 0).sort((a, b) => b.score - a.score).slice(0, 5);
  return results.length ? results : { hint: '零命中——SLA 违约后建议沉淀案例（SCN-OPS-248）' };
}
```

**评分点**:
- SLA 案例 + runbook 检索（SCN-OPS-329/851）。
- superseded 降权 + 零命中（SCN-ENG-332）。
- 沉淀建议（SCN-OPS-248）。
