---
title: [NODE-885] 笔试题——实现发布依赖方影响面扫描（服务端版）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-885：手写影响面扫描

**需求与边界**：
- 需求：发布影响面（SCN-OPS-291 服务端版）——① 接口依赖扫描（本服务的接口被谁调用——反向依赖，SCN-NODE-768 契约）；② 消息依赖扫描（本服务发的 topic 被谁消费——SCN-NODE-651）；③ 影响面报告（SCN-OPS-291）；④ 评审材料联动（SCN-OPS-881）。
- 边界：① 依赖数据源（注册表/调用统计——SCN-OPS-291）；② 影响面的风险分级（消费方 SLA 等级——SCN-OPS-643）；③ 扫描进 CI（SCN-OPS-261 材料前置）。

**答**：
```javascript
async function releaseImpactScan(plan) {
  const apiConsumers = await contractBroker.consumers(plan.app);   // 接口消费方（SCN-NODE-768）
  const topicConsumers = await mq.topicsConsumers(plan.topics);    // 消息消费方（SCN-NODE-651）
  const impacted = [...apiConsumers, ...topicConsumers].map(c => ({
    consumer: c, sla: c.slaLevel, risk: c.slaLevel === 'P0' ? 'HIGH' : 'MID',   // 风险分级（SCN-OPS-643）
    ack: requireAck(c, plan),                          // SCN-OPS-864
  }));
  return { impacted: impacted.sort(byRisk),            // 风险排序
    material: releaseReviewMaterial({ plan, impacted }) };   // 评审材料（SCN-OPS-881）
}
```

**评分点**:
- 接口 + 消息双向扫描（SCN-NODE-768/651）。
- 风险分级（消费方 SLA——SCN-OPS-643）。
- ack 联动（SCN-OPS-864）。
- 评审材料生成（SCN-OPS-881）。
