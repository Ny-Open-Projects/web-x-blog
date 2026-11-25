---
title: [NODE-967] 笔试题——实现沟通记录合规保留（保留期+销毁审批）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-967：手写合规保留

**需求与边界**：
- 需求：合规保留（SCN-FIN-625/967）——① 保留期倒计时（SCN-FIN-625）；② 销毁审批（合规审批——SCN-FIN-625）；③ 销毁的执行（幂等——SCN-NODE-655）；④ 保留的审计（SCN-OPS-220）。
- 边界：① 保留期的分级（SCN-FIN-625）；② 销毁的白名单（SCN-FIN-625）；③ 销毁的验证（SCN-OPS-331 对账）。

**答**：
```javascript
cron('0 3 * * *', async () => {
  const due = await retentionDue();                    // 保留期倒计时（SCN-FIN-625）
  for (const r of due) {
    const approved = await complianceApproval(r);      // 销毁审批（SCN-FIN-625）
    if (!approved) { defer(r); continue; }
    await destroy(r);                                  // 幂等销毁（SCN-NODE-655）
    audit({ destroyed: r.id, by: approved.by });       // 审计（SCN-OPS-220）
  }
});
```

**评分点**:
- 保留期倒计时 + 销毁审批（SCN-FIN-625）。
- 幂等销毁（SCN-NODE-655）。
- 审计（SCN-OPS-220）。
