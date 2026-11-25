---
title: [NODE-939] 笔试题——实现灰度决策审计链（决策序列完整性）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-939：手写审计链

**需求与边界**：
- 需求：决策审计链（SCN-OPS-273/939）——① 决策序列链（每次决策快照——SCN-NODE-937）；② 链完整性（决策序列无缺失——合法迁移序列，SCN-OPS-292）；③ 链验证（哈希链——SCN-NODE-775）；④ 链的消费（复盘/审计——SCN-OPS-248）。
- 边界：① 合法迁移序列（放量状态机——SCN-OPS-292）；② 链的 append-only（SCN-NODE-775）；③ 链的定期验证（SCN-NODE-775）。

**答**：
```javascript
async function decisionChainVerify(releaseId) {
  const chain = decisionChain(releaseId);              // 决策序列（SCN-NODE-937）
  const legal = chain.every((d, i) =>
    LEGAL_TRANSITIONS[chain[i - 1]?.action ?? 'INIT']?.includes(d.action));   // 合法迁移（SCN-OPS-292）
  const hashOk = await verifyChainHash(chain);         // 哈希链（SCN-NODE-775）
  return { legal, hashOk,
    pass: legal && hashOk,
    gaps: !legal ? chain.filter((d, i) => !legalTransition(chain[i - 1], d)) : [],   // 缺失定位
    archive: releaseArchive(releaseId) };              // 消费（SCN-OPS-248）
}
```

**评分点**:
- 合法迁移序列校验（SCN-OPS-292 状态机）。
- 哈希链验证（SCN-NODE-775）。
- 缺失定位（审计可行动）。
- 消费（SCN-OPS-248）。
