---
title: [NODE-585] Node 服务的 Excel 导入服务端（解析/校验/入库）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-585：Excel 导入服务端
**答**:
- 导入链路（ARC-490 服务端实现）：解析（流式解析大文件 NODE-342——内存安全）、校验（三级：格式/业务/依赖——错误明细结构化）、预检结果（错误报告：行/列/原因/修复建议——可下载标注版）、确认入库（异步批量——任务进度推送 ARC-583）、回滚（批次撤销 ARC-575）。
- 校验实现：行级校验并行（批量预检接口——DB 唯一性/依赖存在性批量查）、错误收集上限（错误太多提前终止——全量错误报告生成策略）、警告与错误分级（错误阻断/警告放行——用户确认警告项）。
- 入库一致性：批量插入事务分段（每批一个事务——失败从批次断点续跑）、导入幂等（批次+行唯一键——重复导入去重）、导入限流（大文件资源保护）。
- 模板联动：模板生成与解析同一 schema（ARC-575——字段映射一致性）。
- 观测：导入成功率/失败 Top 原因/平均处理时长——模板优化依据。
```javascript
// 导入流水线
async function runImport(task) {
  const rows = await streamExcel(task.file);                     // 流式解析
  const errors = [];
  for (const batch of chunk(rows, 500)) {
    const errs = await validateBatch(batch);                     // 业务/依赖批量校验
    errors.push(...errs);
    if (errors.length > LIMIT) break;                            // 错误上限提前终止
    if (!errs.some(fatal)) await insertBatch(batch, task.batchId); // 分批入库（幂等键）
  }
  return report(errors);                                         // 错误标注报告
}
```
