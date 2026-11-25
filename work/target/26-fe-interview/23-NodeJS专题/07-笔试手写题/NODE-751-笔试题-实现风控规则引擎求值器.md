---
title: [NODE-751] 笔试题——实现风控规则求值器（优先级短路 + 可解释）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-751：手写风控求值器

**需求与边界**：
- 需求：风控规则求值（SCN-NODE-686）——① 条件表达式求值（SCN-OPS-638 递归下降复用）；② 优先级短路（高优先级命中即决）；③ 决策三件套（action/reason/matchedRule——可解释）；④ 规则集热更新（版本快照——SCN-NODE-663 配置热更）。
- 边界：① 求值异常的规则跳过（坏规则不影响其他——容错）；② 求值耗时预算（>50ms 截断——同步路径保护，剩余走异步模型）；③ 决策日志采样（全量拦截/抽样放行——SCN-SLA-724）。

**答**：
```javascript
function evaluate(signals, ruleSetSnapshot, { budgetMs = 50 } = {}) {
  const t0 = performance.now();
  const sorted = [...ruleSetSnapshot.rules].sort((a, b) => a.priority - b.priority);
  const evaluated = [];
  for (const rule of sorted) {
    if (performance.now() - t0 > budgetMs) {           // 预算截断（同步保护）
      evaluated.push({ rule: rule.id, skipped: 'BUDGET' });
      break;                                           // 剩余规则异步模型补充
    }
    try {
      if (evalExpr(rule.cond, signals))                // 表达式求值（SCN-OPS-638）
        return { action: rule.action, reason: rule.reasonKey, matchedRule: rule.id,
          evaluated };                                 // 三件套可解释（SCN-NODE-686）
      evaluated.push({ rule: rule.id, hit: false });
    } catch (e) {
      evaluated.push({ rule: rule.id, error: e.message });   // 坏规则容错跳过
    }
  }
  return { action: 'PASS', reason: 'no-match', evaluated };
}
// 热更新（规则集快照——SCN-NODE-663）
ruleSetSwap.on('change', (v2) => { currentSnapshot = v2; audit({ ver: v2.version }); });
```

**评分点**:
- 优先级短路 + 表达式求值复用（SCN-OPS-638）。
- 预算截断（同步路径保护——剩余异步模型补充）。
- 坏规则容错跳过（不影响其他规则）。
- 决策三件套可解释（action/reason/matchedRule——SCN-NODE-686）。
