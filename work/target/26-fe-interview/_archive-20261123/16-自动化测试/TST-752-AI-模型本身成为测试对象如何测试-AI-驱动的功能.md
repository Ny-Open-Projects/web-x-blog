---
title: [TST-752] AI 模型本身成为测试对象：如何测试「AI 驱动的功能」
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-752：AI 模型本身成为测试对象：如何测试「AI 驱动的功能」

**答**：
- 结论：AI 功能输出是概率性的，不能断言「精确答案」，要断言「满足属性」——格式合规、约束遵守、语义相关、安全边界。
- 测试集分层：黄金集（固定输入输出，回归用）+ 属性集（规则断言）+ 对抗集（鲁棒性）。
- 用多模型/多采样统计通过率而非单次结果，设定最低通过率阈值。
- 追问钩子：模型升级后黄金集通过率下降但用户体验变好，如何决策？

```javascript
// 属性断言：不比对精确文本，比对结构化约束
function assertAIResponse(resp, constraints) {
  const results = constraints.map(c => {
    if (c.type === 'json') { try { JSON.parse(resp.text); return true; } catch { return false; } }
    if (c.type === 'noPII') return !/\d{11}/.test(resp.text);
    if (c.type === 'maxLen') return resp.text.length <= c.value;
    return false;
  });
  return { pass: results.every(Boolean), details: results };
}
console.log(assertAIResponse(
  { text: '{"answer": 42}' },
  [{ type: 'json' }, { type: 'noPII' }, { type: 'maxLen', value: 100 }]
));
```
