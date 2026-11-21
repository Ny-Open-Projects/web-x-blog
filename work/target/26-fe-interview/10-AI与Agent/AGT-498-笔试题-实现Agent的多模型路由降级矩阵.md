---
title: [AGT-498] 笔试题——实现任务级模型路由矩阵（能力需求×成本×可用性）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-498：手写路由矩阵：任务能力需求匹配、可用性兜底、成本上限联动

**需求与边界**：
- 输入：任务（含能力需求标注）、模型目录（能力/成本/健康度）、预算约束；输出：选定模型。
- 边界要求：① 能力匹配优先（不满足能力的模型直接排除——无论多便宜）；② 健康度过滤（熔断中的模型跳过）；③ 成本上限（超预算的档位降级）；④ 决策理由返回（可解释可审计）。

**答**：
```javascript
function routeModel(task, models, { budget, health }) {
  // 1. 能力匹配硬过滤
  const capable = models.filter(m =>
    task.needs.every(n => m.capabilities.includes(n)));
  if (!capable.length)
    return { error: 'NO_CAPABLE_MODEL', needs: task.needs,
      suggestion: '扩展模型目录或降低需求' };
  // 2. 健康度过滤（熔断中跳过）
  const healthy = capable.filter(m =>
    health.of(m.id) !== 'open');
  const pool = healthy.length ? healthy : capable; // 全熔断仍选最优
  // 3. 成本排序（便宜优先）+ 预算约束
  const sorted = pool.sort((a, b) => a.costPer1k - b.costPer1k);
  const chosen = sorted.find(m => estCost(m, task) <= budget)
    ?? sorted[sorted.length - 1];                // 超预算取最便宜
  // 4. 决策理由
  const reason = {
    capability: task.needs.join('+'),
    filteredByHealth: capable.length - healthy.length,
    costChoice: chosen === sorted[0]
      ? '预算内最便宜' : '预算不足降级',
    estCost: estCost(chosen, task), budget,
    degraded: chosen !== sorted[0],
  };
  return { model: chosen.id, reason };
  // 全熔断时仍选能力最强（可用性优先于健康度——
  // 熔断是概率保护不是绝对禁止，但要有告警）。
}
// models 示例：[
//  { id: 'small', capabilities: ['chat'], costPer1k: 0.5 },
//  { id: 'big', capabilities: ['chat','reasoning','vision'],
//    costPer1k: 8 }]
// task: { needs: ['chat','vision'] } → small 被排除。
```

**评分点**:
- 能力硬过滤优先于成本（能力不足的便宜模型不可用）。
- 健康度过滤+全熔断兜底策略（附告警）。
- 预算约束下的降级路径（超预算取最便宜）。
- 决策理由结构化返回（reason 字段可审计）。
