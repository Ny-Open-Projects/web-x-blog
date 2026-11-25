---
title: [PER-154] 性能修复项的优先级 ROI 矩阵怎么排？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-154：性能修复项的优先级 ROI 矩阵怎么排？

**答**：
- 三维打分：**影响**（影响页面数 × 用户占比 × 预期指标提升）、**成本**（人日）、**风险**（回归可能性），公式 `ROI = 影响分 / (成本分 + 风险分)`。
- 四象限：高 ROI"立即做"、中 ROI"本迭代做"、低 ROI 高成本"排期观察"、高成本低影响"不做"——敢写"不做"才算真排期。
- 打分要有数据支撑：影响分来自 RUM 切片，成本分来自历史类似项的实际人日，避免拍脑袋。
- 节奏：每季度重打一次分，矩阵是动态的；已完成的项回填真实收益，校准下次的估算。

```json
{
  "perf_fix_roi_matrix": {
    "scoring": {
      "impact": "影响页面数 x 用户占比 x 预期指标提升，0到10",
      "cost": "人日预估映射 0到10，越小越便宜",
      "risk": "回归风险 0到10"
    },
    "formula": "ROI = impact / (cost + risk)",
    "examples": [
      { "fix": "LCP 图片 preload 与 fetchpriority", "impact": 9, "cost": 1, "risk": 1, "roi": 4.5, "quadrant": "立即做" },
      { "fix": "删除未使用的历史 polyfill", "impact": 6, "cost": 2, "risk": 2, "roi": 1.5, "quadrant": "本迭代做" },
      { "fix": "全站迁移 HTTP3", "impact": 4, "cost": 8, "risk": 5, "roi": 0.31, "quadrant": "排期观察" },
      { "fix": "自研渲染引擎", "impact": 10, "cost": 10, "risk": 9, "roi": 0.53, "quadrant": "不做" }
    ],
    "cadence": "每季度重新打分，已完成项回填真实收益校准估算"
  }
}
```
