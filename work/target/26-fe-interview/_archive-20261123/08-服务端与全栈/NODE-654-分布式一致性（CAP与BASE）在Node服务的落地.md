---
title: [NODE-654] CAP/BASE 在 Node 服务的落地怎么理解？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-654：CAP/BASE 落地怎么理解？
**答**：
- CAP 实践化：网络分区必然发生（P 必选），真正选择是 C vs A——按「数据类型」分：库存/资金选 C（分区时拒绝服务——宁停不损）、展示/社交选 A（分区时用旧数据——可用性优先）。
- BASE：基本可用 + 软状态 + 最终一致——落地点：异步复制（副本延迟 = 不一致窗口）、读己之写（用户看自己的数据走主库——读一致性保障）、会话粘滞（SCN-OPS-244 sticky 同源）。
- 一致性分级实践：强一致（同事务）→ 读己之写 → 单调读（不回退）→ 最终一致——每级对应不同实现成本，按数据敏感度选级。
- 追问钩子：为什么「读己之写」是大多数产品的最低一致性要求——用户刚改昵称刷新后看到旧昵称（读写分裂到副本）是最高频投诉；实现成本低（写后 N 秒内该用户读主库——时间窗/cookie 标记），却覆盖 80% 的一致性投诉——投入产出比最高的一致性机制。

```javascript
// 读己之写：写后 30s 该用户读主库
async function read(key, user) {
  const recentWrite = await redis.get(`rw:${user.id}`);   // 写时 set 30s
  return recentWrite ? primary.query(key) : replica.query(key);
}
// 写路径
await primary.write(data); redis.set(`rw:${user.id}`, 1, 'EX', 30);
```
