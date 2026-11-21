---
title: [WEB-465] WebSocket 频繁断连的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-465：WebSocket 频繁断连的排查 SOP

**答**：
- 先看断连模式：规律性断（固定 60s/5min → 中间设备空闲超时杀连接）vs 随机断（网络切换/弱网）vs 上线即断（网关不支持升级）
- 排查链：心跳是否在发（协议层 ping/pong 或业务心跳）→ 负载均衡的 proxy_read_timeout/idle timeout → 手机端切网（visibilitychange 时主动重连）
- 心跳设计：间隔 < 中间设备空闲超时（一般 30~50s 一次），超时未回 pong 主动断开重连，避免「半开连接」收不到消息
- 重连策略：指数退避 + 抖动，防止断网恢复后全员同时重连打爆服务端；重连后补拉离线消息
- 移动端特有：锁屏后 App 挂起 WS 必断，回前台立刻检测 readyState 并重建，别等下次心跳失败

```javascript
let heartbeat;
ws.onopen = () => { heartbeat = setInterval(() => ws.send(JSON.stringify({ type: 'PING' })), 30000); };
ws.onclose = () => {
  clearInterval(heartbeat);
  setTimeout(connect, Math.min(30000, 1000 * 2 ** retry++) + Math.random() * 1000);
};
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible' && ws.readyState > 1) connect();
});
```
