---
title: [NODE-889] 笔试题——实现连接泄漏自动修复（强制回收 + 告警）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-889：手写泄漏修复

**需求与边界**：
- 需求：连接泄漏（SCN-NODE-726）——① 泄漏检测（SCN-NODE-726 借出跟踪）；② 自动强制回收（超时连接——SCN-NODE-726 leakCheck）；③ 回滚未完成事务（连接回收前——事务回滚，SCN-NODE-749）；④ 泄漏根因修复闭环（泄漏点告警 → 修复——SCN-NODE-726）。
- 边界：① 强制回收的风险（事务回滚——数据一致性；SCN-OPS-277）；② 泄漏频率监控（SCN-NODE-726）；③ 回收的审计（SCN-OPS-220）。

**答**：
```javascript
setInterval(async () => {
  for (const [conn, meta] of pool.leased) {
    if (Date.now() - meta.since > 30_000) {            // 泄漏（SCN-NODE-726）
      await pool.forceRollback(conn);                  // 回滚未完成事务（SCN-NODE-749 语义）
      pool.release(conn);                              // 强制回收
      alert({ type: 'CONN_LEAK_RECOVERED', stack: meta.stack,   // 根因（SCN-NODE-726）
        heldMs: Date.now() - meta.since });
      audit({ action: 'conn-force-release', stack: meta.stack });   // 审计（SCN-OPS-220）
    }
  }
}, 10_000);
```

**评分点**:
- 强制回收前回滚事务（数据一致性——SCN-NODE-749）。
- 泄漏根因栈（SCN-NODE-726 借出跟踪）。
- 回收审计（SCN-OPS-220）。
- 泄漏频率监控（SCN-NODE-726）。
