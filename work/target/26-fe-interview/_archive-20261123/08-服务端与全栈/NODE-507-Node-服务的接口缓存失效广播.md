---
title: [NODE-507] Node 服务的缓存失效广播（写后多级失效）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-507：缓存失效广播
**答**:
- 场景：数据变更（商品改价）后多处缓存（BFF 片段缓存/下游数据缓存/CDN/客户端）都要失效——失效链路协议化（ARC-444 级联的服务端编排）。
- 失效事件协议：变更事件（domain.changed + 实体 + 影响缓存 tag 清单——写在失效映射表：哪个实体变更影响哪些缓存键）→ 失效执行器（按映射逐级失效：Redis del + Pub/Sub 通知各实例 L1 + CDN purge + 客户端推送失效通知）。
- 映射治理：失效映射登记（新缓存声明时登记它依赖的实体 tag——新缓存不登记映射 = 永不失效的隐患，CI 检查）、映射准确性审计（失效后数据是否真的新鲜——抽检验证 NODE-437）。
- 可靠性：失效失败重试（CDN purge 失败 → 重试队列）、失效与写入的事务性（本地消息表：业务写 + 失效事件同事务 NODE-380——防"写成功失效丢失"）。
- 观察：失效延迟（变更到缓存新鲜的端到端时长）、失效风暴防护（批量变更→失效合并去重——同 tag 窗口内合并一次）。
```javascript
// 失效映射执行
const invalidationMap = { 'goods.changed': ['frag:goods:*', 'cdp:/goods/*', 'client:goods'] };
bus.on('goods.changed', async ({ id }) => {
  for (const tag of invalidationMap['goods.changed'])
    await invalidator.purge(tag, { id, dedupeWindow: '5s' });    // 逐级失效 + 合并
});
```
