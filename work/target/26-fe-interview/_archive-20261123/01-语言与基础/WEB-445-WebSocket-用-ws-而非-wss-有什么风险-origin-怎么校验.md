---
title: [WEB-445] WebSocket 用 ws 而非 wss 有什么风险，origin 怎么校验
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-445：WebSocket 用 ws 而非 wss 有什么风险，origin 怎么校验

**答**：
- ws 明文：握手与消息都可被中间人读取和篡改；CSRF/劫持风险与 http 明文同级别，生产必须 wss
- WebSocket 天然不受同源策略限制：任何页面的脚本都能对你的 ws 端点发起连接——CSWSH（跨站 WebSocket 劫持）是真实威胁
- 握手阶段校验：服务端检查 Origin 头是否在白名单（浏览器一定会带 Origin，非浏览器客户端可能不带，要结合 token）
- 双保险：握手带一次性 ticket（先 HTTP 换取），消息层再校验会话；仅靠 Origin 不足，因为部分客户端不发送
- 钩子：Cookie 鉴权的 WS 最易中 CSWSH，token-in-query 的又易泄漏日志，推荐「握手 ticket + 消息内 token」组合

```javascript
// 服务端握手校验（ws 库）
new WebSocket.Server({
  server,
  verifyClient: (info) => {
    const origin = info.req.headers.origin;
    return ALLOWED_ORIGINS.includes(origin); // 防 CSWSH 第一道
  },
});
```
