---
title: [NODE-682] 定时对账系统（T+1 对账任务）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-682：对账系统怎么做？
**答**：
- 对账流程：拉取两侧数据（我方 DB + 渠道文件——下载/解析渠道对账文件）→ 匹配（ orderId 多重匹配——SCN-FIN-552 对比器）→ 差异分类（长短款/金额/状态——SCN-FIN-552 分类）→ 差异工单（进处理池——人工/自动补偿）。
- 可靠性：对账任务幂等（重跑一致——SCN-NODE-655）、断点续跑（大数据量分片——按小时分片对账）、渠道文件延迟的处理（T+2 补对——对账有重试日历）。
- 自动补偿：可自动处理的差异（单边补单——幂等补偿）自动跑；模糊差异进人工池——自动化与人工的边界显式（SCN-OPS-259 自愈边界同源）。
- 监控：差异率看板（趋势异常告警——差异率突增 = 渠道或我方故障信号）。
- 追问钩子：为什么对账要「按小时分片」而不是整天一把算——全天数据一把算：内存峰值大（百万行）、失败重跑成本高（整天重来）、无法增量；分片（每小时独立对账 + 汇总）让失败只重跑该小时，且可以边跑边告警——分片是对账的工程化基础，与「差异率实时可见」互补。

```javascript
async function reconcile(hours) {
  for (const hour of hours) {                          // 分片：按小时
    const mine = await db.ordersByHour(hour);          // 我方
    const theirs = await parseChannelFile(hour);       // 渠道文件
    const { diff } = reconcilePair(mine, theirs);      // 多重匹配（SCN-FIN-552）
    await enqueueDiffTickets(diff, { auto: classifyAuto(diff) });   // 差异工单
    markHourDone(hour);                                // 断点记录（幂等）
  }
}
```
