---
title: [NODE-095] 如何设计一个通知中心（多渠道聚合）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-095：如何设计一个通知中心（多渠道聚合）？
**答**：
- 职责：统一消息模型（type/模板/接收人/渠道偏好）→ 渠道路由（站内信/短信/邮件/Push，按等级与用户设置选择）→ 渠道适配器（各厂商 SDK 差异封装）→ 发送策略（去重、频控、静默时段）→ 状态回执与重试。
- 模式：模板 + 变量渲染（渠道差异文案）、**扇出**（一条业务事件扇出到多渠道，异步并行）、失败降级（Push 失败转短信）。
- 服务端要点：发送异步化（MQ，NODE-088）、频控（同用户同模板 10 分钟一条，Redis 窗口计数）、回执幂等。

```javascript
// 渠道适配器：统一接口
const channels = {
  email: { async send(to, tpl, vars) { return emailProvider.send(to, render(tpl.email, vars)); } },
  sms:   { async send(to, tpl, vars) { return smsProvider.send(to, render(tpl.sms, vars)); } },
  push:  { async send(to, tpl, vars) { return pushProvider.send(to.deviceTokens, render(tpl.push, vars)); } },
  inbox: { async send(to, tpl, vars) { return db.inbox.create({ uid: to.uid, ...vars }); } },
};

// 渠道路由：按消息等级与用户偏好
function pickChannels(msgLevel, userSetting) {
  const matrix = { critical: ['push', 'sms', 'inbox'], normal: ['push', 'inbox'], marketing: ['inbox'] };
  return matrix[msgLevel].filter((c) => !userSetting.muted?.includes(c));
}

// 扇出 + 频控 + 失败降级
const notifyQueue = new Queue('notify-center', IOREDIS_OPTS);
async function dispatch(event) {
  const user = await userService.find(event.uid);
  for (const channel of pickChannels(event.level, user.notifySetting)) {
    await notifyQueue.add('send', { channel, event }, { attempts: 3,
      backoff: { type: 'exponential', delay: 5000 }, jobId: `${event.id}:${channel}` }); // 幂等键
  }
}

new Worker('notify-center', async ({ data }) => {
  const { channel, event } = data;
  // 频控：同用户同模板 10 分钟 1 条（营销类）
  if (event.level === 'marketing') {
    const ok = await redis.set(`nf:${event.uid}:${event.template}`, '1', 'EX', 600, 'NX');
    if (!ok) return;   // 频控命中：静默丢弃
  }
  try {
    await channels[channel].send(user, templates[event.template], event.vars);
  } catch (err) {
    // 降级：Push 失败转短信（critical 消息）
    if (channel === 'push' && event.level === 'critical') {
      await channels.sms.send(user, templates[event.template], event.vars);
      return;
    }
    throw err;   // 进入 BullMQ 重试
  }
}, { ...IOREDIS_OPTS, concurrency: 20 });

// 回执：厂商 webhook 回调，幂等更新状态
router.post('/callback/:channel', async (ctx) => {
  const { messageId, status } = parseCallback(ctx.params.channel, ctx.request.body);
  await db.query('UPDATE notifications SET status = ? WHERE message_id = ? AND status != ?',
    [status, messageId, 'delivered']);   // 状态机只前进，防回执乱序回退
  ctx.body = 'ok';
});
```
