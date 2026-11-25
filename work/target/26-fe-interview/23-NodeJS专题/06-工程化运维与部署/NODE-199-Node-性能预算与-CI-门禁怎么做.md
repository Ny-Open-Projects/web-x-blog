---
title: [NODE-199] Node 性能预算与 CI 门禁怎么做？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-199：Node 性能预算与 CI 门禁怎么做？
**答**：
- 预算维度：接口 P99/吞吐（NODE-140 基线）、事件循环 lag、启动时间（冷启动 < 3s）、内存水位、依赖体积。
- 门禁机制：CI 里程序化压测（autocannon）对比基线，P99 恶化 20% 或吞吐跌 20% 阻断合并（NODE-100 方法论固化）。
- 防"温水煮青蛙"：基线入库形成趋势曲线，每次小劣化都被拦住，而不是等事故。
- 门禁要快：压测 30s 内完成，跑在预发同规格环境，环境差异会造成误报。

```javascript
// bench-gate.js —— CI 性能门禁
const autocannon = require('autocannon');
const BASELINE = { p99: 250, qps: 2000 };            // NODE-100 沉淀的基线

async function gate() {
  const r = await autocannon({
    url: 'http://localhost:3000/api/home',
    connections: 100, duration: 30,
  });
  const fail = [];
  if (r.latency.p99 > BASELINE.p99 * 1.2)
    fail.push(`P99 恶化 ${r.latency.p99}ms 超基线 20%`);
  if (r.requests.average < BASELINE.qps * 0.8)
    fail.push(`吞吐下降 ${r.requests.average} 低于基线 80%`);
  if (fail.length) { console.error('性能门禁未过:', fail); process.exit(1); }
  console.log(`通过: P99=${r.latency.p99}ms QPS=${r.requests.average}`);
  // 趋势入库：{ commit, p99, qps, ts } → Grafana 看劣化曲线
}
gate();
// CI 配置：启动服务 → 等就绪 → node bench-gate.js → 通过才允许合并
```
