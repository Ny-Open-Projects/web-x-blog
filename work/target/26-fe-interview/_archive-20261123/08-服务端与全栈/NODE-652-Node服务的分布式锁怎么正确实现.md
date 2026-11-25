---
title: [NODE-652] Node 的分布式锁怎么正确实现？看门狗与 fencing 是什么？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-652：分布式锁怎么正确实现？
**答**：
- 基础实现：Redis SET NX PX（原子加锁带过期）+ 唯一 token（释放时校验——Lua 脚本「校验+删除」原子，防删别人的锁）。
- 锁过期问题：任务超时锁先过期 → 两个客户端同时持锁——解法看门狗（后台线程续期，Redlock 的实现细节）与 fencing token（单调递增令牌——下游校验令牌时效，拒绝旧令牌写入）。
- Redlock 的争议：多节点锁在时钟漂移/GC 停顿下仍有竞态——强一致需求用 ZooKeeper/etcd（线性一致）或 DB 唯一约束（最简单最可靠——「唯一索引就是分布式锁」）。
- 实践建议：锁保护的操作尽量幂等（锁失效也不出事——幂等是锁的保险，SCN-FIN-519 同源）；锁粒度最小化（锁资源 ID 而非全局）。
- 追问钩子：为什么「fencing token」能解决锁过期后的竞态——锁过期后客户端 A 仍认为自己持锁并写下游，客户端 B 已拿新锁也写——顺序错乱；fencing token 单调递增，下游存储校验「只接受更大 token」——即使锁服务失效，下游拒绝旧 token 保证写入有序——把一致性检查下沉到资源端，绕过锁的不可靠性。

```javascript
// 正确加锁/释放（Lua 原子）
const token = crypto.randomUUID();
const ok = await redis.set(`lock:${res}`, token, 'PX', 10_000, 'NX');
const release = `if redis.call('get',KEYS[1])==ARGV[1] then return redis.call('del',KEYS[1]) end`;
// 看门狗续期
const watchdog = setInterval(() => redis.eval(`pexpire KEYS[1] 10000`, 1, key), 8000);
```
