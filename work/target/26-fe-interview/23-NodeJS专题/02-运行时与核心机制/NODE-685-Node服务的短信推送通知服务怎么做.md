---
title: [NODE-685] 短信/推送通知服务怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-685：通知服务怎么做？
**答**：
- 渠道编排：多渠道路由（SCN-OPS-612 通知矩阵——紧急双通道/普通摘要/免打扰豁免）；渠道失败降级（短信失败转语音/Push——降级链）。
- 频控与聚合：频控（每用户每日上限——SCN-FIN-557 防轰炸）、聚合（同类合并——SCN-OPS-320 降噪）、退订管理（退订即停——合规）。
- 可靠性：发送队列（MQ 异步——回调入口快速 ack，SCN-NODE-683 同构）；状态回执处理（渠道回执 → 发送状态机——失败重试换渠道）。
- 内容与合规：模板化管理（运营配置——SCN-OPS-610 联动）、敏感内容审核钩子、手机号脱敏日志（SCN-NODE-646）。
- 追问钩子：为什么通知服务必须「入口异步化 + 状态回执闭环」——同步发短信把渠道延迟（秒级）接进业务请求（下单接口变慢）；异步队列 + 渠道回执让「发送结果」显式化（失败可见可补偿）——没有回执闭环的通知服务，丢失率不可知（「发了没收到」客诉无法定位）。

```javascript
// 入口异步化
app.post('/notify', async (req, res) => {
  await mq.publish('notifications', { ...req.body, idemKey: req.idemKey });
  res.accepted();                                      // 快速 ack
});
// 渠道回执 → 状态机
consumer.run({ eachMessage: async ({ message }) => {
  const st = await receiptStatus(message);             // 渠道回执
  st === 'FAILED' ? scheduleRetryOrFallback(message) : markDelivered(message);
}});
```
