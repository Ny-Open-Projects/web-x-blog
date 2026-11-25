---
title: [NODE-945] 笔试题——实现多服务决策审计链验证（跨服务决策链）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-945：手写多服务审计链

**需求与边界**：
- 需求：多服务决策链（SCN-OPS-939/924）——① 跨服务决策链（协同放量的决策序列——SCN-OPS-924）；② 链完整性（合法迁移跨服务——SCN-OPS-292）；③ 哈希链（SCN-NODE-775）；④ 链的消费（SCN-OPS-248）。
- 边界：① 跨服务的决策序列（协同放量循环——SCN-NODE-924）；② 链的快照（SCN-OPS-937）；③ 验证的周期（SCN-NODE-775）。

**答**：
```javascript
async function multiServiceChainVerify(plans) {
  const chains = plans.map(p => decisionChain(p.id));   // 各服务链（SCN-OPS-937）
  const crossService = crossServiceDecisions(plans);   // 协同决策（SCN-OPS-924）
  const legal = chains.every(c => legalTransitions(c)) && crossService.every(legal);   // 合法迁移（SCN-OPS-292）
  const hashOk = await verifyChainHash([...chains.flat(), ...crossService]);   // 哈希（SCN-NODE-775）
  return { legal, hashOk, pass: legal && hashOk,
    archive: plans.map(p => releaseArchive(p.id)) };   // 消费（SCN-OPS-248）
}
```

**评分点**:
- 跨服务决策链（SCN-OPS-924）。
- 合法迁移 + 哈希链（SCN-OPS-292/NODE-775）。
- 消费（SCN-OPS-248）。
