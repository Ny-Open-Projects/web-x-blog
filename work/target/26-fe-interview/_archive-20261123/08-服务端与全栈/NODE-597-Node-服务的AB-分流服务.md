---
title: [NODE-597] Node 服务的 AB 分流服务（实验平台核心）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-597：AB 分流服务
**答**:
- 分流核心：分层正交（实验层叠——不同层实验互不干扰：流量按层独立切分 ARC-277）、桶分配（uid hash → 层内桶——稳定性：同用户恒定桶）、放量平滑（占比提升不迁移已有桶——桶序排序法）。
- 分流服务化：分流 SDK/服务（各语言接入——分桶结果缓存（会话稳定））、实验配置下发（实验注册：变量/流量/指标——配置中心热更）、强制分流（白名单/调试模式——测试工具）。
- 一致性保障：跨端同桶（uid 为分流因子——未登录场景设备 ID 桶（登录后 merge 处理——ARC-572））、分流与灰度联动（灰度标签与实验桶共存——正交设计）。
- 数据质量：分桶正确性监控（流量比例实测 vs 配置——偏差告警）、曝光一致性（用户中途变桶检测——数据污染防护）、SRM 检验（样本比失衡自动告警——实验有效性）。
- 治理：实验冲突检测（同层多实验重叠流量评估）、实验生命周期管理（ARC-555 闭环）。
```javascript
// 分流服务核心
async function assign(uid, experimentId) {
  const exp = await experiments.get(experimentId);               // {layer, buckets, traffic}
  const bucket = hash(`${exp.layer}:${exp.salt}:${uid}`) % exp.totalBuckets;
  if (bucket >= exp.rolloutBuckets) return 'control';            // 未放量桶 → control
  return bucketToVariant(bucket, exp.variants);                  // 桶 → 变体
}
// SRM 监控：observedRatio vs configuredRatio → chi2 > 3.84 告警
```
