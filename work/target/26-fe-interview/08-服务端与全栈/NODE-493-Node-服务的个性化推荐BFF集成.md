---
title: [NODE-493] Node 服务的个性化推荐（BFF 集成推荐服务）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-493：个性化推荐 BFF 集成
**答**:
- BFF 与推荐服务的分工：推荐服务产出候选（算法侧），BFF 负责"装配"（过滤：售罄/黑名单/已购、补充展示数据：价格/库存/图片——推荐 ID 列表 → 批量取详情 NODE-414 主从分页）、兜底（推荐挂了 → 热门榜单兜底 ARC-447）。
- 降档与预算：推荐请求预算（ARC-489 分层——推荐属 fast 层 200ms 超时降级）、高峰降档（热点时公共热门替代个性化 ARC-564）、弱端降档（低端机减少推荐模块）。
- 一致性细节：推荐时效（推荐结果带过期时间——库存变化后旧推荐要失效刷新）、曝光去重（同会话不重复推荐——端上会话集合 + 服务端辅助）、埋点回传闭环（曝光/点击回传推荐服务——算法优化数据 ARC-385）。
- 冷启动：新用户无画像 → 人群兜底策略（热门/运营位）——冷启动策略配置化（运营可调）。
- 观测：推荐接口 P95/兜底触发率/点击率（推荐质量信号进看板）。
```javascript
async function recommend(ctx) {
  const { items, exp } = await Promise.race([
    recoService.for(ctx.user), timeout(200)]);
  const enriched = await goodsSvc.batchFill(filterSellout(items));  // 装配 + 过滤
  if (!enriched.length) return hotFallback(ctx);                    // 兜底
  return { items: enriched, exp, staleAt: Date.now() + 30e3 };      // 时效标注
}
```
