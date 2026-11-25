---
title: [NODE-382] Node 服务的对账体系（资金/库存/积分）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-382：对账体系设计
**答**:
- 定位：异步链路（MQ/saga/延迟任务）的最终安全网——任何"本地消息表/补偿"都可能因 bug 漏掉，对账发现漏网之鱼。
- 结构：数据准备（双方流水按日切片，注意时区与边界 ARC-481）→ 逐条比对（键匹配：金额/状态）→ 差异分类（单边：一方有另一方无 / 金额不一致 / 状态不一致）→ 处理（自动补偿：重发消息；或挂人工工单）。
- 实时对账 vs 批量对账：资金场景 T+1 批量对账（完整稳定）+ 实时对账（增量流比对，提前发现，减少损失窗口）双层。
- 差异治理：差异根因分类统计（重复消费/丢消息/代码 bug/边界时间），Top 根因进修复队列；对账自身要可重跑（幂等，同一天重跑不产生重复补偿）。
- 观测：差异率趋势（目标趋近 0）、差异处理时长（发现到修复）；对账任务失败告警（安全网自己挂了最危险）。
```javascript
async function reconcile(day) {
  const ours = await db.query('select * from pay_flow where day=$1', [day]);   // 本方流水
  const theirs = await channel.downloadFlow(day);                              // 渠道流水
  const { matched, oursOnly, theirsOnly } = diffByKey(ours, theirs, 'tradeNo');
  for (const t of theirsOnly) await compensate(t);              // 单边：渠道有我们没有 → 补单
  for (const o of oursOnly) await openTicket(o, 'ours-only');   // 我方有渠道无 → 人工核实
  return { day, diffRate: (oursOnly.length + theirsOnly.length) / ours.length };
}
```
