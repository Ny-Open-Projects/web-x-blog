---
title: [NODE-486] Node 服务的读写模型分离（CQRS-lite）何时与如何落地？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-486：CQRS-lite 读写分离
**答**:
- 判断起点：不要一上来 CQRS——先识别"读写不对称"的痛点：写模型复杂但读查询形态完全不同（列表/报表/搜索），同表同模型两边别扭。
- CQRS-lite 形态（90% 场景够用）：写走规范化模型（事务/约束），读走专用查询模型（视图/宽表/异构索引 ES NODE-387）——写后异步投影（CDC 同步），读不碰写表。
- 落地步骤：识别读热点查询 → 建投影（宽表/物化视图）→ CDC 投影管道（NODE-387 同步 + 对账 ARC-382）→ 读切换到投影 → 删除读路径的复杂 join。
- 一致性窗口：投影延迟秒级——业务标注（"报表延迟 5min"）或关键读回源校验（写后读用主模型，投影只承载分析/列表 NODE-385）。
- 完整 CQRS（命令总线/事件溯源）只在高并发审计场景考虑——复杂度成本巨大，默认不做。
```javascript
// 写模型 + 读投影
// 写：orders 规范化表（事务/唯一约束）
// 读：order_summary 宽表（CDC 投影：join 商品/用户冗余字段）
async function listOrders(query) { return proj.query('select * from order_summary where ...'); }
async function payOrder(cmd) { return writeModel.tx(t => ordersRepo.markPaid(cmd, t)); } // 写走规范化
```
