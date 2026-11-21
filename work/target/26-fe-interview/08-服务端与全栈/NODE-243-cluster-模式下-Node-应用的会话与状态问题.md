---
title: [NODE-243] cluster 模式下 Node 应用的会话与状态问题？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-243：cluster 模式下 Node 应用的会话与状态问题？
**答**:
- 核心问题：多 worker 内存独立——内存态 session/缓存/限流计数器各一份且不一致。
- 原则：cluster 下**进程内状态不可依赖**——session/缓存/计数器全部外置（Redis/集中缓存），本地内存只做无一致性要求的辅助缓存（NODE-175 RBAC 服务设计原则）。
- 需要进程间广播时：ClusterIPC（cluster.ipc）/外部 pub-sub（Redis pub/sub）——广播限流阈值变更等配置类消息。
- sticky session：WS 场景 Nginx ip_hash 或 cookie 粘滞——与 NODE-240 呼应。

```javascript
// 反模式：内存限流器
// const hitCount = new Map();  // 多 worker 各自计数 → 限流上限 ×N 失效
// 正解：Redis 集中计数
async function rateLimit(uid, limit) {
  const key = `rl:${uid}:${Date.now() / 60000 | 0}`;
  const n = await redis.incr(key);
  if (n === 1) await redis.expire(key, 60);
  return n <= limit;
}
// 配置广播（cluster 内）
process.on('message', (msg) => msg.type === 'config' && reloadConfig(msg.data));
if (cluster.isPrimary) workers.forEach(w => w.send({ type: 'config', data: newCfg }));
```
