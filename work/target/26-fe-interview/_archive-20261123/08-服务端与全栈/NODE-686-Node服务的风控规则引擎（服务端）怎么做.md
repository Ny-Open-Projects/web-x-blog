---
title: [NODE-686] 风控规则引擎（服务端）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-686：风控规则引擎怎么做？
**答**：
- 规则模型：规则 = 条件表达式（SCN-OPS-638 条件求值器）+ 动作（拦截/验证/放行）+ 优先级；规则集配置化（SCN-OPS-573 开关矩阵——运营调整不发版）。
- 决策流程：信号收集（设备/行为/账户画像——SCN-联想-555/556）→ 规则求值（短路——高优先级命中即决）→ 决策输出（决策 + 原因 + 命中规则——可解释）。
- 性能：规则求值 <50ms（同步路径）；重模型评分异步（同步规则先行——规则拦截零成本，模型补充评分异步返回影响后续请求）。
- 反馈闭环：误杀样本回流（SCN-联想-569）、规则命中率看板（SCN-联想-575）。
- 追问钩子：为什么风控决策要「决策 + 原因 + 命中规则」三件套——无原因的拦截无法区分误杀与真杀（运营没法调整规则）；原因与命中规则让每次拦截可审计、可申诉（SCN-联想-561 申诉）、可归因（哪个规则误杀率高）——可解释性是风控引擎与黑盒模型的核心差异。

```javascript
function evaluate(signals, ruleSet) {
  const sorted = ruleSet.sort(byPriority);             // 优先级短路
  for (const rule of sorted) {
    if (rule.enabled && evalCond(rule.cond, signals))
      return { action: rule.action, reason: rule.reasonKey,
        matchedRule: rule.id, score: signals.riskScore };   // 三件套可解释
  }
  return { action: 'PASS', reason: 'no-match' };
}
```
