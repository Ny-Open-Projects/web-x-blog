---
title: [NODE-933] 笔试题——实现回滚数据审计（多维回滚的留痕校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-933：手写回滚审计

**需求与边界**：
- 需求：回滚审计（SCN-OPS-220/933）——① 回滚全链留痕（入口/数据/配置/通知——SCN-NODE-926 四维）；② 留痕完整性校验（SCN-OPS-309 要素）；③ 回滚与事故关联（SCN-OPS-248 档案）；④ 审计的检索（SCN-NODE-775）。
- 边界：① 留痕的 append-only（SCN-NODE-775）；② 审计的哈希链（SCN-NODE-775）；③ 审计的消费（复盘——SCN-OPS-248）。

**答**：
```javascript
async function rollbackAuditVerify(releaseId) {
  const chain = auditChain(releaseId);                 // 回滚链留痕（SCN-NODE-926 四维）
  const required = ['entry-switch', 'data-verify', 'config-rollback', 'notify', 'metric-recovery'];
  const missing = required.filter(step => !chain.some(e => e.action === step));   // 要素校验（SCN-OPS-309）
  const intact = await verifyChainHash(chain);         // 哈希链（SCN-NODE-775）
  return { missing, intact,
    pass: !missing.length && intact,
    link: releaseArchive(releaseId).link };            // 事故关联（SCN-OPS-248）
}
```

**评分点**:
- 回滚链五步留痕校验（SCN-NODE-926）。
- 哈希链完整性（SCN-NODE-775）。
- 事故关联（SCN-OPS-248）。
- 检索（SCN-NODE-775）。
