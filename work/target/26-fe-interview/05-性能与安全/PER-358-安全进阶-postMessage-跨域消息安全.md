---
title: [PER-358] iframe/postMessage 跨域通信的安全清单：origin 校验、消息签名与数据白名单？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-358：iframe/postMessage 跨域通信的安全清单：origin 校验、消息签名与数据白名单？

**答**：
- 发送端：`targetWindow.postMessage(msg, targetOrigin)` 的 targetOrigin **必须精确域名**（不能 `'*'`）——否则消息可被嵌入的任意页面截获（如被 clickjacking 到攻击者 iframe）。
- 接收端三道门：① origin 校验——`e.origin` 必须在白名单（不是 `e.source` 的域，origin 才是可信来源）；② 消息 schema 校验——e.data 结构白名单（type 枚举 + 字段类型校验），拒绝任意对象直接进业务；③ 数据净化——消息里的字符串进 DOM 前净化（防 DOM-XSS：消息体直接 innerHTML 是经典漏洞）。
- 协议设计：消息带版本与 nonce（防重放），敏感操作（跨域登录态/支付）用服务端票据而不是消息直传；双向握手（首次交换能力清单）。
- 监控：未知 origin 的消息计数上报（探测攻击/联调错误）；消息体过大告警（防内存攻击）。

```javascript
// 发送端
iframe.contentWindow.postMessage({ type: 'v1:resize', h: 600 }, 'https://widget.partner.com');

// 接收端（widget 页面）
const ALLOWED = new Set(['https://www.mysite.com']);
window.addEventListener('message', (e) => {
  if (!ALLOWED.has(e.origin)) {                        // 1. origin 白名单
    reportUnknown(e.origin); return;
  }
  const msg = validate(e.data);                        // 2. schema 白名单校验
  if (!msg) return;
  switch (msg.type) {
    case 'v1:resize': resize(msg.h); break;            // 白名单 action 分发
    default: reportUnknownType(msg.type);
  }
});
// 反例：e.origin !== location.origin 才收 —— 错误且危险的写法
// 反例：div.innerHTML = e.data.html —— 消息体直进 DOM，DOM-XSS
```
