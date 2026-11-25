---
title: [NODE-174] 设计一个通知中心（多通道/模板/频控）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-174：设计一个通知中心（多通道/模板/频控）？
**答**：
- 与 NODE-095 互补，本题聚焦**频控与通道优先级**：通知按优先级走通道链（push → sms → email），成功一个即止；营销类通知独立低优先级队列与更严频控。
- 频控：每通道每用户窗口计数（Redis INCR+PEXPIRE，精确版换滑动窗口 NODE-132），超限跳下一通道并记录 skip 原因。
- 模板：模板 + 参数 + i18n 渲染分离；模板变更走 review；发送结果全量落 notifyLog 供查询与对账。
- 免打扰：用户级 mute 配置（时段/通道）在频控之前检查。

```javascript
const CHANNELS = { sms: sendSms, email: sendEmail, push: sendPush, inapp: saveInbox };
const FREQ_LIMITS = { sms: [5, 3_600_000], push: [20, 3_600_000], email: [10, 3_600_000] };

async function notify({ uid, template, params, channels = ['push', 'sms'] }) {
  const user = await db.user.findUnique({ where: { id: uid } });
  for (const ch of channels) {                       // 按优先级依次尝试
    const [max, window] = FREQ_LIMITS[ch];
    const n = await redis.incr(`freq:${ch}:${uid}`); // 频控计数
    if (n === 1) await redis.pexpire(`freq:${ch}:${uid}`, window);
    if (n > max) { recordSkip(uid, ch, 'rate-limited'); continue; }
    if (user.mute?.includes(ch)) { recordSkip(uid, ch, 'muted'); continue; }
    const body = renderTemplate(template, params, user.locale);
    const r = await CHANNELS[ch]({ to: user[ch === 'sms' ? 'phone' : ch], body });
    await db.notifyLog.create({ data: { uid, ch, template, status: r.ok ? 'SENT' : 'FAILED', ref: r.id } });
    if (r.ok) return { delivered: ch };              // 成功一个通道即止
  }
  return { delivered: null };
}
```
