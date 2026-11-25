---
title: [NODE-336] Node 服务的 Redis 使用规范与典型踩坑有哪些？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-336：Node 服务的 Redis 使用规范与典型踩坑
**答**:
- 规范基线：key 命名空间化（biz:entity:id）、TTL 必填（无过期 key 定期清理）、值大小限制（> 10KB 走压缩或换存储）、禁用 KEYS（SCAN 替代）、大 set/hash 拆分。
- 缓存三坑：缓存穿透（不存在的 key 反复查 DB → 空值短 TTL 缓存或布隆过滤器）、雪崩（同批 TTL 相同 → 加随机抖动）、击穿（热 key 过期瞬间打 DB → 互斥重建/逻辑过期）。
- 分布式锁：SET NX PX + 唯一值 + Lua 释放（防误删他人锁），看门狗续期（RedLock 争议场景直接用单实例锁 + 容忍极小概率）；锁粒度到业务键而非全局。
- 连接与超时：ioredis 连接池/复用、命令超时设置（Redis 挂了要快速失败走 DB 兜底而不是挂死请求）、maxmemory-policy 与业务预期对齐。
- 可观测：慢查询日志（SLOWLOG）、命中率监控、大 key 巡检（内存分析脚本定期跑）。
```javascript
// 分布式锁（ioredis + Lua）
const UNLOCK = `if redis.call("get", KEYS[1]) == ARGV[1] then return redis.call("del", KEYS[1]) else return 0 end`;
async function withLock(key, ttlMs, fn) {
  const token = crypto.randomUUID();
  const ok = await redis.set(`lock:${key}`, token, 'PX', ttlMs, 'NX');
  if (!ok) throw new LockBusyError(key);
  try { return await fn(); }
  finally { await redis.eval(UNLOCK, 1, `lock:${key}`, token); }  // 只删自己的锁
}
```
