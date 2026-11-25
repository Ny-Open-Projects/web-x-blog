---
title: [SCN-705] SLA 看板的多维下钻（业务线→页面→接口→trace）怎么设计？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-705：SLA 看板多维下钻怎么设计？
**答**：
- 下钻路径预定义：体验级 → 业务线 → 页面 → 接口/资源 → 样本 trace，每一跳的维度键固定（不自由组合维度，避免组合爆炸与口径混乱）。
- 每层视图不同：上层看趋势与达标率（折线+SLO 线），中层看贡献度分解（哪个页面把大盘拖差），底层看明细样本（可跳 trace 平台）。
- 贡献度分析：下钻自动计算「影响贡献」=（该维度 P95 - 大盘 P95）× 权重，排序呈现——先看拖后腿的再看整体。
- 下钻状态入 URL（可分享）：/board?biz=pay&page=checkout&from=2026-11-14。
- 追问钩子：为什么下钻到 trace 而不是直接展示 trace——样本级数据量大且需上下文，看板负责「发现异常聚集」，trace 负责「单请求深查」，工具链分工。

```javascript
function drillDown(state, dim) {
  const PATH = { root: ['biz'], biz: ['page'], page: ['api', 'resource'], api: ['trace'] };
  const next = { ...state, dim: dim.value, level: PATH[state.level][0] };
  location.href = buildUrl('/board', next);          // 状态入 URL 可分享
  return next;
}
function contribution(dimRows, baselineP95, totalWeight) {
  return dimRows
    .map(r => ({ ...r, contrib: (r.p95 - baselineP95) * (r.weight / totalWeight) }))
    .sort((a, b) => b.contrib - a.contrib)           // 贡献度排序：谁拖差了大盘
    .filter(r => r.contrib > 0);
}
```
