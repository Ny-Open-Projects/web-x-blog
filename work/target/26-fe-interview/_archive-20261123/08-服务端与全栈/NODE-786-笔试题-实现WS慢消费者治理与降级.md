---
title: [NODE-786] 笔试题——实现 WS 慢消费者治理（bufferedAmount 监控 + 降级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-786：手写慢消费者治理

**需求与边界**：
- 需求：WS 慢消费者（SCN-NODE-650）——① bufferedAmount 监控（积压阈值——SCN-NODE-650 核心指标）；② 分级处置（积压 → 暂停推送 → 踢掉转轮询——SCN-NODE-650）；③ 心跳死连接清理（ping/pong）；④ 广播风暴防护（消息合并窗口——SCN-联想-855）。
- 边界：① 处置分级渐进（先暂停高优先级消息——再踢；体验降级路径）；② 踢掉的客户端降级通知（转轮询指引——SCN-联想-558 降级链）；③ 广播合并（万级连接的消息合并窗口——SCN-联想-855 排队页同源）。

**答**：
```javascript
setInterval(() => wss.clients.forEach(ws => {
  if (ws.bufferedAmount > 5e6) {                       // 5MB 积压：踢掉（SCN-NODE-650）
    ws.send(JSON.stringify({ type: 'DEGRADE_TO_POLLING', interval: 5000 }));   // 降级指引
    ws.close(4000, 'SLOW_CONSUMER');
    metrics.count('ws-slow-kicked');                   // 降级监控
  } else if (ws.bufferedAmount > 1e6) {                // 1MB：暂停非关键推送（渐进）
    ws.paused = true;                                  // 仅推 critical 消息（分级）
  } else ws.paused = false;
  if (Date.now() - ws.lastPong > 60_000) ws.terminate();   // 心跳死连接
}), 10_000);
function broadcast(msg) {
  wss.clients.forEach(ws => { if (!ws.paused || msg.critical) ws.send(msg); });   // 分级广播
}
```

**评分点**:
- bufferedAmount 分级处置（1MB 暂停非关键/5MB 踢掉——渐进降级）。
- 降级指引（转轮询——SCN-联想-558 语义）。
- 心跳死连接清理（pong 超时 terminate）。
- 广播分级（critical 穿透暂停——SCN-联想-855 合并窗口同源）。
