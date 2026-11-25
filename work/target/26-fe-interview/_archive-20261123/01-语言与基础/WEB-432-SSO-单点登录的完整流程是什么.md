---
title: [WEB-432] SSO 单点登录的完整流程是什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 鉴权]
type: 面试题
---

## WEB-432：SSO 单点登录的完整流程是什么

**答**：
- 组成：统一认证中心（CAS/SSO Server）+ 各业务系统；一次登录，全域免登
- 流程：业务系统发现无会话 → 302 到认证中心（带回跳地址）→ 认证中心有会话则直接发票据（ticket/code）→ 业务系统后端拿票据换会话 → 建立自己的本地 Cookie
- 认证中心的登录态靠它在自家域下的 Cookie 维持；各业务域 Cookie 只代表本地会话
- 登出：单点登出要广播通知所有业务系统清会话（front/back-channel logout），漏掉会出现「登出后又自动登录」
- 前端注意：跨域跳转链路上 Cookie 的 SameSite=None; Secure 配置，以及回跳时地址栏泄漏 ticket 的处理（进页面立刻 replaceState 清参数）

```javascript
// 回调页清掉敏感票据参数
const url = new URL(location.href);
if (url.searchParams.has('ticket') || url.searchParams.has('code')) {
  url.searchParams.delete('ticket'); url.searchParams.delete('code');
  history.replaceState(null, '', url.pathname + url.search);
}
```
