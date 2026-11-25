---
title: [AIC-567] 笔试：手写 AI 质量改进闭环
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-567：笔试：手写 AI 质量闭环

**答**：实现 `improvementLoop(week1, week2, { modifyThreshold, acceptThreshold })`。week1/week2: `{ acceptRate, modifyRate, retainRate }[]`（两周的度量）。规则：1) **改善检测**：week2.acceptRate > week1.acceptRate → 'improving'；2) **恶化检测**：week2.modifyRate > week1.modifyRate → 'degrading'（修改率上升 = AI 质量下降）；3) **行动建议**：improving → 'continue'；degrading → 更新规则（acceptRate < 30 → 'update-rules'）；持平 → 'monitor'；4) **趋势**：两周的差值（每指标的 delta）。返回 `{ trend: 'improving'|'degrading'|'stable', deltas: Record<metric, number>, action }`。边界：两周数据完全相同（stable）；只有一周（insufficient）；两个指标矛盾（accept 上升但 modify 也上升——net 评估）。

```javascript
function improvementLoop(w1, w2, { modifyThreshold = 30, acceptThreshold = 50 } = {}) {
  if (!w1 || !w2) return { trend: 'insufficient', deltas: {}, action: 'need-more-data' };
  const deltas = {
    acceptRate: +(w2.acceptRate - w1.acceptRate).toFixed(1),
    modifyRate: +(w2.modifyRate - w1.modifyRate).toFixed(1),
    retainRate: +(w2.retainRate - w1.retainRate).toFixed(1),
  };
  // 净评估：accept 上升 = 正；modify 上升 = 负
  const improving = deltas.acceptRate > 0 && deltas.modifyRate <= 0;
  const degrading = deltas.modifyRate > 0 || deltas.acceptRate < -5;
  let trend = 'stable'; let action = 'monitor';
  if (improving) { trend = 'improving'; action = 'continue'; }
  else if (degrading) {
    trend = 'degrading';
    action = w2.acceptRate < acceptThreshold ? 'update-rules' : 'adjust-prompt';
  }
  return { trend, deltas, action };
}

// 自测
const w1 = { acceptRate: 60, modifyRate: 20, retainRate: 85 };
// 改善：accept 上升 + modify 下降
let r = improvementLoop(w1, { acceptRate: 70, modifyRate: 15, retainRate: 90 });
console.log(r.trend === 'improving' && r.action === 'continue');
console.log(r.deltas.acceptRate === 10);
// 恶化：modify 上升
r = improvementLoop(w1, { acceptRate: 55, modifyRate: 40, retainRate: 80 });
console.log(r.trend === 'degrading');
console.log(r.action === 'adjust-prompt');               // acceptRate 55 ≥ 50 → adjust-prompt
// 恶化严重：accept < 30 → update-rules
r = improvementLoop(w1, { acceptRate: 25, modifyRate: 60, retainRate: 60 });
console.log(r.action === 'update-rules');
// 稳定
r = improvementLoop(w1, { acceptRate: 60, modifyRate: 20, retainRate: 85 });
console.log(r.trend === 'stable' && r.action === 'monitor');
// 矛盾：accept 上升但 modify 也上升
r = improvementLoop(w1, { acceptRate: 70, modifyRate: 35, retainRate: 85 });
console.log(r.trend === 'degrading');                    // modify 上升 = degrading 优先
// 数据不足
console.log(improvementLoop(w1, null).trend === 'insufficient');
```

**评分点**：
- 双周对比的 delta 计算（每指标的差值——趋势量化）
- 矛盾处理（accept 上升但 modify 也上升 → degrading 优先——质量恶化信号更紧急）；action 分级（continue/adjust/update）
- 边界（稳定/数据不足/矛盾）；accept 阈值决定 action 级别
- 能说清「AI 质量改进需要闭环：接受率下降 → 自动发现 → 更新规则 → 验证——不是一次性调优而是持续进化」属于加分
