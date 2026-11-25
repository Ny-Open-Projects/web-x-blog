---
title: [NODE-764] 笔试题——实现 Redis 大 key 渐进治理任务（扫描+删除+报告）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-764：手写大 key 任务

**需求与边界**：
- 需求：大 key 治理任务（SCN-NODE-747）——① 定时扫描（SCAN + MEMORY USAGE 采样——低峰）；② 渐进删除队列（低峰窗口执行——限速）；③ 治理报告（大 key 清单/已处理/剩余——趋势）；④ 预防规则（应用层写入上限——schema 拒绝，SCN-NODE-689）。
- 边界：① 扫描与删除的窗口隔离（扫描白天、删除凌晨——影响窗口分离）；② 删除的进度断点（分批删除中断续删）；③ 治理告警（大 key 数量趋势——劣化信号）。

**答**：
```javascript
async function bigKeyGovernance() {
  const big = await scanBigKeys(redis, { thresholdMB: 1 });   // SCN-NODE-747 扫描
  report({ total: big.length, top: big.slice(0, 10),
    trend: vsLastWeek(big.length) });                  // 治理报告（趋势——SCN-NODE-689）
  const deletable = big.filter(b => !b.protected);
  for (const b of deletable) {
    if (!inLowPeakWindow()) break;                     // 低峰窗口才删（影响窗口隔离）
    await resumeGradualDelete(b.key, { batchSize: 100, throttleMs: 50 });   // 断点续删
  }
  // 预防：应用层写入上限（Redis 值 schema）
  setWriteGuard({ maxHashElements: 10000, maxValueMB: 1 });   // 超限拒绝（预防优于治理）
}
```

**评分点**:
- 扫描/删除窗口隔离（低峰才删——影响窗口）。
- 断点续删（渐进删除中断恢复——SCN-NODE-747）。
- 治理报告趋势（劣化信号——SCN-NODE-689）。
- 写入预防规则（schema 上限——预防优于治理）。
