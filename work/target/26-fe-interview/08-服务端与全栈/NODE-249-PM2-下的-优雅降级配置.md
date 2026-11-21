---
title: [NODE-249] PM2 下的优雅降级配置？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-249：PM2 下的优雅降级配置？
**答**:
- 过载保护链：请求队列积压（指标）→ 主动降级（关非核心接口 NODE-052）→ 最后兜底（Nginx 返回静态兜底页/限流 503）。
- PM2 层联动：max_memory_restart 是最后防线（异常时回收实例）——但不能依赖它做常态降级（重启期间 QPS 损失）。
- 应用侧分级：health 探针返回负载水位（elu/队列长度）→ 网关据此限流（NODE-28x 健康探针）。
- 大促预案（ARC-258 服务端版）：降级开关进配置中心（NODE-150），PM2 reload 不必要（配置热更）。

```javascript
// 应用侧水位上报（供网关决策）
app.get('/__health', (req, res) => {
  const elu = eventLoopUtilization().utilization;
  const rss = process.memoryUsage().rss / 1024 / 1024;
  const status = elu > 0.85 || rss > 500 ? 503 : 200;    // 过载：让 LB 摘流
  res.status(status).json({ elu, rss, degraded: degraded.active });
});
// Nginx：max_fails=2 fail_timeout=10s → 摘流自动恢复
// upstream node_api { server 127.0.0.1:3000 max_fails=2 fail_timeout=10s; }
```
