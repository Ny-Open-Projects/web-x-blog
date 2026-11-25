---
title: [NODE-1031] 笔试题——实现租户 SLA 知识检索（分层检索）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1031：手写租户检索

**需求与边界**：
- 需求：租户检索（SCN-SLA-1008/1013）——① 分层检索（SCN-SLA-1013）；② 脱敏（SCN-NODE-698）；③ 零命中沉淀（SCN-OPS-248）；④ 检索集成（SCN-ENG-332）。
- 边界：① 分层（SCN-SLA-1013）；② 脱敏（SCN-NODE-698）；③ 零命中（SCN-OPS-248）。

**答**：
```javascript
function tenantSlaHow(query, tier) {                   // 分层检索（SCN-SLA-1013）
  const terms = query.toLowerCase().split(/\s+/);
  const results = tenantSlaCases(tier)                 // 分层（SCN-SLA-1013）
    .map(desensitize)                                  // 脱敏（SCN-NODE-698）
    .map(doc => ({ doc, score: terms.reduce((s, t) =>
      s + (doc.title.includes(t) ? 3 : 0) + (doc.body.includes(t) ? 1 : 0), 0) }))
    .filter(r => r.score > 0).sort((a, b) => b.score - a.score).slice(0, 5);
  return results.length ? results : { hint: '零命中——沉淀租户案例（SCN-OPS-248）' };
}
```

**评分点**:
- 分层检索（SCN-SLA-1013）。
- 脱敏 + 零命中沉淀（SCN-NODE-698/OPS-248）。
