---
title: [929] 两个 Agent 同时调同一个工具（如写同一文件）怎么办
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 并发控制]
type: 面试题
---

## 929：两个 Agent 同时调同一个工具（如写同一文件）怎么办

**答**：
- 资源分级：只读工具可并发；写类工具按资源 key 加互斥锁（文件路径、表行、外部 API）；外部副作用工具（发消息、下单）必须幂等 + 锁。
- 死锁预防：Agent 单次最多持一把锁、锁带 TTL 自动释放、获取顺序统一按 key 排序。
- 冲突解决策略：默认「后者失败重试」而不是「后写覆盖」，被锁阻塞的 Agent 收到明确错误后重规划，比静默覆盖安全。
- 追问钩子：Agent 循环里忘记释放锁怎么办？——TTL + 心跳续期双保险，Agent 崩溃锁也能到期释放。

```ts
const locks = new Map<string, { owner: string; expire: number }>();
async function withLock(key, agent, fn, ttlMs = 30000) {
  const now = Date.now();
  const cur = locks.get(key);
  if (cur && cur.expire > now) throw new LockBusy(key, cur.owner);
  locks.set(key, { owner: agent, expire: now + ttlMs });
  try { return await fn(); }
  finally { if (locks.get(key)?.owner === agent) locks.delete(key); } // TTL 兜底误删
}
```
