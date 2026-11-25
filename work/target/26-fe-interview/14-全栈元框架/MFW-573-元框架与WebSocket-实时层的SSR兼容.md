---
title: [MFW-573] 元框架与 WebSocket：实时层与 SSR 的兼容架构
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-573：WebSocket 实时层与 SSR 的兼容架构

**答**:
- Next 的 WS 难点：standalone server 自持 WS 升级（custom server 脱离 Next 路由体系）或独立 WS 服务（跨服务协调 RBL-916）；serverless 平台无 WS（Vercel 函数无长连接——实时层必须外部：Pusher/Ably/自建 WS 服务）。
- 架构：1) **独立 WS 服务**（Node ws 服务 + Redis pub/sub 跨实例广播 RBL-569）；2) Next 的角色：SSR 页面 + 发起连接的 token 签发（WS 鉴权：Next 签短期 token → WS 服务校验——认证共享（session cookie 或 JWT 跨服务））；3) client 的连接管理（RBL-879 封装）。
- SSR 与实时数据的组合：页面数据走 SSR（初始快照）+ WS 订阅后续变更（快照 + 增量流——首屏 RSC 数据 + WS 实时层双通道；双通道的数据一致性（SSR 快照时刻与 WS 订阅起点之间的事件不丢——WS 订阅带 since 版本号/事件 id 补拉）。
- 追问钩子：为什么「SSR 快照 + WS 增量」的缝隙是最容易丢数据的？——SSR 渲染时读 DB（快照 T0）→ client 水合后建 WS 订阅（订阅从 T1 开始）——T0 到 T1 之间的变更丢失（订阅晚于快照）；解法：SSR 快照带版本号（数据表 version/max event id）→ WS 订阅 `since: version` → 服务端补发 T0-T1 之间的事件——「快照与流的接缝」是实时架构的经典缝隙：任何「初始读 + 后续订阅」的组合都要处理接缝（游标语义 RBL-920 的订阅版）。

```typescript
// Next 侧：签发 WS token + SSR 快照带版本
export default async function Page() {
  const session = await auth();
  const snapshot = await getOrders(session.userId);      // 快照 T0
  const wsToken = await signWsToken(session.userId, 60); // 短期 token
  return <Orders initial={snapshot} since={snapshot.version} wsToken={wsToken} />;
}
// WS 服务：token 校验 + since 补拉
wss.on('connection', async (ws, req) => {
  const session = await verifyWsToken(new URL(req.url, 'http://x').searchParams.get('t'));
  ws.send(JSON.stringify({ type: 'orders', data: await getOrders(session.userId) }));   // 可选：服务端补全
});
// client：快照渲染 + WS 增量（since 补缝隙）
const ws = createWsClient({ url: `wss://ws.x.com?token=${wsToken}` });
ws.send({ type: 'subscribe', channel: `orders:${userId}`, since });
// server 收到 since → 先补发 T0-T1 事件 → 再直播实时事件
```
