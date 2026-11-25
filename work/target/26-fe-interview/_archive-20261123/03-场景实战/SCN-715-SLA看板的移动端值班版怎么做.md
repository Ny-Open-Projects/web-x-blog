---
title: [SCN-715] SLA 看板的移动端值班版怎么做？在手机上看什么？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-715：移动端值班版怎么做？
**答**：
- 手机值班场景是「响应告警」而非「浏览分析」：核心是告警卡片（严重度/当前值 vs SLO/持续时长）+ 快捷动作（认领/静默/拉群），复杂分析引导回 PC（一键把当前视图链接发到 PC）。
- 推送驱动：移动端以推送为主、拉取为辅，冷启动直接落在「未认领告警」页，而不是看板首页。
- 低信息密度：一屏一个告警的详情，滑动切换；图表只保留 sparkline 迷你趋势。
- 可靠性：推送通道保活（厂商通道 + 轮询兜底）、弱网重试、关键动作（认领）离线排队。
- 追问钩子：移动端要不要做完整看板——不建议，屏幕与场景都不适合；做「告警响应工具」比做「缩小版看板」价值高，别把 PC 需求平移到手机。

```javascript
// 移动端值班首页 = 未认领告警队列
const mobileOncall = {
  primary: 'unclaimed-alerts',
  actions: ['claim', 'silence_15m', 'create_group_chat'],   // 三个快捷动作
  sparklineOnly: true,                                     // 迷你趋势
  handoff: (view) => shareToDesktop(view.url),             // 一键发 PC
  offlineQueue: true,                                      // 认领动作离线排队
};
```
