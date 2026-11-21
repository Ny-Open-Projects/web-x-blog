---
title: [NODE-453] Node 服务的多渠道消息推送（短信/邮件/IM）通道管理如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-453：多渠道推送通道管理
**答**:
- 通道抽象：统一消息模型（模板 + 收件人 + 优先级 + 业务场景）→ 渠道路由（按场景配置主备渠道，NODE-436 供应商治理）→ 适配器（短信/邮件/IM/Push 各自实现）。
- 可靠性：发送异步化（MQ 解耦业务）、失败重试退避 + 降级渠道（短信失败 → 邮件 → 站内信）、发送回执对账（供应商回执 vs 本地记录，ARC-382）。
- 频控与合规：同用户同场景频控（验证码 1 分钟 1 条/天 10 条——防骚扰与成本）、营销消息用户偏好（退订生效 NODE-453）、夜间静默（非紧急类）。
- 模板治理：模板版本化与审核（文案变更走审批——发错模板是事故）、变量校验（渲染失败不发送——防半截消息出去）。
- 观测：各渠道成功率/延迟/成本看板、通道故障自动切换记录（切换事件告警）。
```javascript
// 渠道路由 + 降级
async function send(msg) {
  if (!await frequency.allow(msg.to, msg.scene)) return skip('频控');
  const rendered = template.render(msg.tpl, msg.vars);
  for (const ch of channels(msg.scene)) {                        // [sms, email, inbox]
    try { const r = await ch.send(rendered); await receipt.track(msg.id, ch, r); return r; }
    catch (e) { log.warn(e); continue; }                         // 降级下一通道
  }
  await dlq.add(msg);                                            // 全失败进死信
}
```
