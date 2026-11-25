---
title: [PER-597] 监控数据的标签（tag/维度）体系怎么设计？维度爆炸导致查询变慢怎么办？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-597：监控数据的标签（tag/维度）体系怎么设计？维度爆炸导致查询变慢怎么办？

**答**：
- 标签设计原则：**有限基数**（每个 tag 的取值可枚举，如设备档 3 档、网络 4 档；URL、用户 id 这类高基数字段绝不做 tag，进明细当属性）、**查询导向**（tag 是你下钻查询的轴，不查的别加）、**版本演进**（tag 集合变更要走迁移，新老数据可比性标注）。
- 维度爆炸的治理：高基数 tag 会让时序库 series 数量爆炸（成本与查询劣化）；治理手段——归并取值（URL 归并到路由模板）、维度白名单（超过 8 个 tag 的指标要评审）、预聚合替代实时下钻（常用组合做物化视图）。
- 明细与聚合分离：下钻需求走明细（点击 p75 -> 查原始样本），聚合层只保留低基数 tag——查询体验和成本两头兼顾。
- 度量：series 数量、单查询 p95 耗时、物化视图命中率，进监控自身的成本看板。

```javascript

const tagPolicy = {
  allowed: { deviceTier: ['low', 'mid', 'flag'], net: ['3g', '4g', 'wifi', 'offline'],
    route: '/list|/detail|...(路由模板，非原始 URL)', bucket: 'gray|control' },
  forbidden: ['rawUrl(高基数->进明细属性)', 'userId', 'traceId', 'timestamp-as-tag'],
  rules: {
    maxTags: 8,                       // 超过需评审
    materialize: ['route×deviceTier', 'route×bucket'],      // 常用组合预聚合
    drilldown: '分位数下钻走明细库，聚合层只存低基数 tag',
  },
  health: ['series 数量 < 100w', '查询 p95 < 2s', '物化命中率 > 80%'],
};
console.log(tagPolicy.rules.drilldown);
```
