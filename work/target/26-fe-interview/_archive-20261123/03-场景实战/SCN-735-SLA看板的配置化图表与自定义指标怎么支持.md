---
title: [SCN-735] 看板的配置化图表与自定义指标（自助分析）怎么支持？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-735：配置化图表与自助分析怎么支持？
**答**：
- 自助查询：指标注册表 + 维度选择 + 简单表达式（对比/同环比/滑动平均）→ 生成临时图表；查询模板保存分享。
- 防御性设计：自助查询走只读物化层、查询成本预估（维度组合数超限提示）、查询超时上限——防止一个复杂查询拖垮共享集群。
- 与正式看板的关系：自助图表转正流程（常用查询 → 提案 → 口径卡补齐 → 上正式板）；避免「个人图表」长期承担团队职责却无人维护。
- 权限与配额：按团队分配查询配额（并发/次数），防滥用。
- 追问钩子：怎么防止自助查询把时序库查挂——准入三道闸：维度组合预估（基卡片数）、强制物化层、超时熔断；复杂分析引导到数仓离线链路。

```javascript
async function adhocQuery(expr, dims, range) {
  const cost = estimateCost(dims, range);            // 基数估算
  if (cost.cardinality > 1e6) throw new Error('TOO_EXPENSIVE');
  const q = compileExpr(expr, registry);             // 只允许注册表内指标
  return withTimeout(queryMaterialized(q, range, dims), 10_000);
}
function promoteToBoard(chart) {                     // 转正流程
  return api.post('/board/proposal', { ...chart, needs: ['metric-card', 'owner', 'slo'] });
}
```
