---
title: [NODE-475] Node 服务的分布式锁可靠性升级（ fencing token）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-475：分布式锁可靠性升级（fencing token）
**答**:
- 普通 Redis 锁的漏洞：锁过期瞬间持有者还在跑（GC 停顿/网络延迟），另一实例拿到锁 → 双执行。fencing token：锁带递增版本号，写入操作校验"我的 token 是最新版"——过期持有者的旧 token 写入被拒。
- 实现：锁服务发 token（Redis INCR 或 ZK 版本），存储层条件写（where fence = current——DB 乐观锁承载 fencing NODE-412）；Redis-only 场景：token 存入被保护资源的元数据比对。
- 持有者健康：看门狗续期（执行中自动续锁——但续期失败要能优雅终止：检查点保存 + 通知重新调度 NODE-391）、执行超时上限（超过说明卡死，锁应可被抢）。
- 场景分级：低风险任务（重跑无害——幂等即可，不需要 fencing）、高风险任务（资金/库存——必须 fencing + 事务性资源校验）；不要所有任务都上 fencing（复杂度成本）。
- 测试：锁失效场景测试（模拟持有者 GC 停顿 → 验证 fencing 拒绝旧 token 写入）。
```javascript
// fencing token + 条件写
const lock = await acquireLock('nightly-settle', { fencing: true }); // token=17
try {
  const r = await db.query(`update settle set status='done', fence=$1
    where fence=$2 and id=$3`, [17, 16, jobId]);                 // 只有最新 fence 能写
  if (r.rowCount === 0) throw new StaleFencing('锁已被接管，中止执行'); // 过期持有者自动退出
} finally { await releaseLock(lock); }
```
