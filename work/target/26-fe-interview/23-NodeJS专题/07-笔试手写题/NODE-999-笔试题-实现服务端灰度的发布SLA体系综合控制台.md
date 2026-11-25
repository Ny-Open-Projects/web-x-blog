---
title: [NODE-999] 笔试题——实现 SLA 体系综合控制台（SLA 收束）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-999：手写 SLA 控制台

**需求与边界**：
- 需求：SLA 控制台（SCN-SLA-999）——① SLA 看板（SCN-OPS-239/714）；② 违约跟踪（SCN-SLA-974）；③ 趋势预警（SCN-SLA-996）；④ 合规审计（SCN-SLA-997）；⑤ 知识沉淀（SCN-SLA-998）——五区聚合。
- 边界：① 各区复用前文（编号引用）；② 控制台只聚合（SCN-OPS-333）；③ SLA 能力地图（951~998）。

**答**：
```javascript
function slaConsole(consumer) {
  return {
    board: notifySlaBoard(month()),                    // 看板（SCN-OPS-968）
    breaches: breachTracker(consumer),                 // 违约（SCN-SLA-974）
    forecast: slaTrendForecast(consumer.sla),          // 趋势（SCN-SLA-996）
    audit: slaAudit(),                                 // 合规（SCN-SLA-997）
    knowledge: slaKnowledgeLoop(breaches),             // 沉淀（SCN-SLA-998）
    map: SLA_MAP,                                      // 能力地图
  };
}
const SLA_MAP = {   // 951~998 索引
  advice: ['951-advice', '970-sla-guard', '976-boundary', '977-human'],
  governance: ['952-approval', '955-tracking', '959-prefs', '964-tiers', '968-board'],
  data: ['982-report', '987-alignment', '988-replication', '992-tiers', '995-report'],
  loop: ['926-rollback', '944-freeze', '950-knowledge', '997-audit', '999-console'],
};
```

**评分点**:
- 五区聚合（看板/违约/趋势/合规/沉淀）全链引用。
- 只聚合不决策（SCN-OPS-333）。
- SLA 能力地图收束（951~998）。
