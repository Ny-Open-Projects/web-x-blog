---
title: [WEB-265] WebSocket 鉴权怎么做？握手阶段与消息阶段
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, WebSocket]
type: 面试题
---

## WEB-265：WebSocket 鉴权怎么做？握手阶段与消息阶段

**答**：
- WebSocket 握手是 HTTP Upgrade 请求，可以用 HTTP 鉴权手段：Cookie（同域自动带，天然可用 session）、URL query token（会进日志，不推荐）、Sec-WebSocket-Protocol 或自定义 header（浏览器 WS API 不能设自定义头，故 Cookie/子协议是最常用路径）。
- 服务端在 upgrade 前校验 cookie/session，失败返回 401 并拒绝升级。
- 消息阶段：连接建立后 token 无法再「带在头上」，心跳/消息内嵌 auth 字段做二次校验；长连接要定期重验（用户被踢/权限变更时服务端主动 close）。
- 连接复用与重连：断线重连要用最新 token 重新握手，旧 token 过期会导致重连失败循环——前端要处理 401 后刷新 token 再重连。

```javascript
// 前端：token 过期后重连
let ws;
function connect(token) {
  ws = new WebSocket(`wss://im.example.com/ws`);
  ws.onclose = async (e) => {
    if (e.code === 4401) {              // 自定义：token 失效
      await refreshToken();
      return connect(token = store.token);
    }
    setTimeout(() => connect(token), backoff()); // 指数退避重连
  };
}
```
