---
title: [NODE-1018] 笔试题——实现跨租户 SLA 知识共享（同租户层知识复用）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1018：手写知识共享

**需求与边界**：
- 需求：知识共享（SCN-SLA-1013/1018）——① 同层案例共享（SCN-SLA-1013 沉淀）；② 共享的脱敏（SCN-NODE-698）；③ 共享的消费（新租户 onboarding——SCN-联想-833）；④ 共享的度量（复用率——SCN-联想-886）。
- 边界：① 脱敏（SCN-NODE-698）；② 共享的范围（同层——SCN-SLA-992）；③ 消费（SCN-联想-833）。

**答**：
```javascript
async function shareTenantKnowledge(tier) {
  const cases = (await tenantSlaCases(tier)).map(c => desensitize(c));   // 脱敏共享（SCN-NODE-698）
  await publishToTier(cases, { scope: `tier:${tier}` });   // 同层共享（SCN-SLA-992）
  await linkToOnboarding(cases);                       // onboarding 消费（SCN-联想-833）
  const reuse = caseReuseRate(cases);                  // 复用率（SCN-联想-886）
  return { shared: cases.length, reuse };
}
```

**评分点**:
- 同层共享 + 脱敏（SCN-SLA-992/NODE-698）。
- onboarding 消费（SCN-联想-833）。
- 复用率度量（SCN-联想-886）。
