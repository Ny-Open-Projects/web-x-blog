---
title: [AGT-159] 跨进程/跨机的分布式多 Agent 任务分发怎么实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-159：跨进程/跨机的分布式多 Agent 任务分发怎么实现？
**答**：
- 架构组件：任务队列（Redis Stream/消息队列）承载任务单、worker 池按能力注册（谁擅长什么、并发上限）、结果回传（reply queue 或共享存储）+ 心跳与租约防「僵尸 worker 占任务」。
- 可见性超时是关键：worker 领任务即获租约，超时未 ack 任务自动重新入队（配合幂等键防重复执行）——单机内存队列做不到这一点。
- 任务亲和性：同一会话的多步任务尽量路由到同一 worker（利用其上下文缓存），无亲和需求才纯负载均衡；用会话哈希做一致性路由。
- 前端视角：分布式下的进度流要经中心事件总线（Redis Pub/Sub → SSE 网关）汇聚，任何 worker 的事件都能推到对的用户连接。

```typescript
// 基于 Redis Stream 的分布式 Agent 任务分发
import Redis from 'ioredis';
const redis = new Redis(process.env.REDIS_URL);
const STREAM = 'agent:tasks', GROUP = 'workers';

export async function registerWorker(workerId: string, caps: string[], concurrency = 3) {
  await redis.xgroup('CREATE', STREAM, GROUP, '0', 'MKSTREAM').catch(() => {}); // 幂等建组
  await redis.hset('agent:workers', workerId, JSON.stringify({ caps, concurrency, aliveAt: Date.now() }));
}

export async function dispatchTask(task: { id: string; cap: string; payload: unknown; idempotencyKey: string }) {
  await redis.xadd(STREAM, '*', 'task', JSON.stringify(task), 'visibleTimeout', '30000'); // 30s 租约
}

export async function workerLoop(workerId: string, myCaps: string[], handle: (t: any) => Promise<unknown>) {
  while (true) {
    const msgs = await redis.xreadgroup('GROUP', GROUP, workerId, 'COUNT', 3, 'BLOCK', 5000, 'STREAMS', STREAM, '>');
    for (const [, entries] of msgs ?? []) {
      for (const [msgId, fields] of entries) {
        const task = JSON.parse(fields[fields.indexOf('task') + 1]);
        if (!myCaps.includes(task.cap)) { await redis.xack(STREAM, GROUP, msgId); continue; } // 不匹配直接放行他人
        await redis.hset(`agent:lease:${task.id}`, workerId, Date.now());                      // 续租约
        try {
          const result = await handle(task);           // 幂等键去重由执行层保证
          await redis.xadd(`agent:results:${task.id}`, '*', 'result', JSON.stringify(result));
          await redis.xack(STREAM, GROUP, msgId);
        } catch (e) {
          await redis.xadd(STREAM, '*', 'task', JSON.stringify(task), 'retry', '1'); // 失败重入队
          await redis.xack(STREAM, GROUP, msgId);
        }
      }
    }
  }
}

// 事件汇聚：任一 worker 的进度经 Pub/Sub 推给对应会话的 SSE 连接
export function subscribeProgress(sessionId: string, cb: (e: unknown) => void) {
  const sub = redis.duplicate();
  sub.subscribe(`progress:${sessionId}`);
  sub.on('message', (_, m) => cb(JSON.parse(m)));
  return () => sub.disconnect();
}
```
