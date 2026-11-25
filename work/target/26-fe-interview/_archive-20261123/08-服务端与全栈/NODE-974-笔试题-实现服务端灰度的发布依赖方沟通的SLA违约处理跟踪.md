---
title: [NODE-974] 笔试题——实现 SLA 违约处理跟踪（违约→处置→闭环）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-974：手写违约跟踪

**需求与边界**：
- 需求：违约跟踪（SCN-SLA-963/OPS-227）——① 违约工单（SCN-SLA-963）；② 处置跟踪（补偿/改进——SCN-OPS-227 善后）；③ 闭环校验（处置完成——SCN-OPS-227）；④ 违约的趋势（SCN-SLA-708）。
- 边界：① 违约的分级（P0/P1——SCN-OPS-891）；② 处置的时效（SCN-OPS-210）；③ 闭环的审计（SCN-OPS-273）。

**答**：
```javascript
async function breachTracker(breach) {
  const ticket = await createTicket({ breach, level: breach.slaTier, due: slaDue(breach) });   // 工单（SCN-OPS-210 时效）
  ticket.onStep(async (step) => {
    await execute(step);                               // 处置（SCN-OPS-227）
    if (ticket.allStepsDone() && verified(breach)) {   // 闭环校验（SCN-OPS-227）
      await closeTicket(ticket); audit({ breach: breach.id, closed: true });
    }
  });
}
```

**评分点**:
- 违约工单 + 时效（SCN-SLA-963/210）。
- 闭环校验（SCN-OPS-227）。
- 趋势（SCN-SLA-708）。
