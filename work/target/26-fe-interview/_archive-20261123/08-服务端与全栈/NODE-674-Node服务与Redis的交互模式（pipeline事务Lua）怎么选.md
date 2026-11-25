---
title: [NODE-674] Redis 交互模式（pipeline/事务/Lua）怎么选？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-674：Redis 交互模式怎么选？
**答**：
- pipeline：批量命令一次网络往返（延迟优化——无原子性）；适合批量读写（批量 GET/SET）。
- MULTI/EXEC 事务：命令排队原子执行（无回滚——执行中错误不撤销前序）；需要「打包」但逻辑简单时用。
- Lua 脚本：真原子（读-判-写复合逻辑——限流/锁/库存扣减，SCN-NODE-641/652/656 全是 Lua）；脚本要幂等考虑（重放安全）。
- 选型准则：只要批量 → pipeline；要原子打包 → MULTI；要「条件逻辑原子」→ Lua；Lua 过长 → 拆分或换数据结构（Redis 阻塞——脚本要快）。
- 追问钩子：为什么「读-判-写」必须用 Lua 而不是 pipeline——pipeline 的命令间无原子性（客户端 A 读 token=1、客户端 B 也读 1、都判断通过都扣减——超扣）；Lua 在服务端单线程执行「读-判-写」不可分割——竞态条件的原子化只有 Lua/事务能做，pipeline 只优化网络。

```javascript
// pipeline：批量（无原子）
const pipe = redis.pipeline();
keys.forEach(k => pipe.get(k));
const vals = await pipe.exec();
// Lua：读-判-写原子
const allowed = await redis.eval(tokenBucketLua, 1, key, ...args);
```
