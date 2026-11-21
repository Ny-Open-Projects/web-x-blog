---
title: [NODE-313] tRPC 深水区：订阅与批处理的工程实践？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-313：tRPC 深水区：订阅与批处理的工程实践？
**答**:
- 批处理（batch link）：客户端自动合并同一 tick 的多个 query 为一次 HTTP（batch 参数）——服务端按 procedure 数组顺序返回；服务端内部再 DataLoader 合批。
- 订阅资源管理：WS 连接数上限、每连接订阅数上限、订阅 key 去重（同 key 多端共享一份 bus 监听）。
- 错误语义：订阅错误推送（emit.error）后客户端自动重订阅（退避）——断线恢复订阅列表。
- 边界：批处理开启后单请求放大（N 个 procedure 一个请求）——网关限流按"逻辑请求数"计。

```typescript
// 批处理 + 订阅上限
// client: httpBatchLink({ maxURLLength: 2000 })   // 自动批
// server: 订阅限额
const limits = new Map();   // wsId → count
wss.on('connection', (ws) => {
  ws.on('message', (msg) => {
    if (isSubscribe(msg) && (limits.get(ws.id) ?? 0) > 50)
      return ws.close(4001, 'too many subscriptions');    // 上限保护
    limits.set(ws.id, (limits.get(ws.id) ?? 0) + 1);
  });
  ws.on('close', () => limits.delete(ws.id));
});
```
