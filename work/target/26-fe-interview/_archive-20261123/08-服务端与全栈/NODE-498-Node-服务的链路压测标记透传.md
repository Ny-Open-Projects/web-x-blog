---
title: [NODE-498] Node 服务的压测流量标记与影子数据隔离如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-498：压测流量标记与影子隔离
**答**:
- 危险：压测流量混入生产数据（真实订单表进压测订单——资损与数据污染事故）。标记体系：压测请求全链路打标（x-load-test: 1）→ 各存储按标记路由影子。
- 影子方案：影子表（同结构表 + 压测写入路由到 shadow 表）、影子队列（MQ topic 加 shadow 后缀）、影子下游（下游调用同样透传标记，下游也写影子）、外部通道硬断（短信/支付等真实外部调用直接拒绝或 mock——压测标记流量禁出外网 NODE-436）。
- 透传实现：与灰度标签同机制（NODE-497 封装）——标记随 ALS/消息头全程传递；入口校验（标记只能来自压测发压机白名单 IP，防伪造混入）。
- 对账与清理：影子数据定期清理（压测后 shadow 表 truncate 任务）、监控分离（压测指标独立命名空间不污染生产告警——NODE-372 tag 区分）。
- 演练：标记泄漏测试（注入带标记请求 → 断言生产表零写入——隔离真实性的最终验证）。
```javascript
// 影子路由
function routeTable(tag) { return tag === 'load-test' ? 'orders_shadow' : 'orders'; }
await db.query(`insert into ${routeTable(ctx.state.loadTag)} ...`);
// 外部通道：if (ctx.state.loadTag) return mockSms();            // 压测不出外网
// 清理：cron('0 4 * * *') → truncate all *_shadow              // 每日影子清理
```
