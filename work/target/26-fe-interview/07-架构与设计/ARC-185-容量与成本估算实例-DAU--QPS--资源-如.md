---
title: [ARC-185] 容量与成本估算实例（DAU → QPS → 资源）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-185：容量与成本估算实例（DAU → QPS → 资源）如何设计？
**答**：
- 推导链固定五步：DAU → 峰值 QPS（DAU×人均请求数÷活跃时长，乘峰值系数 3-5x）→ CDN 带宽（峰值 QPS×平均响应体×8bit）→ 服务端容器（QPS÷单实例吞吐×冗余 1.5）→ 缓存与存储（命中率目标反推缓存容量）。
- 前端重点算清"带宽与 CDN 成本"：静态资源 + 图片 + API 响应是三块大头，图片通常占 70%+，所以图片格式/尺寸策略直接决定成本曲线。
- 估算要给区间与敏感度：假设参数全部列出（人均 PV、峰值系数、压缩率），结论给 P50/P90 两档——精确的错误不如粗略的正确加敏感性分析。
- 大促场景另算：活动峰值模型独立建模（预热缓存、弹性扩容窗口、降级预案的成本收益）。

```typescript
// 容量估算计算器（输入假设 → 输出资源与成本）
interface Assumptions {
  dau: number;                  // 100 万
  pageViewsPerUser: number;     // 人均 PV 8
  activeHours: number;          // 日活跃时长分布 10h
  peakFactor: number;           // 峰值系数 4
  avgApiResponseKB: number;     // 15KB（gzip 后）
  avgImageKB: number;           // 80KB（每 PV 平均图片传输）
  cacheHitRate: number;         // 0.85
}

function estimate(a: Assumptions) {
  const totalPV = a.dau * a.pageViewsPerUser;                    // 800 万 PV
  const avgQPS = totalPV / (a.activeHours * 3600);               // ≈ 222 QPS 均值
  const peakQPS = avgQPS * a.peakFactor;                         // ≈ 889 QPS 峰值（P50 假设）
  // 大促按峰值系数 10 单算：≈ 2222 QPS（P90 场景）
  const cdnBandwidthMbps = (peakQPS * (a.avgApiResponseKB * (1 - a.cacheHitRate) + a.avgImageKB) * 8) / 1000 / 1000;
  // ≈ (889 × (2.25 + 80) × 8) / 1e6 ≈ 0.58 Gbps，图片占 97% → 图片优化是成本杠杆
  const originQPS = peakQPS * (1 - a.cacheHitRate);              // 回源 ≈ 133 QPS
  const instances = Math.ceil((originQPS * 1.5) / 300);          // 单实例 300 QPS，冗余 1.5 → 1 台起，双可用区 2 台
  return {
    totalPV, avgQPS: round(avgQPS), peakQPS: round(peakQPS),
    cdnBandwidthMbps: round(cdnBandwidthMbps),
    originQPS: round(originQPS), instances,
    costLevers: [                                                // 成本敏感度排序
      '图片：AVIF 渗透率每 +10%，带宽 -6%（最大杠杆）',
      '缓存命中率每 +5%，回源带宽 -33%',
      'JS bundle 每 -100KB，冷启动流量成本线性下降',
    ],
  };
}
// 纪律：所有假设参数入表可调，结论给 P50/P90 双档；大促峰值单独建模
```
