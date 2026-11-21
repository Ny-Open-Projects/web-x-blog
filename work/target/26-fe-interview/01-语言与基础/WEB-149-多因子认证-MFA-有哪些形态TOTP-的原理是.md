---
title: [WEB-149] 多因子认证（MFA）有哪些形态？TOTP 的原理是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-149：多因子认证（MFA）有哪些形态？TOTP 的原理是什么？
**答**：
- 三类因子：知识（密码）、持有（手机/硬件钥匙）、生物特征；MFA 要求跨类别至少两种，"密码+短信验证码"是弱化的 2FA（短信可被 SIM 劫持）。
- TOTP（RFC 6238）：服务端与认证器共享密钥，各自按 30 秒时间窗 + HMAC 算出 6 位码，容忍 ±1 窗口的时钟偏差。
- 备份码：MFA 开启时一次性下发，防止认证器丢失把账号锁死。
- 前端职责：MFA 引导页与二维码渲染、验证码输入的自动提交/粘贴处理、失败次数与冷却提示；敏感操作做二次验证（step-up auth）。

```javascript
// 服务端（Node）用 otplib 校验 TOTP，前端只负责采集输入
const { authenticator } = require('otplib');
// 绑定阶段：生成密钥与 otpauth 链接，前端渲染成二维码
const secret = authenticator.generateSecret();
const uri = authenticator.keyuri('user@example.com', 'Example Inc', secret);
// 校验阶段：窗口容忍 ±1，应对设备时钟偏差
authenticator.options = { window: 1 };
const ok = authenticator.verify({ token: req.body.code, secret });
if (!ok) return res.status(401).json({ error: 'invalid_totp' });
```
