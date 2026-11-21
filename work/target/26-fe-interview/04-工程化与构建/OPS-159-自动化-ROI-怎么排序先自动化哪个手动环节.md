---
title: [OPS-159] 自动化 ROI 怎么排序？先自动化哪个手动环节？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-159：自动化 ROI 怎么排序？先自动化哪个手动环节？
**答**：
- 量化公式：ROI = 年节省人时 × 人力单价 ÷ 实现成本，再加风险收益权重（出错率下降、事故避免的期望价值）。
- 排序规律：高频 × 低复杂度 × 高出错率的环节最先做——发布后的 CDN 刷新与验证、checklist 卡口、到期巡检都是典型。
- 反面清单：低频 × 高复杂度的（全自动回滚决策、审批自动化）收益低风险高，保留人在回路。
- 自动化不是消灭人工而是消灭"遗漏"：机器负责执行与提醒，人负责判断与拍板。
- 每季度重新盘点手动步骤清单（OPS-100 的评估法），ROI 表是滚动维护的。

```json
{
  "automation_roi": {
    "method": "ROI = 年节省人时 × 人力单价 ÷ 实现成本，叠加风险收益（出错率下降）加权",
    "candidates": [
      { "priority": 1, "item": "CDN 刷新与发布后验证自动化", "manual_per_day_min": 15, "build_days": 3, "roi": "极高", "note": "每天 3-5 次发布，漏刷/重刷引发半新半旧事故（OPS-117）" },
      { "priority": 2, "item": "发布单自动生成与 checklist 卡口", "manual_per_day_min": 20, "build_days": 5, "roi": "极高", "note": "人肉 checklist 遵守率不足 60%（OPS-180）" },
      { "priority": 3, "item": "证书/域名到期自动巡检", "manual_per_month_min": 30, "build_days": 1, "roi": "高", "note": "低频高危事故，台账 + 预警（OPS-189）" },
      { "priority": 4, "item": "可用性周报自动生成", "manual_per_week_min": 60, "build_days": 2, "roi": "高", "note": "模板 + API 拉数（OPS-136）" },
      { "priority": 5, "item": "灰度放量自动化", "manual_per_day_min": 25, "build_days": 8, "roi": "中高", "note": "依赖看板数据准确（OPS-187）" },
      { "priority": "keep_human", "item": "生产审批与回滚决策", "roi": "低", "note": "合规要求与判断职责，机器辅助建议 + 人工拍板（OPS-139）" }
    ],
    "principle": "先做高频低复杂度；自动化负责执行与提醒，人负责判断与拍板"
  }
}
```

---

## 十八、多端发布（OPS-160 ~ OPS-167）

一码多端的发布矩阵：版本策略、小程序分包与 CI、Electron 更新、RN/Flutter 差异、内嵌 H5 协商、离线包与矩阵构建。
