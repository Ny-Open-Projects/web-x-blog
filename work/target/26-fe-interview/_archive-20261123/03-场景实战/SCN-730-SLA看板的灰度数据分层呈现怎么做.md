---
title: [SCN-730] SLA 看板的灰度/版本维度数据怎么分层呈现？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-730：版本维度数据分层呈现怎么做？
**答**：
- 版本切片：所有 SLI 按发布版本维度拆分，看板默认展示「全量 + 当前灰度版本」双线对比——灰度版本的 P95 独立可见，劣化早于全量发现。
- 流量加权提示：灰度版本流量小时（1%）P95 置信度低，面板显示样本量与置信带，防止小样本误判。
- 版本间对比表：最近 5 个版本的关键指标对比 + 差异显著性标注（样本量足够才标注差异）。
- 自动归档：版本退出灰度后其切片数据保留 30 天供回溯，之后并入全量趋势。
- 追问钩子：灰度版本和全量指标差多少才算劣化——显著性检验（样本量加权）而非固定阈值；流量小时用贝叶斯方法融合先验，避免 1% 流量的随机波动触发误判。

```javascript
function versionSlice(metric, releases) {
  return releases.map(r => ({
    version: r.id, trafficPct: r.traffic,
    p95: query(metric, { version: r.id }),
    ci: confidenceInterval(r.traffic),               // 小流量置信带宽
    significant: r.traffic > 0.05,                   // 5% 以上流量才做显著性标注
  }));
}
```
