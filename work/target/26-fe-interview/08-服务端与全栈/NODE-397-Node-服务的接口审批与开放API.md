---
title: [NODE-397] Node 服务的开放 API（第三方接入）架构如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-397：开放 API 架构
**答**:
- 接入模型：应用注册（appKey/appSecret）+ 授权（OAuth2 授权码模式，用户授权第三方访问自己的资源 NODE-036）+ 访问令牌（access token + refresh token）。
- 调用安全：请求签名（appSecret + HMAC 签名防篡改/防重放：timestamp + nonce 窗口校验）、HTTPS 强制、IP 白名单（可选）。
- 配额与计费：appKey 维度限流（分档配额）、用量统计与计费指标、超配额 429 + 升级引导。
- 契约治理：对外 API 是"承诺级"契约——OpenAPI 文档公开、版本与 sunset 政策（NODE-359）、变更提前公告（第三方升级周期长）、沙箱环境与测试账号。
- 监控与风控：异常调用模式（爬取行为：高频分页扫描）识别与处置；错误响应不泄露内部信息。
```javascript
// 开放 API 签名校验
function verifyOpenApi(req) {
  const { appKey, timestamp, nonce, sign } = req.headers;
  if (Math.abs(Date.now() - timestamp) > 300e3) throw new Error('时间窗过期');   // 防重放
  if (await redis.get(`nonce:${nonce}`)) throw new Error('重复请求');            // nonce 去重
  await redis.set(`nonce:${nonce}`, 1, 'PX', 300e3);
  const expected = hmacSign(appSecret(appKey), `${appKey}${timestamp}${nonce}${req.rawBody}`);
  if (!timingSafeEq(expected, sign)) throw new Error('签名错误');
  await quota.take(appKey);                                       // appKey 配额
}
```
