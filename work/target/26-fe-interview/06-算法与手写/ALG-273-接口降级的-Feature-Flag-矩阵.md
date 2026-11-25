---
title: [ALG-273] 接口降级矩阵：多服务依赖的降级组合（每个服务的降级档位 × 功能可用性映射）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-273：接口降级矩阵：多服务依赖的降级组合（每个服务的降级档位 × 功能可用性映射）？
**答**：详情页依赖 4 服务（商品/价格/库存/推荐）——某服务故障时的降级组合（价格服务挂 → 显示"价格暂不可用"并禁用下单；推荐挂 → 隐藏区块）。降级矩阵声明式配置（服务状态 × 组件行为），而不是 if-else 散落。

**思路**：矩阵 = { 服务: 档位（ok/degraded/down）→ 每组件的渲染决策 }；健康判定（连续失败次数 + 熔断 HW-063）；矩阵驱动渲染。

```javascript
const DEGRADE_MATRIX = {
  price:   { down: { hide: ['priceBar'], disable: ['buyBtn'] } },
  stock:   { down: { disable: ['buyBtn'], note: '库存查询中' } },
  goods:   { down: { redirect: '/error?from=goods' } },            // 核心服务挂：整页降级
  recs:    { down: { hide: ['recSection'] } },                     // 边缘服务挂：静默隐藏
};
function applyDegradation(services) {
  const actions = [];
  for (const [svc, state] of Object.entries(services)) {
    const rule = DEGRADE_MATRIX[svc]?.[state];
    if (rule) actions.push({ svc, ...rule });
  }
  return actions;    // [{ svc: 'price', hide: ['priceBar'], disable: ['buyBtn'] }]
}
// 渲染层按 actions 执行：hide → 区块 display none；disable → 按钮 disabled + note；redirect → 整页跳转
// 健康判定：连续 3 次失败 → degraded（降级响应）→ 5 次则 down（HW-063 熔断）——半开恢复探测
// 矩阵价值：降级策略集中声明（评审可见）、新增服务只加一行（不再散落 if-else）
// 大促联动：L2/L3 降级（PER-377）= 手动强制矩阵状态（绕过健康判定直接 down）
```

**评分点**:
- 声明式降级矩阵（服务 × 档位 → 组件动作）——本题核心。
- 健康判定（连续失败 + 熔断半开）与手动强制（大促预案）两条触发路径。
- 核心服务 vs 边缘服务的降级差异（redirect vs hide）。
- 矩阵集中声明的可评审性。
