---
title: [NODE-741] 笔试题——实现结构化日志中间件（采样/脱敏/慢请求）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-741：手写日志中间件

**需求与边界**：
- 需求：访问日志中间件（SCN-NODE-646）——① 结构化输出（traceId/耗时/状态码/关键维度——ALS 注入）；② 采样策略（慢请求/错误全量、正常 10%——SCN-SLA-724 分层）；③ 敏感字段脱敏（redact 白名单——SCN-NODE-698）；④ 异步写入（不阻塞事件循环——pino sync:false）。
- 边界：① res.on finish 时机（响应完成后拿最终状态码）；② 采样决策在响应完成时（慢请求信息只在完成后可知）；③ body 不进日志（大 body 内存 + 敏感——只进摘要字段）。

**答**：
```javascript
function accessLog(logger, { sample = 0.1, slowMs = 500 } = {}) {
  return (req, res, next) => {
    const start = performance.now();
    res.on('finish', () => {
      const ms = Math.round(performance.now() - start);
      const slow = ms > slowMs, err = res.statusCode >= 500;
      const sampled = slow || err || Math.random() < sample;   // 分层采样（SCN-SLA-724）
      if (!sampled) return;
      const s = ctx.getStore() ?? {};
      logger[slow || err ? 'warn' : 'info']({
        traceId: s.traceId, tenant: s.tenant,
        method: req.method, path: req.route?.path ?? req.path,   // 模板路径（非原始——聚合友好）
        status: res.statusCode, ms,
        ua: req.headers['user-agent']?.slice(0, 50),
        // body 不进日志（敏感+内存）；redact 由 pino serializer 处理
      }, 'access');
    });
    next();
  };
}
// pino 配置：异步 + redact（SCN-NODE-646/698）
const logger = pino({ redact: { paths: ['*.phone', '*.token'], censor: '[REDACTED]' },
  transport: undefined }, pino.destination({ sync: false }));
```

**评分点**:
- 分层采样（慢/错全量、正常采样——SCN-SLA-724）。
- route 模板路径（聚合友好——非原始 URL）。
- redact 白名单 + 异步写（SCN-NODE-646/698 双合规）。
- body 不进日志（敏感 + 内存红线）。
