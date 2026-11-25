---
title: [SCN-726] SLA 看板的信息架构（首屏三问）怎么组织？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-726：看板信息架构怎么组织？
**答**：
- 首屏三问：整体健康吗（健康分/达标率总览）、现在有事吗（活跃告警/烧率）、哪最差（最差指标 Top3）——10 秒内回答完，用户决定看细节还是走人。
- 层级折叠：核心区（6 卡）→ 业务线矩阵 → 单指标详情页（趋势/构成/改进项）；每个层级入口清晰，反对「一屏塞 30 个图」。
- 色彩纪律：红黄绿三色语义 + 中性色；红色同时出现在超过 5 个位置时强制聚合（红太多等于没有红）。
- 面向角色预设视图：值班/团队 leader/业务方各自默认视图（同一数据不同组织）。
- 追问钩子：怎么验证信息架构有效——新用户 5 秒任务测试（「现在系统健康吗」「哪个业务最差」）+ 值班响应时长对比，答不上来的首屏就是失败的首屏。

```javascript
const boardIA = {
  hero: ['healthScore', 'burnRateNow', 'worstTop3'],
  core: 6,                                    // 核心卡上限
  drill: ['bizMatrix', 'metricDetail'],
  colorRule: { redMaxVisible: 5, aggregateWhenExceed: true },
  roleViews: { oncall: 'now+unclaimed', lead: 'trend+team', biz: 'journey' },
};
```
