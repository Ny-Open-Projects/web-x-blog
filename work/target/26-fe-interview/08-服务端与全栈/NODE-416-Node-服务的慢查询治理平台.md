---
title: [NODE-416] Node 服务的慢查询治理平台化如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-416：慢查询治理平台化
**答**:
- 从"人工看日志"到"平台化闭环"：采集（慢查询日志/DB 侧 pg_stat_statements）→ 指纹聚合（参数归一化合并同类）→ 归因（执行计划快照 + 表结构 + 索引建议）→ 分派（按 service/owner 自动开单）→ 修复追踪（修复前后耗时对比）→ 回归验证。
- 平台核心数据：慢查询 TopN（按总耗时 = 次数 × 单次耗时排序，总耗时排序才能找到真正大头）、趋势（新进榜指纹告警——新发布引入的慢查询当天发现）。
- 索引管理：冗余索引/未使用索引识别（drop 降低写放大）、索引使用率统计、索引变更走 DDL 评审（在线执行 NODE-335）。
- 量化门禁：新发布引入慢查询（总耗时增量超阈值）阻断发布；存量 Top10 每季度清零目标。
- 与代码联动：慢查询指纹关联到代码位置（ORM 调用点埋点关联），修复定位到具体函数。
```javascript
// 指纹关联代码位置
db.on('query', q => { const t0 = Date.now();
  q.on('end', () => { const ms = Date.now() - t0;
    if (ms > 500) slowLog.write({ fingerprint: norm(q.sql), ms,
      codeAt: captureStackTrace(2)[0] }); });                  // ORM 调用点堆栈
});
```
