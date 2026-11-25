---
title: [AGT-608] 给运营/产品看的 Agent 大盘应该放什么指标（与开发看的有什么区别）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-608：给运营/产品看的 Agent 大盘应该放什么指标（与开发看的有什么区别）

**答**：
- 运营视角是「结果与钱」：任务完成率、用户采纳率（复制/点赞）、活跃会话数、单位任务成本、负反馈 topN 标签；开发视角是「过程健康」：错误率/延迟/依赖可用性。两个大盘分开，共用底层指标。
- 大盘每张图都要能下钻：点完成率下降的柱子→按任务类型/模型版本/租户拆分→直接给出可疑维度与样本 trace 链接。
- 防呆：大盘指标定义有口径说明与版本（"完成率=含工具成功的任务占比"，口径变更要公告），否则跨周对比失真。

```javascript
const OPS_PANEL = [
  { metric: 'taskDoneRate', drill: ['taskType', 'modelVer', 'tenant'] },
  { metric: 'adoptionRate', drill: ['surface', 'persona'] },
  { metric: 'costPerTask', drill: ['modelVer', 'taskType'] },
  { metric: 'dislikeTopTags', drill: ['promptVer'] },
];
function drillDown(metric, dim) {               // 点图下钻到样本
  return {
    breakdown: groupBy(metric, dim),
    samples: recentTraces({ where: anomalyFilter(metric), limit: 20 }),
  };
}
```

