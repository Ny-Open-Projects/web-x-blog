---
title: [NODE-946] 笔试题——实现限流双层联动（客户端自限+服务端强制）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-946：手写限流联动

**需求与边界**：
- 需求：双层限流（SCN-NODE-710/641）——① 客户端自限（per-下游令牌桶——SCN-NODE-710）；② 服务端强制（Redis Lua——SCN-NODE-731）；③ 双层的协调（客户端自限先行——服务端兜底，SCN-NODE-710）；④ 双层的监控（自限命中率/服务端拦截率——SCN-NODE-710）。
- 边界：① 自限的计数漂移（SCN-NODE-710 契约漂移）；② 服务端拦截的告警（SCN-NODE-710）；③ 双层的一致性（配额协商——SCN-NODE-822）。

**答**：
```javascript
// 客户端自限（SCN-NODE-710）
const clientQuota = tokenBucket({ rate: contract.qps });
async function callDownstream(args) {
  if (!clientQuota.tryTake()) { telemetry.count('self-limited'); return backoff(args); }
  try { return await rpc(args); }
  catch (e) { if (e.code === 'RATE_LIMITED') telemetry.count('server-limited'); throw e; }   // 服务端拦截（SCN-NODE-731）
}
// 双层监控
telemetry.aggregate(['self-limited', 'server-limited'], { by: 'downstream' });   // 自限率/拦截率
```

**评分点**:
- 客户端自限先行（SCN-NODE-710）。
- 服务端强制兜底（SCN-NODE-731）。
- 双层监控（自限率/拦截率——SCN-NODE-710）。
- 配额协商联动（SCN-NODE-822）。
