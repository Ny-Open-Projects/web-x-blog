---
title: [NODE-186] BFF 的团队分工与边界治理怎么做？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-186：BFF 的团队分工与边界治理怎么做？
**答**：
- 契约先行：前后端先评审 OpenAPI（NODE-157），BFF 按契约 mock，并行开发；契约变更走 breaking 检测。
- 所有权：BFF 按端由对应前端团队维护；**通用能力下沉平台层**（鉴权/限流/日志/追踪做成内部 npm 包），各 BFF 一行接入，避免重造轮子。
- 边界判断：BFF 出现业务规则（if 金额判断）= 架构劣化信号，规则必须下沉微服务；BFF 频繁因业务逻辑改版说明在越界。
- 度量：每个 BFF 接口有 SLA（P99/错误率），与下游微服务同一大盘；BFF 数量与重复度定期治理。

```javascript
// 平台层沉淀：@company/bff-kit 一行接入公司标准
const kit = require('@company/bff-kit');

app.use(kit.tracing());                          // OTel 自动埋点（NODE-134）
app.use(kit.requestContext());                   // ALS + traceId（NODE-106/133）
app.use(kit.auth({ jwksUrl: env.JWKS_URL }));    // 统一鉴权（NODE-034）
app.use(kit.ratelimit({ strategy: 'token-bucket' })); // NODE-132
app.use(kit.aggregators());                      // 聚合/超时/降级工具（NODE-048）
// 治理检查（CI 可自动化）：
// ① BFF 目录里 grep 业务金额判断 → 警告越界
// ② kit 版本漂移检测 → 各 BFF 必须锁同主版本
// ③ 接口 SLA 看板 → P99 劣化自动 @owner
```
