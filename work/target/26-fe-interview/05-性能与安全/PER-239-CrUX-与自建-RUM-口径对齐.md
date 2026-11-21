---
title: [PER-239] 自建 RUM 与 CrUX 数据差了 40%，怎么排查与对齐口径？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-239：自建 RUM 与 CrUX 数据差了 40%，怎么排查与对齐口径？

**答**：
- 按嫌疑度排查清单：① 采样偏差——RUM 只在 JS 跑起来才上报，白屏/极慢用户根本没上报成功，天然偏快；CrUX 无此偏差。② 指标实现差异——LCP 是否取最后候选、CLS 是否过滤 hadRecentInput、INP 的 durationThreshold 是否设置。③ 聚合差异——分位数算法（精确 vs 分桶）、窗口（28 天滚动 vs 当天）、页面粒度。④ 浏览器覆盖——CrUX 只有 Chrome，RUM 全量。⑤ 设备/地域分布差异。
- 对齐步骤：先只比"Chrome + navigate + 手机"切片；再对指标实现做双跑校验（同一页面同时用 web-vitals 库与自己实现上报对比）；最后查聚合窗口与分桶。
- 残差管理：对齐后仍会有 5~10% 残差（采集时机、上报丢失），设阈值告警而不是追求绝对相等。

```javascript
// 双跑校验：官方 web-vitals 库 vs 自实现，同一页面并行上报
import { onLCP, onCLS, onINP } from 'web-vitals';
onLCP(m => sendBeacon('/rum/calib', JSON.stringify({ src: 'official', metric: 'LCP', v: m.value })));
trackLCP(m => sendBeacon('/rum/calib', JSON.stringify({ src: 'custom',   metric: 'LCP', v: m.value })));
// 服务端按 src 分组对比分布：中位差 > 5% 说明自实现有口径 bug，
// 常见差异点：没取最后 LCP 候选 / buffered: true 缺失 / hidden 后仍采集
```
