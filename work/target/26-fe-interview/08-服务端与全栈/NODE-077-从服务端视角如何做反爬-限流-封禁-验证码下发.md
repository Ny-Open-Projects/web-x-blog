---
title: [NODE-077] 从服务端视角如何做反爬（限流、封禁、验证码下发）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-077：从服务端视角如何做反爬（限流、封禁、验证码下发）？
**答**：
- 分层防御：① **规则层**——IP/uid/设备指纹限流（令牌桶）、UA 与 Referer 校验、频率特征（无鼠标轨迹/请求间隔过于均匀）；② **成本层**——验证码（滑块/点选）下发与校验、JS 质询（动态 token、接口签名）；③ **数据层**——蜜罐字段、混淆数据（价格分单位、字段名动态化）。
- 处置梯度：限流（429）→ 人机验证（返回 `need_captcha`，前端弹验证码）→ 临时封禁（IP/uid 进黑名单 Redis）→ 永久封禁 + 风控审计。
- 服务端要点：处置必须**可自动解除**（TTL）与可申诉；误杀率监控；验证码校验结果一次性使用防重放。

```javascript
// 分层反爬中间件
const RISK_LEVELS = { ALLOW: 0, CAPTCHA: 1, BLOCK: 2 };

async function antiCrawler(ctx, next) {
  const uid = ctx.state.user?.uid;
  const fp = ctx.get('x-device-fp');                  // 前端 SDK 采集的设备指纹

  // 1. 黑名单检查（Redis Set/布隆）
  if (await redis.sismember('block:ip', ctx.ip) || (uid && await redis.sismember('block:uid', uid))) {
    ctx.status = 403;
    return (ctx.body = { code: 'BLOCKED' });
  }

  // 2. 行为特征：滑动窗口计数（1 分钟内请求数 + 失败率）
  const windowKey = `req:${uid ?? ctx.ip}`;
  const count = await redis.incr(windowKey);
  await redis.expire(windowKey, 60);
  const uniform = ctx.get('x-req-interval');           // 前端上报的请求间隔熵（演示）

  let risk = RISK_LEVELS.ALLOW;
  if (count > 300) risk = RISK_LEVELS.BLOCK;           // 高频
  else if (count > 60 || uniform === 'fixed') risk = RISK_LEVELS.CAPTCHA;  // 疑似脚本

  // 3. 验证码校验：携带 captcha token 的请求先验证
  if (ctx.get('x-captcha-token')) {
    const ok = await verifyCaptcha(ctx.get('x-captcha-token'));  // 滑块服务端校验，一次性
    if (ok) risk = RISK_LEVELS.ALLOW;                  // 通过人机验证放行并降权
    else { ctx.status = 403; return (ctx.body = { code: 'CAPTCHA_FAILED' }); }
  }

  // 4. 处置
  if (risk === RISK_LEVELS.BLOCK) {
    await redis.sadd('block:ip', ctx.ip);
    await redis.expire('block:ip', 0); // 说明：生产用 zadd/block:ip:{ip} 带 TTL，此处示意
    await redis.setex(`block:ip:${ctx.ip}`, 3600, '1');   // 1 小时临时封禁
    log.warn({ event: 'crawler_blocked', ip: ctx.ip, uid });
    ctx.status = 403;
    return (ctx.body = { code: 'BLOCKED' });
  }
  if (risk === RISK_LEVELS.CAPTCHA) {
    ctx.status = 401;
    return (ctx.body = { code: 'NEED_CAPTCHA', captchaUrl: '/captcha/challenge' }); // 前端弹验证码
  }
  await next();
}
```
