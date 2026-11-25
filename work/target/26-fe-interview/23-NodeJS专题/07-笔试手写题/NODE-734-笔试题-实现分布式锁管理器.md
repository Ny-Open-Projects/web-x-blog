---
title: [NODE-734] 笔试题——实现分布式锁管理器（看门狗 + fencing + 释放安全）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-734：手写分布式锁

**需求与边界**：
- 需求：Redis 分布式锁（SCN-NODE-652）——① SET NX PX + 唯一 token（SCN-OPS-294 评估引擎语义）；② 看门狗自动续期（任务未完锁不失效）；③ 释放 Lua 原子（校验 token 才删——防删别人锁）；④ fencing token（单调递增——下游校验）。

**答**：
```javascript
class DistributedLock {
  async acquire(resource, { ttl = 10_000, watchdog = true } = {}) {
    const token = crypto.randomUUID();
    const ok = await redis.set(`lock:${resource}`, token, 'PX', ttl, 'NX');
    if (!ok) return null;                              // 被持（调用方决定等待/放弃）
    let wd;
    if (watchdog) wd = setInterval(() =>               // 看门狗续期（任务未完锁不失效）
      redis.eval(`if redis.call('get',KEYS[1])==ARGV[1] then redis.call('pexpire',KEYS[1],${ttl}) end`, 1, `lock:${resource}`, token), ttl * 0.7);
    const fencing = await redis.incr(`fencing:${resource}`);   // 单调递增 fencing token
    return {
      release: async () => {                           // Lua 原子释放（token 校验）
        clearInterval(wd);
        await redis.eval(`if redis.call('get',KEYS[1])==ARGV[1] then return redis.call('del',KEYS[1]) end return 0`, 1, `lock:${resource}`, token);
      },
      fencing,                                         // 下游校验：只接受更大 token（SCN-NODE-652）
    };
  }
}
// 用法
const lock = await lockMgr.acquire('order:123');
if (!lock) return retryLater();
try { await processOrder(order, lock.fencing); } finally { await lock.release(); }
```

**评分点**:
- 唯一 token + Lua 原子释放（防删别人锁——SCN-NODE-652）。
- 看门狗自动续期（任务超 TTL 不失效——锁过期竞态解法）。
- fencing token 单调递增（下游校验——锁失效兜底）。
- 未获取返回 null（调用方决策——不隐式阻塞）。
