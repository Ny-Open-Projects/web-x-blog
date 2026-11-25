---
title: [1048] 人工审批积压怎么办，介入队列怎么设计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 人机协同]
type: 面试题
---

## 1048：人工审批积压怎么办，介入队列怎么设计

**答**：
- 介入队列设计：按风险与时效分级（高危实时推送、普通 4h SLA、低危批量处理），队列有「老化自动升级」（4h 未处理自动升级到上级审批人），超 SLA 自动按预设策略处理（默认拒绝）。
- 审批人负载均衡：同类审批按「在线状态 + 处理中数量」分发，避免全堆给一个人；缺席自动转移。
- 上下文完整：推给审批人的不只是请求，还有「Agent 计划 + 依据 + 历史 3 轮摘要」，减少审批人来回查询的成本——审批延迟大头是「信息不全导致的犹豫」。
- 追问钩子：审批人一直不在线业务就停了？——降级策略预定义：该类操作是否允许「超时自动放行」取决于风险等级，高危永不自动放行，中危可配「双人其中一人批即生效」。

```ts
const queue = new PriorityApproval({
  levels: { high: { sla: '15m', push: true, timeout: 'reject' },
            mid: { sla: '4h', timeout: 'reject' },
            low: { sla: '24h', batch: true } },
  aging: 'escalate',            // 老化自动升级
  assign: loadBalancedByOnline, // 在线负载均衡
});
```
