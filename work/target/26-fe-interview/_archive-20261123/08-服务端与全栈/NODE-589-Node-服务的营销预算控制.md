---
title: [NODE-589] Node 服务的营销预算控制（活动成本防超支）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-589：营销预算控制
**答**:
- 预算模型：活动预算（总预算/日预算——按维度：用户数/金额/发放量）、消耗跟踪（实时累计——券核销/积分发放/补贴金额消耗预算池）、超支行为（到量停止/降档（概率调低）/预警——策略配置）。
- 实现要点：预算池原子扣减（Redis/DB 原子——并发超发防护）、消耗回滚（退款/取消 → 预算返还——回滚幂等）、预算粒度（总池/分人群池/分渠道池——嵌套预算）、预算与库存关系（券库存独立于预算——双约束）。
- 预警与干预：消耗速率异常告警（烧钱过快——防羊毛/promote 配置错误）、人工干预（紧急降档/停止——操作留痕）、预算报表（活动成本实时看板——ROI 跟踪 ARC-584）。
- 一致性：预算扣减与发放事务一致性（预算先扣/发放失败回滚——同事务或补偿）、跨服务预算（券服务/积分服务共享预算池——统一预算服务）。
- 复盘：预算使用率/超支事件复盘（根因：配置错/羊毛——防护改进）。
```javascript
// 预算池扣减
async function consumeBudget(campaignId, cost) {
  const ok = await luaDecr(`budget:${campaignId}:${today()}`, cost);   // 日预算原子
  if (!ok) return strategy.onExhausted(campaignId);              // 降档/停止（配置策略）
  return cost;
}
// 回滚：refundEvent → luaIncr(budget, cost) —— 幂等（事件 ID）
```
