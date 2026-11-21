---
title: [NODE-569] Node 服务的短信发送服务（通道/频控/回执）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-569：短信发送服务
**答**:
- 通道管理：多供应商（NODE-453 路由——主备/按地区路由）、模板管理（模板审核/变量校验——渲染失败不发送）、通道成本与质量（到达率/延迟——路由权重数据）。
- 频控体系：多层频控（同号码：验证码 1/min、营销 1/day——分级场景频控；全局防轰炸熔断：异常量自动停发——防短信轰炸攻击成本事故）、黑名单（退订用户——营销类拦截）、夜间静默（非紧急类延迟）。
- 发送链路：异步发送（MQ 解耦——业务不阻塞）、重试与降级（失败重试 → 换通道 → 死信）、发送幂等（业务键唯一——防重复发）。
- 回执处理：状态回执（供应商回执 → 更新发送状态——失败原因分类：空号/关机/拦截——号码质量数据）、上行回执（回复短信——业务联动如回复 TD 退订）。
- 对账：发送量对账（本地记录 vs 供应商账单——成本对账 ARC-382）、到达率监控告警。
```javascript
async function sendSms(msg) {
  if (!(await freq.allow(msg.phone, msg.scene))) return blocked('频控');
  const rendered = template.render(msg.tpl, msg.vars);
  for (const ch of smsChannels(msg.region)) {
    const r = await ch.send(rendered).catch(() => null);
    if (r) { await receipt.expect(r.msgId); return r; }          // 回执追踪
  }
  await dlq.add(msg);
}
```
