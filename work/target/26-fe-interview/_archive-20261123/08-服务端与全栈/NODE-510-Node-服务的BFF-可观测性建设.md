---
title: [NODE-510] Node 服务的 BFF 层专属可观测性（聚合视角）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-510：BFF 层专属可观测性
**答**:
- BFF 的观测重点不同于普通服务：聚合视角（页面/接口 → 多下游的调用树健康）、降级视角（降级触发率/兜底数据占比——用户看到"假数据"的比例是 BFF 特有质量指标 NODE-490）、协议视角（多端 profile 正确性——装配错误是 BFF 特有 bug）。
- 指标体系：按接口聚合指标（总耗时/关键路径耗时/瀑布深度 NODE-501）、下游依赖指标（按下游分桶的调用成功率——哪个下游拖累哪个页面）、降级指标（degrade 事件率/降级时长/降级后用户体验指标）、缓存指标（NODE-502 三层命中）。
- trace 特化：聚合 span 树的可视化（调用树 + 降级标记 + 缓存命中标记——排障一眼看全 ARC-501 瀑布）、trace 与前端 RUM 关联（ARC-533 打通——BFF 是中间桥梁）。
- 告警特化：页面级 SLO（BFF 按页面维度告警——不是按服务，用户关心页面）、降级率告警（兜底占比 > 阈值 = 事实上的降级运行要告警）。
- 运营：BFF 健康周报（各页面聚合健康度——厚积薄发的治理输入 NODE-500）。
```javascript
// BFF 特化指标
metrics.histogram('bff.page.duration', dur, { page: 'home', tier, gray });
metrics.counter('bff.degrade', 1, { page, dep: 'recommend', reason: 'timeout' });
metrics.gauge('bff.degrade.ratio', degradedCount / totalCount);  // 兜底占比告警线 5%
// trace: span(degrade) 标记 + cache hit 标记 → 调用树可视化
```
