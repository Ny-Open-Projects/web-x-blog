---
title: [NODE-381] Node 服务的幂等实现全景：重试/重放/重复消费防线
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-381：幂等实现全景
**答**:
- 幂等层清单：HTTP 接口（前端重试防重）、MQ 消费（重复投递）、定时任务（重入）、补偿（saga 重放）。原则：at-least-once 环境下每个写操作都要有幂等防线。
- 手段谱系：唯一键约束（DB 唯一索引，最可靠——insert 冲突即重复）、状态机检查（订单已支付拒绝再次支付）、幂等键表（idempotencyKey → 结果缓存，重复请求返回首次结果）、条件更新（update where status=pending 的 affectedRows=0 即已处理）。
- 接口幂等协议：客户端生成幂等键（uuid）随请求携带，服务端存"键 → 响应"（TTL 24h），同键重复返回原响应（不是重新执行）；键冲突但参数不同返回错误。
- 消费幂等：消息自带 messageId，消费前查处理表（唯一索引 insert）；或天然幂等设计（set 语义覆盖写）。
- 验证：幂等回归测试（同请求打两次断言同结果、并发同键断言只生效一次——用并发测试暴露竞态）。
```javascript
// 幂等键表实现
async function createOrder(idemKey, params) {
  const existing = await db.query('select * from idem where key=$1 and expires > now()', [idemKey]);
  if (existing) return existing.response;                       // 重放首次结果
  const order = await db.tx(async t => {
    const o = await doCreateOrder(t, params);
    await t.query(`insert into idem(key, response, expires) values($1,$2,now()+interval '24 hours')`, [idemKey, JSON.stringify(o)]);
    return o;
  });                                                           // 业务+幂等记录同事务
  return order;
}
```
