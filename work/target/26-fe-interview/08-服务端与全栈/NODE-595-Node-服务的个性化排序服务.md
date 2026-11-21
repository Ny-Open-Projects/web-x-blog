---
title: [NODE-595] Node 服务的个性化排序（推荐服务集成）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-595：个性化排序服务
**答**:
- 排序层次：召回（多路：热门/类目/个性化——候选集）、粗排（轻模型打分）、精排（推荐服务模型——BFF 集成 ARC-493）、重排（业务规则：打散（同店铺限流）/置顶（运营位）/多样性——规则层与模型层分离）。
- 服务边界：推荐模型在算法服务（离线/在线模型），交易服务只做"组装与规则"——BFF 侧的 re-rank 规则配置化（打散/过滤规则运营可调）。
- 数据流：用户特征（实时行为——特征服务）、物品特征（商品侧数据）、曝光去重（已曝光集合——端上报 + 服务端会话集合）、因果反馈（曝光→点击→转化数据回流——模型训练数据 ARC-385）。
- 可靠性：推荐超时降级（热度兜底 ARC-493）、多样性保底（规则层保底——模型挂也不至于全同质）、AB 分桶（实验体系 NODE-445）。
- 观测：排序质量指标（CTR/CVR 按位衰减——位置偏差校正）、规则触发统计。
```javascript
// 排序重排（BFF 侧规则层）
function rerank(items, ctx) {
  let ranked = modelScores ? sortDesc(items, 'score') : hotFallback(items);  // 模型或兜底
  ranked = diversify(ranked, { maxPerShop: 3 });                 // 打散规则
  return interleaveOps(ranked, ctx.opsSlots);                    // 运营位插入
}
```
