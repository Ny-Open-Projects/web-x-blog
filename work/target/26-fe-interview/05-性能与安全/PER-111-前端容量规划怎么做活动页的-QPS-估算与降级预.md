---
title: [PER-111] 前端容量规划怎么做？活动页的 QPS 估算与降级预案如何制定？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-111：前端容量规划怎么做？活动页的 QPS 估算与降级预案如何制定？

**答**：
- 容量估算链条：**预估 PV -> 峰值 QPS**（经验公式：峰值 QPS ≈ PV / 86400 * 峰值系数，大促峰值系数 20-50）-> 静态资源 CDN 带宽（页面均重 * QPS）-> API QPS 按接口画像拆分。
- 前端侧的容量动作：静态资源全量 CDN 化并预热、API 侧网关限流与队列化、**降级预案清单化**（每类资源挂了展示什么）。
- 压测配合：预发环境按 1.5 倍峰值压测，观察首屏 API 的 P99 与 CDN 回源量；按压测结果调整预热与缓存 TTL。
- 降级预案分级：静态兜底（缓存页/骨架）-> 功能降级（关推荐/关实时库存）-> 熔断排队（虚拟等待室）。

```javascript
// 活动页容量估算器：PV -> 峰值 QPS -> CDN 带宽
function capacityPlan({ pv, peakFactor = 30, pageWeightKB = 800, apiCallsPerPv = 8 }) {
  const peakQps = Math.ceil((pv / 86400) * peakFactor);        // 峰值 QPS
  const cdnBandwidthGbps = +(peakQps * pageWeightKB * 8 / 1e6).toFixed(2); // 静态带宽
  const apiPeakQps = peakQps * apiCallsPerPv;                  // 接口侧按画像放大
  return {
    peakQps,
    cdnBandwidthGbps,
    apiPeakQps,
    suggestions: [
      cdnBandwidthGbps > 20 ? '带宽超 20Gbps：提前 24h CDN 预热 + 图片降档' : '带宽可承受',
      apiPeakQps > 50000 ? 'API 峰值高：网关限流 + 页面数据静态化到 CDN' : 'API 可承受',
      '配置降级：关推荐位 -> 关实时库存 -> 静态兜底页',
    ],
  };
}
console.log(capacityPlan({ pv: 50_000_000, peakFactor: 40 }));
```

```javascript
// 前端降级开关模块：配置中心下发，按级别自动降级
const DEGRADE_LEVELS = ['normal', 'level1', 'level2', 'level3']; // 逐步加深的降级

function applyDegrade(level) {
  const flags = {
    normal:  { recommend: true, realtimeStock: true, video: true },
    level1:  { recommend: false, realtimeStock: true, video: true },  // 关推荐
    level2:  { recommend: false, realtimeStock: false, video: true }, // 库存改快照
    level3:  { recommend: false, realtimeStock: false, video: false },// 静态兜底页
  }[level];
  window.__degrade = { level, ...flags };
  document.body.dataset.degrade = level;
}

fetch('/api/app-config', { cache: 'no-store' }) // 配置中心强实时
  .then((r) => r.json())
  .then((c) => applyDegrade(c.degradeLevel))
  .catch(() => applyDegrade('level3')); // 配置中心都不可达：直接最深降级
```

## 十八、综合案例与收束
