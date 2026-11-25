---
title: [PER-509] 性能基线（Baseline）如何建立、存储与更新？基线漂移了怎么办？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-509：性能基线（Baseline）如何建立、存储与更新？基线漂移了怎么办？

**答**：
- 基线的本质是"已知良好版本的指标快照"，要素包括：版本号、环境档位、各指标分位数值、样本量与采集时间；没有版本与环境维度的基线不可比。
- 存储建议入库（带 tag 的时序记录）而不是配置文件硬编码，才能支撑"任意两个版本对账"；每次发版自动写入新基线。
- 更新策略分三种：例行更新（随发版）、显著更新（大改版后重新跑全量建基线）、回滚更新（发现新基线是污染数据时回退到上一个可信 tag）。
- 漂移处理：先分清**真实漂移**（代码变了）与**环境漂移**（机房、CDN、数据分布变了），用固定对照组页面（不参与迭代的页面）校准环境漂移，校准不掉的才是代码回归。

```javascript

// 基线记录的 schema 与对账逻辑
const baseline = {
  tag: 'v2.3.0', env: 'moto-g4/fast3g', dataset: 'snapshot-2026Q4',
  metrics: { lcpP75: 2180, inpP75: 160, clsP75: 0.03 },
  samples: 240, ts: 1763600000000,
};
function diffBaseline(cur, base, tolerance = 0.05) {
  return Object.entries(cur.metrics).map(([k, v]) => {
    const b = base.metrics[k];
    const drift = (v - b) / b;
    return { k, drift: +(drift * 100).toFixed(1) + '%', regression: drift > tolerance };
  });
}
// 环境漂移校准：对照组页面（首页未改动）同步涨了 8% -> 全局环境因素，不是本次回归
```
