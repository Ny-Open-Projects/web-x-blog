---
title: [PER-615] login CSRF（登录 CSRF）是什么？和普通 CSRF 的危害差异与防御要点
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-615：login CSRF（登录 CSRF）是什么？和普通 CSRF 的危害差异与防御要点

**答**：
- 登录 CSRF：攻击者诱使受害者浏览器**用攻击者的凭据完成登录**（向登录接口提交攻击者账号密码），受害者无感知地登录进攻击者的会话——之后受害者把银行卡、地址、甚至文档存进自己的账号，实际是攻击者的账号，攻击者登录即可收割。
- 与普通 CSRF 的差异：普通 CSRF 是以受害者身份执行操作，login CSRF 是把受害者换成攻击者身份"；防御上 SameSite/CSRF Token 同样有效，但登录页常为了免 CSRF"设计成 GET 明文提交，恰好绕开了这些防护。
- 防御要点：登录接口强制 POST + CSRF Token（别图省事用 GET）；SameSite=Lax/Strict cookie；登录成功后的**身份确认页**（显示你已登录为 xxx@xx.com"）让用户可发现异常；OAuth 回调场景校验 state 防止登录注入。
- 移动端/APP 深链场景同样适用：scheme 唤起带 token 自动登录的链路要防被外部唤起注入会话。

```javascript

const loginCsrfDefense = {
  form: { method: 'POST', csrfToken: '随表单下发并校验', forbid: 'GET 查询串提交凭据' },
  cookie: { session: 'SameSite=Lax', csrf: 'Double-Submit' },
  confirmPage: '登录成功展示账号邮箱，用户可发现被登录成攻击者账号',
  oauth: { state: '回调强制校验 state，防 login 注入' },
  deepLink: { scheme: 'autoLogin?token=xxx 链路校验来源签名 + 一次性' },
};
// 攻击复现路径：攻击者页 <img src="/login?u=attacker&p=pwd"> -> 受害者浏览器带 cookie 提交
// -> 若登录接口接受 GET 且无 token，即中招；改 POST + Token + SameSite 后打不动
```
