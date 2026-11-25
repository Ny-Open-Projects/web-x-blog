---
title: [NODE-618] Node 服务的接口慢日志（应用层慢请求归因）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-618：接口慢日志
**答**:
- 应用层慢日志定位：DB 慢查询日志只到 SQL——应用层慢日志补全"慢在哪一段"（中间件链/业务计算/序列化/外部调用——分段计时）。
- 实现：分段计时器（请求生命周期埋点：parse→biz→db→ext→serialize——各段耗时记录 NODE-421 上下文）、慢阈值分级（预算层级 NODE-489——各 tier 独立阈值）、采样与保真（慢请求 100% 记录 + 关键上下文：route/参数摘要/traceId——NODE-468）。
- 归因输出：慢请求结构化记录（分段耗时 top——自动归因到段：'ext:recommend 400ms 占 80%'——NODE-501 瀑布简化版）、关联证据（trace 链接——下钻入口）。
- 与治理联动：慢日志 → 慢接口清单（NODE-518 治理数据源）、告警（新慢请求模式——突增告警）。
- 度量：慢请求率趋势、分段耗时分布（哪段是共性瓶颈——横向分析）。
```javascript
// 分段计时中间件
app.use((ctx, next) => ctx ALS.run({ segments: {} }, next));
const mark = (name) => (ctx) => ctx.segments[name] = Date.now();
// 流程：mark('parse') → mark('bizStart') ... → 请求结束：
const segs = diff(ctx.segments);                                  // {parse:3, biz:120, ext:400}
if (total > budget(ctx.route)) slowLog.write({ route: ctx.path, segs, traceId });
```
