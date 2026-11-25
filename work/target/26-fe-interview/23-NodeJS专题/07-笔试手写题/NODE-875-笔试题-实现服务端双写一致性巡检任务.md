---
title: [NODE-875] 笔试题——实现双写一致性巡检任务（定时 + 分片 + 趋势）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-875：手写一致性巡检

**需求与边界**：
- 需求：双写巡检（SCN-NODE-793 常态化）——① 定时分片巡检（每小时分片——SCN-NODE-755 分片）；② 巡检幂等（断点——SCN-NODE-755）；③ 趋势看板（漂移率趋势——SCN-NODE-872）；④ 巡检发现 → 补偿联动（SCN-NODE-868）。
- 边界：① 巡检与业务隔离（低峰——SCN-NODE-764 窗口）；② 巡检深度（抽样 vs 全量——数据量决定）；③ 多表巡检的优先级（核心表优先——风险排序）。

**答**：
```javascript
cron('0 */2 * * *', async () => {                      // 定时分片（SCN-NODE-755）
  const tables = PRIORITY_TABLES.filter(t => !drifting(t));   // 核心表优先
  for (const t of tables.slice(0, 3)) {                // 每轮 3 表（低峰隔离——SCN-NODE-764）
    const r = await dualWriteDriftCheck(t, { sampleRate: tableSize(t) > 1e6 ? 0.01 : 1 });   // 深度自适应
    if (r.drifted) {
      const causes = classifyDrift(r.samples);         // SCN-NODE-872 归因
      await compensateAuto(causes.autoFixable);        // 补偿联动（SCN-NODE-868）
      if (!causes.autoFixable) alert({ type: 'DRIFT_MANUAL', table: t });
      trend.record(t, r.rate);                         // 趋势（SCN-NODE-872）
    }
  }
});
```

**评分点**:
- 定时分片 + 低峰隔离（SCN-NODE-755/764）。
- 深度自适应（抽样 vs 全量——数据量决定）。
- 归因 + 补偿联动（SCN-NODE-872/868）。
- 趋势看板（SCN-NODE-872）。
