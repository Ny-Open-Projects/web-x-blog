---
title: [NODE-444] Node 服务的服务端特性开关（与前端联动）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-444：服务端特性开关
**答**:
- 开关的两种裁决位置：服务端裁决（路由/接口行为/返回结构）与端上裁决（UI 显隐）——联动原则：一个开关一次分桶（ARC-390），服务端把分桶结果随响应下发（x-flag 头或 meta 字段），前端消费而非重复分桶（防端侧算法不一致导致请求与 UI 不匹配）。
- 服务端开关实现：中间件读开关快照（NODE-388 配置中心）→ 按用户分桶 → 路由到新旧 handler（版本并存 NODE-359 思想）或注入行为参数。
- 类型安全：开关影响的行为差异收敛到策略对象（newPaymentFlow vs oldPaymentFlow 实现同一接口），handler 层无 if 散落。
- 生命周期：开关必须有清理计划（上线稳定后删除分支代码——开关债务堆积是反模式，ARC-288 配额治理）、创建时登记 owner/清理日期。
- 观测：开关命中率/性能影响（开与关的延迟对比——开关本身不应显著变慢）。
```javascript
// 服务端开关：一次分桶，结果下发
app.use((ctx, next) => {
  const bucket = gray.resolve(ctx.user, 'payment-v3');           // 分桶
  ctx.state.flag = { 'payment-v3': bucket };
  ctx.set('x-flag-payment-v3', bucket);                          // 前端消费同一结果
  return next();
});
// handler：策略对象
const flow = flagOn(ctx) ? paymentV3 : paymentV2;                // 同接口两实现
ctx.body = await flow.pay(ctx.state.parsed);
```
