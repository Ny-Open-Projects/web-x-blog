---
title: [NODE-947] 笔试题——实现发布档案生成（多维留痕聚合）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-947：手写发布档案

**需求与边界**：
- 需求：发布档案（SCN-OPS-248/220）——① 多维留痕聚合（门禁/灰度/哨兵/回滚——SCN-OPS-220）；② 档案的不可变（SCN-NODE-775 append-only）；③ 档案的检索（SCN-OPS-248）；④ 档案的哈希链（SCN-NODE-775）。
- 边界：① 档案的完整性（SCN-OPS-309 要素）；② 档案的消费（复盘/审计——SCN-OPS-248）；③ 档案的保留期（SCN-FIN-625）。

**答**：
```javascript
async function releaseArchiveBuild(release) {
  const archive = {
    gates: releaseGatesLog(release.id),                // 门禁（SCN-OPS-859）
    gray: decisionChain(release.id),                   // 决策链（SCN-OPS-939）
    sentinel: sentinelLogs(release.id),                // 哨兵（SCN-NODE-798）
    rollback: rollbackAudit(release.id),               // 回滚（SCN-NODE-933）
    regression: releaseRegressionReport(release),      // 回归（SCN-NODE-897）
  };
  archive.hash = chainHash(archive);                   // 哈希链（SCN-NODE-775）
  await appendArchive(archive);                        // append-only（SCN-OPS-248）
  return { archive, retention: '30d' };                // 保留期（SCN-FIN-625）
}
```

**评分点**:
- 多维聚合（门禁/灰度/哨兵/回滚/回归——SCN-OPS-220）。
- append-only + 哈希链（SCN-NODE-775）。
- 检索消费（SCN-OPS-248）。
- 保留期（SCN-FIN-625）。
