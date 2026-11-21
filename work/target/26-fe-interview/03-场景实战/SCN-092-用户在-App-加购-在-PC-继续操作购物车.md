---
title: [SCN-092] 用户在 App 加购、在 PC 继续操作购物车，两端数据不一致，如何做跨端同步与冲突合并？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-092：用户在 App 加购、在 PC 继续操作购物车，两端数据不一致，如何做跨端同步与冲突合并？
**答**：
- 服务端为唯一真源：本地操作（加购/改数量/删行）先改 UI 再记入本地操作日志（oplog），防抖批量上报。
- 合并规则按行执行：同一商品行两端都改取操作时间新的（last-write-wins）；一端改、一端删时删除优先，避免"删掉的商品复活"。
- 同步流程：先推 oplog 让服务端按规则合并，再拉取合并后的全量结果整体替换本地。

```typescript
// 购物车跨端合并：服务端真源 + 行级 LWW + oplog 批量同步
type CartOp =
  | { type: 'add'; skuId: string; count: number; at: number }
  | { type: 'set'; skuId: string; count: number; at: number }
  | { type: 'remove'; skuId: string; at: number };

const pendingOps: CartOp[] = [];   // 本地未同步操作日志

async function syncCart() {
  if (!pendingOps.length) return;
  // 1. 上传 oplog，服务端按行合并：
  //    同一行两端都改 -> at 更新的胜出（last-write-wins）
  //    一端改、一端删 -> 删除优先，避免删掉的商品复活
  await api.pushCartOps([...pendingOps]);
  pendingOps.length = 0;
  // 2. 拉取合并后的服务端真源，整体替换本地
  const server = await api.getCart();
  replaceLocalCart(server.items);
}

// 本地操作：立即改 UI + 记 oplog，等同步时机批量上报
function setCount(skuId: string, count: number) {
  localCart.set(skuId, { count, updatedAt: Date.now() });
  pendingOps.push({ type: 'set', skuId, count, at: Date.now() });
  scheduleSync();   // 防抖 2 秒，操作密集时合并上报
}
```

## 十八、性能场景进阶
