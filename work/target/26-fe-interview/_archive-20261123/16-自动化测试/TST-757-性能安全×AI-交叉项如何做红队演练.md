---
title: [TST-757] 性能安全×AI 交叉项如何做「红队演练」验证防护有效性
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-757：性能安全×AI 交叉项如何做「红队演练」验证防护有效性

**答**：
- 结论：红队演练要攻击「AI 引入的新攻击面」——Prompt 注入诱导泄露、模型输出投毒、通过 AI 特性绕过安全门禁。
- 演练设计：设定攻击目标（如越权/泄露 PII/绕过限流），红队用 AI 辅助生成攻击变体，蓝队验证检测与阻断。
- 结果必须量化：拦截率、误报率、平均发现时长，形成防护有效性基线并持续复测。
- 追问钩子：红队用 AI 生成了蓝队规则库里没有的攻击，说明什么？

```javascript
// 红队演练：攻击变体覆盖度统计
function redTeamSummary(attacks) {
  const blocked = attacks.filter(a => a.blocked).length;
  const byType = {};
  for (const a of attacks) byType[a.type] = (byType[a.type] || 0) + (a.blocked ? 1 : 0);
  return {
    blockRate: +(blocked / (attacks.length || 1)).toFixed(2),
    byType,
  };
}
console.log(redTeamSummary([
  { type: 'prompt-inject', blocked: true },
  { type: 'pii-leak', blocked: false },
]));
```
