---
title: [NODE-266] tRPC 的订阅与流式？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-266：tRPC 的订阅与流式？
**答**:
- subscription：tRPC 的实时通道（WS 底层），observer 模式推增量——类型安全延伸到流（payload 类型同样推导）。
- 实现要点：订阅句柄返回（onStop 清理）、去重（同 key 多订阅端合并为一份上游订阅——观察者扇出 NODE-256 同构）、心跳保活。
- 与 SSE 的取舍：tRPC WS（双向+订阅）/ SSE（单向简单，NODE-45x AI 场景）——AI 流式对话用 SSE 更轻。
- 连接管理：鉴权在 WS 握手（token 随协议头），断线重连 + 订阅状态恢复（重订阅 key 列表）。

```typescript
// tRPC 订阅
const router = t.router({
  onOrderUpdate: protectedProcedure
    .input(z.object({ orderId: z.string() }))
    .subscription(({ input, ctx }) => {
      return observable<Order>((emit) => {
        const unsub = orderBus.on(`order:${input.orderId}`, (o) => emit.next(o));   // 观察者
        return () => unsub;                        // 客户端断开时清理（防泄漏）
      });
    }),
});
// 客户端：const sub = trpc.onOrderUpdate.subscribe({ orderId: '1' }, { next: (o) => render(o) });
// 扇出：orderBus 按 key 分发——N 个订阅端共享一份 bus 监听（去重由 bus 层实现）
```
