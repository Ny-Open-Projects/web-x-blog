---
title: [NODE-1019] 笔试题——实现 SLA 合规变更审计（合规链留痕）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1019：手写合规审计

**需求与边界**：
- 需求：合规变更审计（SCN-SLA-1005/1019）——① 合规变更链（审查/审批/通知/归档——SCN-SLA-1005 四步）；② 链完整性（SCN-OPS-309 要素）；③ 哈希链（SCN-NODE-775）；④ 链的消费（SCN-OPS-248）。
- 边界：① 四步链（SCN-SLA-1005）；② 哈希链（SCN-NODE-775）；③ 消费（SCN-OPS-248）。

**答**：
```javascript
async function complianceChainVerify(consumer) {
  const chain = complianceChangeChain(consumer);       // 四步链（SCN-SLA-1005）
  const required = ['compliance-review', 'approval', 'notify', 'archive'];
  const missing = required.filter(s => !chain.some(e => e.step === s));   // 要素（SCN-OPS-309）
  const hashOk = await verifyChainHash(chain);         // 哈希链（SCN-NODE-775）
  return { pass: !missing.length && hashOk, missing, archive: link(consumer) };   // SCN-OPS-248
}
```

**评分点**:
- 四步链校验（SCN-SLA-1005）。
- 要素 + 哈希链（SCN-OPS-309/NODE-775）。
- 消费（SCN-OPS-248）。
