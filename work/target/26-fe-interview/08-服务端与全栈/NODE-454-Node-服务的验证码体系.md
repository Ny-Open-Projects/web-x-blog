---
title: [NODE-454] Node 服务的验证码体系（短信/图形/行为）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-454：验证码体系设计
**答**:
- 验证码三类：短信/邮件 OTP（强验证）、图形/滑块（人机识别）、行为验证（风控打分 ARC-158）。场景决定强度（登录=OTP、查询=图形、支付=OTP+二次）。
- OTP 安全：6 位随机（crypto.randomInt NODE-363）、有效期 5 分钟、一次性消费（验证成功即失效）、错误次数限制（5 次锁 30 分钟）、绑定维度（phone+scene+session——防跨场景爆破）。
- 发送治理：频控（NODE-453）、防轰炸（同号码限频 + 全局异常量熔断——被恶意刷短信的成本事故常见）、发送渠道降级。
- 人机验证集成：风控前置（低风险免验证/高风险加强验证——分级验证减少打扰）、验证通过凭证（token 短时效 + 一次性，后端复核）。
- 可观测：发送成功率/验证通过率/失败原因分布、验证码相关攻击模式告警。
```javascript
// OTP 发送与校验
async function sendOtp(phone, scene) {
  const key = `otp:${scene}:${phone}`;
  if (!(await freq.allow(key))) throw new TooFrequent();
  const code = crypto.randomInt(100000, 1000000);
  await redis.set(key, hash(code), 'EX', 300);                   // 哈希存储防缓存泄露直读
  await sms.send(phone, tplOtp, { code });                       // NODE-453 通道
}
async function verifyOtp(phone, scene, input) {
  if (++attempts(key) > 5) throw new Locked();
  if (await getdel(key) === hash(input)) return issueToken({ phone, scene, exp: 300 }); // getdel 原子消费
  throw new WrongCode();
}
```
