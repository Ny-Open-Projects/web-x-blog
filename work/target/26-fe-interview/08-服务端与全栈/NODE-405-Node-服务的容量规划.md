---
title: [NODE-405] Node 服务的容量规划（从流量模型到资源清单）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-405：Node 服务的容量规划
**答**:
- 容量模型推导链：业务指标（DAU/订单量）→ 接口 QPS（行为漏斗占比，与前端埋点对齐 ARC-446）→ 单实例容量（压测 NODE-373）→ 实例数（峰值 QPS ÷ 单实例 × 冗余系数 1.5~2）→ 依赖容量（DB 连接 = 实例 × 池 × 副本数、下游配额、MQ 分区数）。
- 三类资源清单：计算（CPU/内存，HPA 上限 NODE-375）、连接类（DB/Redis 连接上限是隐性瓶颈——连接数不随 HPA 线性安全扩展，配 PgBouncer）、带宽与配额（CDN/第三方 API）。
- 验证：容量预案压测走一遍（每层余量确认）、依赖方容量对齐会（下游知道你的峰值）。
- 动态复核：容量模型随流量结构变化失效（新功能改变行为漏斗）——季度复核 + 大促前重算；容量使用率看板（长期 > 70% 即扩容评审）。
- 产出：容量预案文档（各层数字 + 扩容 SOP + 触发阈值），值班可执行（ARC-446 配合）。
```javascript
// 容量计算器
function capacity({ dau, peakFactor, funnel, perInst }) {
  const peakQps = dau * peakFactor / 86400 * funnel.actionShare;   // 接口峰值
  const replicas = Math.ceil(peakQps / perInst.qps * 1.8);         // 冗余 1.8
  const dbConns = replicas * perInst.poolSize;
  return { peakQps: Math.ceil(peakQps), replicas,
    dbConns, dbOk: dbConns <= dbMaxConnections, note: dbOk ? '' : '需 PgBouncer' };
}
```
