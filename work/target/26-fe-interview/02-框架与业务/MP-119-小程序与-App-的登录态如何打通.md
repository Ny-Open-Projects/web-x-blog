---
title: [MP-119] 小程序与 App 的登录态如何打通？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-119：小程序与 App 的登录态如何打通？
**答**：
- 同一账号体系下，App 与小程序各自完成本平台鉴权（App：手机号/三方登录；小程序：wx.login），**服务端将两者关联到同一个 userId**，签发统一的自有 token。
- 关联方式：小程序端引导绑定（手机号一键登录 `getPhoneNumber`），或 App 拉起小程序时**经签名参数传递临时授权码**，服务端校验后绑定。
- token 过期共用同一刷新机制；openid/unionid 只是身份映射，**绝不能作为唯一鉴权依据**。
- 安全要点：跨端传递的参数要带时间戳+签名防重放；绑定关系落库（userId ↔ openid ↔ device）。

```mermaid
sequenceDiagram
  participant U as 用户
  participant MP as 小程序
  participant SRV as 服务端
  participant APP as App
  U->>MP: 打开小程序
  MP->>SRV: wx.login 的 code 换 openid
  SRV->>SRV: 查绑定表 openid 对应 userId
  alt 已绑定
    SRV-->>MP: 返回统一 token
  else 未绑定
    MP->>U: 引导手机号一键登录
    MP->>SRV: phoneCode 换手机号并绑定 userId
    SRV-->>MP: 签发统一 token
  end
  U->>APP: 返回 App
  APP->>SRV: 用同一 userId 校验 token
  SRV-->>APP: 登录态互通成功
```
