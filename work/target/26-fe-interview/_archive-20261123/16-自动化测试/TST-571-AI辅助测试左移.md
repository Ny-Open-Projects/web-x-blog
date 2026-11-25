---
title: [TST-571] AI 如何辅助测试左移（需求到测试点）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-571：AI 如何辅助测试左移（需求到测试点）

**答**：
- 结论：在需求评审阶段让 AI 把用户故事拆成「正向/边界/异常/安全/性能」测试点清单，并标出需求歧义与缺失的验收标准，提前暴露问题。
- 做法：输入需求文本 + 历史同类缺陷，Prompt 要求按维度输出测试点并给出「需求疑问」；人工评审补充业务隐含规则；结果进入测试计划并追踪覆盖。
- 追问钩子：AI 拆出的测试点太多太散怎么办？——用风险分级与去重收敛，聚焦高风险与高频路径；AI 的价值是「不漏」，收敛靠人的判断。

```javascript
// 需求 → 测试点：按维度分类 + 标记歧义
const DIMENSIONS = ['happy', 'boundary', 'error', 'security', 'performance'];
function expandTestPoints(requirement) {
  const points = DIMENSIONS.map(d => ({ dimension: d, items: [] })); // 实际由 LLM 填充
  const ambiguous = [];
  if (/较快|及时|友好/.test(requirement)) ambiguous.push('存在模糊指标，需量化');
  if (!/权限|鉴权/.test(requirement)) ambiguous.push('未提及权限要求');
  return { points, ambiguous };
}
console.log(expandTestPoints('登录后较快看到订单列表')); // ambiguous 含模糊指标提示
```
