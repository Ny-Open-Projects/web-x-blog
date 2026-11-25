---
title: [PER-158] Web 图表库性能对比要素？canvas/svg 选型与数据量阈值？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-158：Web 图表库性能对比要素？canvas/svg 选型与数据量阈值？

**答**：
- 四个决策轴：**数据点数量**、**交互复杂度**（tooltip/缩放/框选）、**更新频率**、**导出与无障碍需求**。
- 经验阈值：≤2000 点且重交互选 SVG（DOM 事件模型天然支持）；2000~10 万点或高频更新选 Canvas（无 DOM 开销）；>10 万点或实时波形上 WebGL + LTTB 降采样。
- 阈值必须**真机实测**：桌面端测出的拐点不能直接套到移动端 50 分位设备；同一库不同版本差异也可能翻倍。
- 混合方案常见：坐标轴/图例用 SVG 保文本语义与无障碍，数据系列用 Canvas 保性能。

```json
{
  "chart_selection_matrix": {
    "decision_axes": ["数据点数量", "交互复杂度", "更新频率", "导出与无障碍需求"],
    "rules": [
      { "condition": "点数小于等于 2000 且需要 tooltip 与局部缩放", "choice": "svg 图表库", "reason": "DOM 事件模型天然支持交互" },
      { "condition": "点数 2000 到 10 万或更新频率大于等于 10fps", "choice": "canvas 图表库", "reason": "无 DOM 开销，重绘成本线性" },
      { "condition": "点数大于 10 万或实时波形", "choice": "webgl 或 LTTB 降采样", "reason": "GPU 批量绘制加有损降采样" },
      { "condition": "需要打印或文本可检索", "choice": "svg 为主加 canvas 混合", "reason": "坐标轴与图例用 svg 保留语义" }
    ],
    "thresholds_must_be_measured": "阈值以真机 50 分位设备实测为准，桌面端拐点不可直接套用到移动端"
  }
}
```
