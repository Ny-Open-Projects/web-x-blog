---
title: [NODE-697] 幂等键存储设计（幂等表 TTL/清理）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-697：幂等键存储怎么做？
**答**：
- 存储选型：Redis（TTL 自动过期——快但需防清理时结果未落库）、DB 幂等表（持久+事务内原子插入——SCN-NODE-655 唯一约束）；混合——DB 权威 + Redis 加速。
- TTL 设计：幂等窗口 > 重试窗口（客户端最长重试周期——窗口短于重试期则重试穿过幂等层失效）；窗口不能无限长（存储成本——24h~72h 常见）。
- 结果存储语义：存「请求结果」而非「处理中」——重放返回原结果（处理中状态要处理：in-flight 锁——并发同 key 单飞，SCN-NODE-691）。
- 清理与审计：过期清理任务（SCN-NODE-667）、幂等命中统计（命中率/重复率——重复率异常 = 客户端重试异常信号）。
- 追问钩子：为什么「并发同 key 请求」是幂等设计最容易漏的分支——幂等表常见实现是「查无→插入→执行」；并发两请求都查无（竞态）→ 双执行——需要唯一约束兜底（SCN-NODE-655）或 in-flight 锁（第二个请求等待第一个的结果而非重复执行）——「重放幂等」与「并发幂等」是两个问题，分别要解。

```javascript
async function withIdempotency(key, fn) {
  const existing = await db.query('SELECT result, status FROM idem WHERE key=$1', [key]);
  if (existing?.status === 'DONE') return existing.result;      // 重放返回原结果
  if (existing?.status === 'RUNNING') await waitDone(key);      // 并发：等待首请求结果
  await db.insertIdem(key, 'RUNNING');                  // 唯一约束（并发只有一个成功）
  try { const r = await fn(); await db.finishIdem(key, r); return r; }
  catch (e) { await db.failIdem(key); throw e; }        // 失败释放（可重试）
}
```
