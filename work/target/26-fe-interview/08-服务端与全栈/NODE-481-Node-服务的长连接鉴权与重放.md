---
title: [NODE-481] Node 服务长连接的安全（鉴权续期/消息防重放）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-481：长连接鉴权与防重放
**答**:
- 连接生命周期鉴权：握手时验 token（NODE-393）只是起点——长连接可能活几小时，token 早过期。续期协议：token 过期前服务器推送"要求重认证"，客户端带新 token 回执；超时未续 → 优雅断开（客户端自动重连走新 token）。
- 消息防重放：上行消息带 nonce + 时间窗（服务端验窗 + nonce 去重缓存——防抓包重放操作消息）；关键操作消息（连麦控制/支付相关）双重校验（签名 + 会话内序号）。
- 会话绑定：连接与登录会话绑定——会话被踢（ARC-415 单点登出）→ 长连接同步断开（踢出事件触发 force close）；同账号多连接管理（新设备顶替策略）。
- 权限动态化：订阅权限随会话变化（用户权限收回 → 相关 topic 订阅即时撤销，ARC-550 联动）。
- 审计与风控：连接层异常模式（高频重连/异常 topic 订阅尝试）上报风控（NODE-456）。
```javascript
// 长连接续期 + 防重放
ws.on('reauth', async ({ token }) => {
  const s = await verify(token);                                 // 过期前续期
  if (!s) return ws.close(4401, 'reauth failed');
  ws.session = s;                                                // 绑定新会话
});
function onUpstream(msg) {
  if (!nonceCheck(msg.id)) return drop('replay');                // nonce 去重
  if (Date.now() - msg.ts > 10e3) return drop('stale');          // 时间窗
  route(msg);
}
session.on('revoked', () => ws.close(4403, 'session revoked'));  // 踢出联动
```
