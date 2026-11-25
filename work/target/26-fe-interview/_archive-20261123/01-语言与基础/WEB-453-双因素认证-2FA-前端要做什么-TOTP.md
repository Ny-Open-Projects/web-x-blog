---
title: [WEB-453] 双因素认证 2FA 前端要做什么（TOTP）
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-453：双因素认证 2FA 前端要做什么（TOTP）

**答**：
- 2FA 两类载体：TOTP 动态码（Google Authenticator 扫码绑定）与短信验证码；TOTP 更安全（不依赖运营商信道）
- 前端职责一：绑定流程展示 otpauth URI 的二维码——`otpauth://totp/站点:账号?secret=XXX&issuer=站点`，用户扫码录进验证器
- 前端职责二：登录时输入 6 位动态码，倒计时提示刷新周期（30s），错误码友好提示
- 恢复码：绑定后必须让用户保存一次性恢复码（下载/复制），丢失验证器时保命
- 安全细节：动态码输入不要做自动提交（防粘贴钓鱼页自动验证）；接口按账号限流防爆破

```html
<!-- 绑定页：渲染 otpauth 二维码 -->
<img src="/api/2fa/qrcode" alt="用验证器 App 扫码绑定">
<input inputmode="numeric" pattern="[0-9]{6}" maxlength="6" placeholder="6 位动态码">
```
