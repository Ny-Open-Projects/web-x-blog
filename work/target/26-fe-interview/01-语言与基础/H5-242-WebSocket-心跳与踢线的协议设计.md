---
title: [H5-242] WebSocket 心跳与踢线的协议设计
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebSocket]
type: 面试题
---

## H5-242：WebSocket 心跳与踢线的协议设计

**答**：
- 双向心跳：客户端 30s 发 PING，服务端回 PONG；服务端也要检测「客户端 PING 停止」超时（如 90s）主动断开，回收死连接
- 协议层 vs 应用层：WS 自带 ping/pong 帧（浏览器 JS 无法发送，由实现层触发），应用层通常自定义 JSON 心跳消息
- 超时判定：连续 2 次心跳无响应即视为半开连接，客户端主动 close 触发重连，别傻等 TCP 层错误
- 踢线设计：服务端单播 KICK 消息（带原因码），客户端收到后停止重连（置 stopped 标志）并跳登录——与普通断线的重连逻辑必须区分
- 频率权衡：太密浪费流量、太疏受制于中间设备 idle 超时（常见 60~300s），30~50s 是安全区

```javascript
let pongTimeout;
function ping() {
  ws.send(JSON.stringify({ type: 'PING', t: Date.now() }));
  pongTimeout = setTimeout(() => ws.close(), 10000); // 10s 没回就重连
}
setInterval(ping, 30000);
ws.onmessage = (e) => {
  const m = JSON.parse(e.data);
  if (m.type === 'PONG') clearTimeout(pongTimeout);
  if (m.type === 'KICK') { stopped = true; gotoLogin(m.reason); } // 不再重连
};
```
