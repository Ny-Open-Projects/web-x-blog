---
title: [MFW-622] Edge 函数的冷启动预热策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-622：Edge 函数冷启动预热

**答**:
- 冷启动预热的三种机制：1) **平台级预热池**（min isolate 常驻——平台自动 RBL-518）；2) **应用级预热**（cron ping 热点路由——isolate 驻留：请求驱动的预热（定时打 /health 或热点页——让 isolate 不休眠））；3) **代码级预热**（顶层轻初始化（连接池/字典载入——isolate 启动时就绪））。
- 预热的效果与成本：cron ping = 常驻实例成本（每区域一个 isolate 常驻——费用）；「预热的覆盖范围」：全球 N 区域 × 热点路由 = ping 矩阵（全区域预热成本高——按流量分区域预热）。
- 冷启动的监控：cold-start 标记（平台 header x-vercel-id 首次请求——区分冷热请求的 p95）——冷启动率的 SLO（RBL-904）；「预热的有效性验证」：冷启动率下降 = 预热 ROI。
- 追问钩子：为什么「应用级预热」要按区域流量分配而非全区域？——全区域预热 = N 区域常驻成本（区域越多成本线性）；流量分布不均（80% 用户在 20% 区域——按流量预热 = 覆盖 80% 用户 × 20% 成本）；「预热 ROI = 覆盖的用户请求 × 冷启动节省 − 常驻成本」——与 CDN 节点选择、失效加权的流量优先原则（RBL-600）同构：资源的流量加权分配。

```typescript
// 预热的 cron ping（按流量分区）
const REGIONS_BY_TRAFFIC = [
  { region: 'iad1', weight: 0.4 }, { region: 'sfo1', weight: 0.25 },
  { region: 'fra1', weight: 0.2 }, { region: 'sin1', weight: 0.15 },
];
// cron: 每分钟 ping（keep-alive）
for (const { region } of REGIONS_BY_TRAFFIC.slice(0, 2)) {   // Top 2 区域预热
  await fetch(`https://${region}.app.com/health`, { headers: { 'x-preheat': '1' } });
}
// 冷启动率监控
function coldStartRate(requests: { isCold: boolean }[], windowMin = 60) {
  const cold = requests.filter(r => r.isCold).length;
  const rate = cold / requests.length;
  if (rate > 0.05) warn(`冷启动率 ${(rate * 100).toFixed(1)}% > 5%——预热覆盖不足`);
  return rate;                                           // SLO: <5% RBL-904
}
// 代码级预热：顶层轻初始化
const routes = new Map([...]);                           // 顶层常量：isolate 启动即就绪
// 反模式：顶层 await connectDB()                        // 每次冷启动付费
// 修正：请求时懒连接 + 连接复用（DO/外置连接池 RBL-517）
```
