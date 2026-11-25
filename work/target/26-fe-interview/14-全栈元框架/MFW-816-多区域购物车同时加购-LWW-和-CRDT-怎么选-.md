---
title: [MFW-816] 多区域购物车同时加购，LWW 和 CRDT 怎么选（字节电商场景）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-816：多区域购物车同时加购，LWW 和 CRDT 怎么选（字节电商场景）

**答**：
- 结论：LWW（最后写入胜）会丢更新——A 区加 X、B 区加 Y，最终只剩其一；CRDT（LWW-Element-Set / OR-Set）能合并双方，适合「加购」这类可交换操作。
- 取舍：CRDT 需带版本号/节点 id、状态无限增长需 tombstone 压缩；LWW 简单但只适合「整体覆盖」语义（如昵称、状态）。
- 追问钩子：金额/库存能用 CRDT 吗？——不能；强一致数据走事务 + 主库，CRDT 只用于可交换的协作型数据。

```javascript
// LWW：整对象覆盖，后写覆盖先写 → 丢更新
function lwwCart(local, remote) {
  return remote.updatedAt > local.updatedAt ? remote : local;
}
const A = { items: { x: 1 }, updatedAt: 10, node: 'a' };
const B = { items: { y: 1 }, updatedAt: 11, node: 'b' };
console.log(lwwCart(A, B).items);                    // { y:1 } —— x 丢失

// CRDT（LWW-Element-Set）：逐元素按时间戳合并
function mergeSet(a, b) {
  const out = new Map(a);
  for (const [id, ts] of b) if ((out.get(id) ?? -1) < ts) out.set(id, ts);
  return out;
}
console.log([...mergeSet(new Map([['x', 1]]), new Map([['y', 1]]))]);
// x,y 都保留 —— 加购语义正确合并
```
