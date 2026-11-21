---
title: [NODE-061] 健康检查端点如何设计（liveness 与 readiness 的区别）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-061：健康检查端点如何设计（liveness 与 readiness 的区别）？
**答**：
- K8s 双探针：**liveness**（`/healthz`）——进程活着吗？失败则重启容器，**必须是零依赖的自检**（不能因为 Redis 挂了就重启 Node，越探越死）；**readiness**（`/healthz/ready`）——能接流量吗？失败只摘流量不重启，可包含关键依赖检查与发布状态。
- 补充 `startup` 探针（慢启动应用）与 `/healthz/startup`。响应体应包含版本号、uptime、依赖状态明细（排障利器）。
- 反模式：liveness 里查 DB（DB 抖动 → 全部容器被重启 → 集群雪崩）；健康检查端点本身要轻量、无鉴权、有响应超时。

```javascript
const startedAt = Date.now();
const VERSION = process.env.GIT_COMMIT_SHA || 'dev';
const deps = {
  redis: () => redis.ping().then(() => true).catch(() => false),
  mysql: () => pool.query('SELECT 1').then(() => true).catch(() => false),
};

// liveness：只查自己，绝不停外部依赖
app.get('/healthz', (req, res) => {
  res.status(200).json({ status: 'alive', version: VERSION, uptime: Date.now() - startedAt });
});

// readiness：检查关键依赖（带 1s 超时，防止挂起）
app.get('/healthz/ready', async (req, res) => {
  if (state.shuttingDown) return res.status(503).json({ ready: false, reason: 'draining' });
  const results = {};
  await Promise.race([
    Promise.all(Object.entries(deps).map(async ([name, check]) => {
      results[name] = await check();
    })),
    new Promise((r) => setTimeout(r, 1000)),
  ]);
  const ok = Object.values(results).every(Boolean);
  res.status(ok ? 200 : 503).json({ ready: ok, version: VERSION, deps: results });
});
```

```yaml
# k8s deployment 探针配置片段
livenessProbe:
  httpGet: { path: /healthz, port: 3000 }
  initialDelaySeconds: 10
  periodSeconds: 10
  failureThreshold: 3
readinessProbe:
  httpGet: { path: /healthz/ready, port: 3000 }
  initialDelaySeconds: 5
  periodSeconds: 5
  failureThreshold: 2
  successThreshold: 1
startupProbe:
  httpGet: { path: /healthz, port: 3000 }
  failureThreshold: 30      # 30 × 10s = 最长 5 分钟启动窗口
  periodSeconds: 10
```
