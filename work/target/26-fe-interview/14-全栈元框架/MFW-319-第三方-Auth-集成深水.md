---
title: [MFW-319] 第三方 Auth 集成深水（回调/会话同步/多域）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-319：第三方 Auth 深水

**答**:
- 回调安全：OAuth state 双提交（cookie + 参数比对——OAuth 流内 CSRF）+ redirect_uri 白名单精确匹配（open redirect 面）
- 会话同步双源问题：第三方托管会话（Clerk 类）与自建业务会话并存——以第三方为单一真相（自建只存业务链接表），避免双登出不同步
- 多域 SSO：主域证书 cookie（.app.com）子域共享；跨 product 域走中心 SSO 跳板（token 换取，非 cookie 直跨）
- 降级预案：Auth 供应商故障 → 只读模式（已登录会话延寿）+ 登录入口维护页——鉴权是单点，预案提前写

```text
四件：state 双提交防 OAuth CSRF / 第三方为会话单源 / 多域走 SSO 跳板 / 供应商故障只读预案
```
