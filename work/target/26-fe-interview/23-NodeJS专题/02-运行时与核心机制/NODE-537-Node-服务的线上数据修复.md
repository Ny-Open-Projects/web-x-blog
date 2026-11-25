---
title: [NODE-537] Node 服务的线上数据修复（批量修正的安全流程）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-537：线上数据修复流程
**答**:
- 场景：程序 bug 造成批量脏数据（状态错误/金额错误）——修复是高危操作（修错 = 二次事故）。安全流程：修复申请（范围声明：影响行数/筛选条件/修复逻辑——SQL 或脚本）、审核（双人：提出者 + DBA/owner——修复逻辑 review）、预演（dry-run：只查不改，输出将影响的行清单——人工抽查确认）、执行（分批 + 限速 + 可中断）、验证（修复后抽检 + 业务指标确认）、回滚预案（修复前备份受影响行——可还原）。
- 工具化：修复平台（申请→审批→dry-run→执行→报告一站式——NODE-451 运维工具的专项）、修复脚本模板（分批循环/进度记录/失败暂停——防一次性大事务锁表 NODE-335）。
- 红线：禁止直接在生产手写 UPDATE（必须走平台——操作留痕可回滚）、修复期间监控关注（修复流量对在线服务的影响——只读副本执行优先）。
- 复盘联动：数据修复事件归因到 bug（修复是止血——根因修复单独跟踪 ARC-407）、同类 bug 的批量影响扫描（同模式数据全量排查——是否还有没发现的脏数据）。
```javascript
// 修复平台执行器
async function runFix(plan) {                                    // plan: {filter, fix, batchSize}
  await plan.dryRun();                                           // 影响清单人工确认
  await backup(plan.filter);                                     // 备份可回滚
  for (const batch of plan.batches(500)) {                       // 分批
    await batch.apply(); await pause(100);                       // 限速
    if (aborted()) break;                                        // 可中断
  }
  await verify(plan);                                            // 抽检验证
}
```
