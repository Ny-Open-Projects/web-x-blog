---
title: [TST-845] 性能预算(performance budget)如何在 CI 中「卡住」而不被绕过？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-845：性能预算(performance budget)如何在 CI 中「卡住」而不被绕过？
**答**：
- 结论：性能预算要「写入配置、内联进 CI 门禁、超阈值直接 fail、异常需审批」——把预算变成代码而非文档约定。
- 预算项：LCP/INP/CLS 阈值、JS/CSS 体积上限、请求数、第三方脚本数，配置化（budget.json）。
- 卡点方式：Lighthouse CI 断言超预算即 fail（blocking），PR 检查必须过；基线对比禁止无声退化。
- 防绕过：预算只能经评审修改（CODEOWNERS 保护 budget 文件），临时豁免需标注过期时间并自动提醒。
- 追问钩子：有人把 Lighthouse 分数阈值调低来「过门禁」，你如何从流程和机制上堵住？

```javascript
// 性能预算门禁：超预算即 fail
const budget = { lcp: 2500, cls: 0.1, jsKB: 300 };
function checkBudget(actual) {
  const breaches = [];
  if (actual.lcp > budget.lcp) breaches.push(`LCP ${actual.lcp} > ${budget.lcp}`);
  if (actual.cls > budget.cls) breaches.push(`CLS ${actual.cls} > ${budget.cls}`);
  if (actual.jsKB > budget.jsKB) breaches.push(`JS ${actual.jsKB}KB > ${budget.jsKB}KB`);
  return { pass: breaches.length === 0, breaches };
}
console.log(checkBudget({ lcp: 2100, cls: 0.05, jsKB: 320 })); // fail: JS 超预算
```
