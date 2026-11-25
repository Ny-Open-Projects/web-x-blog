---
title: [NODE-448] Node 服务的接口调用方画像（谁在用我的接口）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-448：接口调用方画像
**答**:
- 画像维度：每个 route 的调用方集合（服务名/端类型/版本分布）、调用量与趋势、错误率（调用方视角——是下游真挂还是某调用方用法错误）、参数分布（某调用方总传异常参数 → 定向沟通）。
- 数据来源：网关访问日志（caller 头 NODE-369）聚合、trace span 属性（调用方身份 span tag）、开放 API 的 appKey 维度（NODE-397）。
- 用途：废弃流程（NODE-440 等谁迁移）、容量协商（大调用方扩容联动 NODE-405）、异常定位（错误集中在某调用方 → 参数或版本问题）、计费（NODE-401 按 appKey）。
- 落地形态：服务画像卡扩展（NODE-427）：每个接口的"调用方表格"自动生成；变更评审自动附（NODE-447）。
- 治理：未知调用方识别（没有身份的调用——裸调/爬虫识别与引导注册）、僵尸调用方（30 天零流量 → 废弃推进）。
```javascript
// 调用方画像聚合
async function routeCallers(route, { days = 7 }) {
  return logAgg.groupBy(['route', 'caller.svc', 'caller.version'], {
    filter: { route, since: days },
    metrics: { qps: avg(rps), err: rate(5xx), p95: p95(dur) } });
}
// 未知调用方：caller.svc 缺失 → 打 'unknown' 标签 → 安全盘点（是否爬虫/未注册服务）
```
