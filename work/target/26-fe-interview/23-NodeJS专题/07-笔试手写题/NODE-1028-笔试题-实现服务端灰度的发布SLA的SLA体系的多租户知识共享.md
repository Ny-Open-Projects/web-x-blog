---
title: [NODE-1028] 笔试题——实现租户 SLA 知识共享（跨租户脱敏共享）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
duplicate_of: NODE-1018   # 与 NODE-1018 语义重复（相似度 0.65），保留那条即可
---

## NODE-1028：手写知识共享

**需求与边界**：
- 需求：知识共享（SCN-SLA-1013/1018）——① 同层共享（SCN-SLA-1013）；② 脱敏（SCN-NODE-698）；③ 消费（SCN-联想-833）；④ 复用率（SCN-联想-886）。
- 边界：① 脱敏（SCN-NODE-698）；② 消费（SCN-联想-833）；③ 复用率（SCN-联想-886）。

**答**：
```javascript
async function shareSlaKnowledge(tier) {               // SCN-SLA-1013 复用
  const cases = (await tenantSlaCases(tier)).map(desensitize);   // 脱敏（SCN-NODE-698）
  await publishToTier(cases, { scope: `tier:${tier}` });   // 同层（SCN-SLA-992）
  await linkToOnboarding(cases);                       // 消费（SCN-联想-833）
  return { shared: cases.length, reuse: caseReuseRate(cases) };   // 复用率（SCN-联想-886）
}
```

**评分点**:
- 同层共享 + 脱敏（SCN-SLA-1013/992）。
- onboarding 消费（SCN-联想-833）。
- 复用率（SCN-联想-886）。
