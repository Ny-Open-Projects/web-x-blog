---
title: [WEB-327] token 被盗了有哪些迹象？前端能做什么缓解？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-327：token 被盗了有哪些迹象？前端能做什么缓解？
**答**：
- 迹象：异地/异常 UA 同 token 并发使用、行为突变（批量请求）、refresh 使用冲突（轮换撞车）。
- 前端缓解：HttpOnly 缩小可窃面、绑定设备指纹/IP 段进 token claim、关键操作二次验证（密码/短信/生物）。
- 根治靠后端风控：会话风险评分 + 可疑即吊销；前端责任是"别让 XSS 偷到 token"。

```javascript
// 风控信号采集（前端上报）
collect({ ua: navigator.userAgent, tz: Intl.DateTimeFormat().resolvedOptions().timeZone,
  fp: await fingerprint(), action: 'login' });
// 服务端: token 绑定 fp hash，不匹配 → 要求二次验证
console.log('token 不是唯一凭证，行为+设备构成多维信号');
```
