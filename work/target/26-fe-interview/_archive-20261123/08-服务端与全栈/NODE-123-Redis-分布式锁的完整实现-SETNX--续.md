---
title: [NODE-123] Redis 分布式锁的完整实现（SETNX + 续期 + Lua 释放）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-123：Redis 分布式锁的完整实现（SETNX + 续期 + Lua 释放）？
**答**：
- 加锁：`SET key token NX PX ttl` 一条命令原子完成"不存在才写 + 过期时间"，token 用 UUID 标识持有者。
- 释放：**Lua 保证"比对 token + 删除"原子**——直接 GET 再 DEL 两步之间锁可能已易主，会误删别人的锁。
- 看门狗：业务未执行完锁先过期 = 互斥失效；每 `ttl/3` 用 Lua 校验 token 后 PEXPIRE 续期。
- 局限要说清：主从切换可能丢锁，强一致场景用 Redlock 多节点或 ZK/etcd；锁只保护互斥，不替代幂等。

```javascript
const crypto = require('crypto');
const UNLOCK_LUA = `
if redis.call("get", KEYS[1]) == ARGV[1] then
  return redis.call("del", KEYS[1])
else
  return 0
end`;
const RENEW_LUA = `
if redis.call("get", KEYS[1]) == ARGV[1] then
  return redis.call("pexpire", KEYS[1], ARGV[2])
else
  return 0
end`;

async function withLock(key, ttlMs, fn) {
  const token = crypto.randomUUID();       // 唯一 token，防误删他人锁
  // ioredis：SET key value PX ttl NX 原子加锁
  const ok = await redis.set(key, token, 'PX', ttlMs, 'NX');
  if (!ok) throw Object.assign(new Error('lock conflict'), { status: 429 });

  const timer = setInterval(async () => {   // 看门狗：ttl/3 续期一次
    await redis.eval(RENEW_LUA, 1, key, token, ttlMs);
  }, ttlMs / 3);

  try { return await fn(); }
  finally {
    clearInterval(timer);
    await redis.eval(UNLOCK_LUA, 1, key, token); // 原子"比对+删除"
  }
}

// 使用：防止定时任务多实例并发执行
await withLock('lock:sync-orders', 30_000, () => syncOrders());
```
