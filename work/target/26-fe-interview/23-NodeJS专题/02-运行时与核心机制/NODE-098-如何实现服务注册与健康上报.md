---
title: [NODE-098] 如何实现服务注册与健康上报？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-098：如何实现服务注册与健康上报？
**答**：
- 场景：自建多实例 BFF（无 K8s 服务发现）时，下游/网关需要知道"有哪些活着的实例"。实例启动时注册（IP:port/权重/metadata），**定时心跳续期**，宕机后 TTL 过期自动摘除。
- Redis 实现：`SET instance:{service}:{id} JSON EX 10` + 每 5s 续期；发现方 `KEYS/SCAN instance:{service}:*` 或维护哈希集合；优雅退出主动注销。
- K8s 场景则交给 Service/EndpointSlice + readiness 探针（NODE-061），自研注册用于混部/虚机环境。

```javascript
// 服务注册客户端
class ServiceRegistry {
  constructor({ serviceName, port, heartbeatMs = 5000 }) {
    this.serviceName = serviceName;
    this.instanceId = `${os.hostname()}:${port}`;
    this.meta = { port, version: process.env.APP_VERSION, zone: process.env.ZONE };
    this.heartbeatMs = heartbeatMs;
    this.timer = null;
  }

  async register() {
    await this.renew();
    this.timer = setInterval(() => this.renew().catch((e) =>
      log.error({ event: 'heartbeat_failed', msg: e.message })), this.heartbeatMs);
    this.timer.unref();
  }

  async renew() {
    // TTL 10s = 2 个心跳周期：连续 2 次心跳失败即被摘除
    await redis.setex(`instance:${this.serviceName}:${this.instanceId}`, 10, JSON.stringify({
      ...this.meta, lastSeen: Date.now(), healthy: await this.selfCheck(),
    }));
  }

  async selfCheck() {
    try { await fetch(`http://127.0.0.1:${this.meta.port}/healthz`, { signal: AbortSignal.timeout(500) }); return true; }
    catch { return false; }
  }

  async deregister() {          // 优雅退出时主动注销（不等 TTL）
    clearInterval(this.timer);
    await redis.del(`instance:${this.serviceName}:${this.instanceId}`);
  }
}

// 服务发现：客户端负载均衡
async function discover(serviceName) {
  const keys = await redis.scanStream({ match: `instance:${serviceName}:*` });
  const instances = [];
  for await (const batch of keys) {
    const values = await redis.mget(...batch);
    instances.push(...values.filter(Boolean).map((v) => JSON.parse(v)).filter((i) => i.healthy));
  }
  return instances;   // 调用方按 zone 亲和 / 轮询 / 随机选择
}
```
