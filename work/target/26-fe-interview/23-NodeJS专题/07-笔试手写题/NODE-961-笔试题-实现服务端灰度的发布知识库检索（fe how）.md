---
title: [NODE-961] 笔试题——实现发布知识库检索（fe how 发布版）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-961：手写发布检索

**需求与边界**：
- 需求：发布知识检索（SCN-ENG-332/951）——① 发布案例检索（标签+模块——SCN-OPS-329）；② runbook 检索（SCN-OPS-851）；③ 结果的摘要行（SCN-ENG-332）；④ 零命中建议（SCN-ENG-332）。
- 边界：① 标签权重（SCN-OPS-329）；② superseded 降权（SCN-ENG-332）；③ 检索的集成（CLI/IM——SCN-ENG-332）。

**答**：
```javascript
function feHowRelease(query) {
  const terms = query.toLowerCase().split(/\s+/);
  const results = [...releaseCases(), ...runbooks()]
    .map(doc => ({
      doc, score: terms.reduce((s, t) =>
        s + (doc.title.includes(t) ? 3 : 0) + (doc.body.includes(t) ? 1 : 0), 0),   // SCN-ENG-332
      note: doc.supersededBy ? `已被 ${doc.supersededBy} 取代` : null,   // 降权（SCN-ENG-332）
    }))
    .filter(r => r.score > 0).sort((a, b) => b.score - a.score).slice(0, 5);
  return results.length ? results : { hint: '零命中——发布后建议沉淀案例（SCN-OPS-248）' };   // 零命中
}
```

**评分点**:
- 发布案例 + runbook 检索（SCN-OPS-329/851）。
- 标题加权 + superseded 降权（SCN-ENG-332）。
- 零命中沉淀建议（SCN-OPS-248）。
