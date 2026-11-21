---
title: [NODE-578] Node 服务的开放平台（限流计费/分级配额）如何运营？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-578：开放平台限流计费
**答**:
- 接入分级：免费层/标准层/企业层（各层配额：QPS/日调用/数据范围——NODE-439 配额）、审核接入（appKey 申请——用途审核）。
- 计量计费链路：调用计量（NODE-401 幂等计量事件）→ 聚合（按 appKey/接口/天）→ 计费（套餐内/超量阶梯——价格引擎）→ 账单与预警（配额 80% 预警——升级引导）。
- 限流实现：appKey 维度令牌桶（NODE-360）+ 并发限制（防打爆）+ 日配额硬限（超了 429 到次日）、突发保护（bucket burst——短时突发容忍）。
- 防滥用：签名与防重放（NODE-576/458）、爬取模式检测（NODE-458 crawlPattern）、异常用量告警（盗用 appKey 检测——IP/行为突变）。
- 运营指标：接入数/活跃率/调用量趋势/收入（开放平台健康）、工单分类（接入难/限流误伤——DX 改进 ARC-399）。
```javascript
// 开放 API 网关限流
const limits = planOf(appKey);                                   // {qps: 100, daily: 1e6, burst: 150}
const ok = await tokenBucket.take(`open:${appKey}`, { rate: limits.qps, burst: limits.burst })
  && await dailyQuota.take(`open:${appKey}`, limits.daily);
if (!ok) return 429({ retryAfter, upgrade: pricingPage });
await meter('openapi.call', { appKey, route });                  // 计量事件
```
