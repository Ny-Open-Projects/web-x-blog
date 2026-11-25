---
title: [H5-256] Web Push 的 VAPID 是什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-256：Web Push 的 VAPID 是什么

**答**：
- VAPID：服务器身份标识——一对 ECDSA 密钥，签名证明「推送确实来自我的服务器」，浏览器据此过滤垃圾推送
- 流程：公钥下发给前端用于 subscribe；私钥只在服务端，web-push 库用它签名每次推送请求
- 与推送服务的关系：浏览器厂商的推送服务（FCM、Apple Push、Mozilla）验证 VAPID 后才投递到设备
- 密钥管理：一对密钥长期使用（换掉会导致所有订阅失效），私钥严格保密
- 钩子：Apple 的推送走 APNs（iOS Safari 16.4+ 的 Web Push），配置上多一个 `web.push.apple.com` endpoint，但协议仍统一

```javascript
// 服务端（web-push 库）
const vapid = require('web-push').generateVAPIDKeys();
require('web-push').sendNotification(subscription, JSON.stringify(payload), {
  vapidDetails: { subject: 'mailto:admin@example.com', publicKey: vapid.publicKey, privateKey: vapid.privateKey },
});
```
