---
title: [NODE-497] Node 服务的灰度标签全链路透传（HTTP/MQ/定时任务）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-497：灰度标签全链路透传
**答**:
- 场景：灰度判定在某层做出（网关/端上），后续所有环节（BFF→下游→MQ→定时任务）必须延续同一标签——否则灰度数据混杂、新旧逻辑交叉（ARC-449 数据兼容的前提）。
- HTTP 链路：网关染色（NODE-370）→ 每跳透传（HTTP 客户端自动转发 x-gray-tag——客户端封装统一处理，禁手写遗漏）→ ALS 上下文携带（NODE-421）。
- MQ 链路：消息体/头携带标签 → 消费端按标签路由（灰度消息消费到灰度实例 NODE-370）——无标签消息按默认处理。
- 定时/异步任务：任务发起时的标签快照（定时任务本身无请求上下文——按任务声明或全量策略）。
- 观测与对账：标签覆盖率监控（灰度比例 vs 各层标签比例对齐——某层缺失立即发现）、标签丢失点定位（链路打点：入口→BFF→下游→MQ 各层标签存在率）。
- 边界：标签透传是"尽力而为 + 监控兜底"——完全保证需要全链路改造，优先保证关键链路（交易）。
```javascript
// 透传封装（客户端统一）
async function internalCall(url, init = {}) {
  const g = als.getStore()?.gray;                                // ALS 取标签
  return fetch(url, { ...init, headers: { 'x-gray-tag': g ?? 'stable', ...init.headers } });
}
// MQ 生产：produce(topic, { payload, grayTag: als.getStore()?.gray }) → 消费端按标签路由
```
