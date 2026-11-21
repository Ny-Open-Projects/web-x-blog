---
title: [NODE-393] Node 服务的 WebSocket 鉴权与防滥用如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-393：WebSocket 鉴权与防滥用
**答**:
- 鉴权：握手期认证（URL/首消息带 token，server 端 verifyUpgrade）——升级为 WS 前完成鉴权，未认证连接不分配资源（或短时限时踢）；连接后定期续验（长连接 token 过期 → 服务器主动要求重新认证或断开）。
- 资源配额：每用户连接数上限（防多开耗尽）、每连接消息频率限制（令牌桶，超限断开或静默丢弃）、消息大小上限（防大包内存攻击）、订阅数上限。
- 滥用场景防护：恶意重连风暴（同 IP 重连限流，退避惩罚）、扫描探测（未认证连接统计与封禁）、房间轰炸（房间成员校验，禁止任意 join）。
- 与风控联动：WS 侧异常行为（消息频率/内容违规）上报风控中心；封禁用户的连接立即踢出并拒绝重连。
- 日志与取证：连接生命周期日志（connect/auth/fail/disconnect + uid + IP），攻击可回溯。
```javascript
wss.on('upgrade', async (req, socket, head) => {
  const token = new URL(req.url, 'http://x').searchParams.get('token');
  const user = await verify(token).catch(() => null);
  if (!user || connCount(user) >= MAX_PER_USER) { socket.destroy(); return; }  // 拒绝升级
  wss.handleUpgrade(req, socket, head, ws => {
    ws.user = user;
    ws.rate = tokenBucket({ rate: 20, burst: 40 });               // 消息频率配额
  });
});
ws.on('message', (d) => { if (!ws.rate.take() || d.length > 4096) return; handle(ws, d); });
```
