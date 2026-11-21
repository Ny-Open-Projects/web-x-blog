---
title: [PER-228] 如何为团队制定 INP SLO 并推动治理？指标、看板与卡口怎么设计？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-228：如何为团队制定 INP SLO 并推动治理？指标、看板与卡口怎么设计？

**答**：
- 定基线：先接 RUM 跑两周拿现状 p75/p98 INP 与 top 慢交互清单，按"好 ≤ 200ms（p75）"设目标，不要直接照抄 Google 阈值到全部页面——按页面重要性分档（核心交易页严格、低频页放宽）。
- 看板设计：分位数（p75/p98）× 页面 × 交互类型三维拆解；带 LoAF invoker 归因 top5；标注版本发布时间轴，能对上"哪次发版弄坏了 INP"。
- 卡口：CI 里 Lighthouse CI 压 TBT（实验室近似 INP 的指标）+ 产物体积预算；RUM 周报里 INP 回归页面自动艾特 owner；紧急预案——INP p75 连续 3 天超标则冻结非修复类发布。
- 推动技巧：把 INP 与业务指标挂钩（转化率/留存），用"慢 500ms 损失 X% 转化"说话；给 owner 的不是抽象指标而是可直接修的慢函数清单。

```javascript
// 看板聚合 SQL 思路示例（服务端）：按页面 × 交互类型出 p75/p98
// SELECT page, interaction_type,
//        APPROX_PERCENTILE(inp, 0.75) AS p75,
//        APPROX_PERCENTILE(inp, 0.98) AS p98,
//        COUNT(*) AS samples
// FROM rum_interactions
// WHERE ts >= NOW() - INTERVAL 7 DAY AND nav_type = 'navigate'
// GROUP BY page, interaction_type
// HAVING p75 > 200          -- 超标页面进治理清单
// ORDER BY p98 DESC;
// 周报：把 p75 > 200ms 的页面按 owner 分组，附 LoAF top5 慢脚本
```
