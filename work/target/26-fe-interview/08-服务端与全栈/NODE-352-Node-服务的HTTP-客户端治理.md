---
title: [NODE-352] Node 服务的 HTTP 客户端（调用下游）治理如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-352：Node 服务的 HTTP 客户端治理
**答**:
- 客户端五要素：超时（连接+响应+整体预算，禁默认无限）、重试（幂等 GET 有限重试退避；POST 用幂等键才可重试）、连接池（keepAlive agent 复用，防 TIME_WAIT 暴涨）、熔断（连续失败熔断快速失败，half-open 探测）、降级（fallback 数据）。
- 超时分层：per-attempt timeout 与总预算（含重试）分开——重试后总耗时可能超 SLA，聚合层预算分配（ARC-447）。
- DNS：dns 缓存 TTL 与故障切换（内网服务域名解析失败是常见事故），node 的 dns lookup 与 keepAlive agent 配合。
- 大响应：流式接收（不整包 buffer）、大小上限（防下游异常返回 GB 级拖爆内存）。
- 可观测：下游调用指标按目标服务分桶（QPS/错误率/P95/重试率），trace 续链（NODE-291），慢下游自动进容量评估。
```javascript
const https = require('https');
const agent = new https.Agent({ keepAlive: true, maxSockets: 100 });  // 连接复用
async function callDownstream(url, { timeout = 2000, retries = 2 } = {}) {
  for (let i = 0; ; i++) {
    try {
      return await fetch(url, { agent, signal: AbortSignal.timeout(timeout),
        headers: { traceparent: currentTraceHeader() } });
    } catch (e) {
      if (i >= retries || !retryable(e)) throw e;
      await sleep(2 ** i * 200);
    }
  }
}
```
