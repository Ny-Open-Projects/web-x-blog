---
title: [TST-866] AI 生成测试的「可解释性」如何保证（为什么这么测）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-866：AI 生成测试的「可解释性」如何保证（为什么这么测）？
**答**：
- 结论：AI 生成测试必须附「测试意图说明」——每个用例标注覆盖的需求点/风险点，让人能审查「为什么测这个」而非只看代码。
- 做法：prompt 要求输出注释块（被测行为、边界依据、对应需求）；生成结果与需求条款建立双向追溯。
- 价值：可解释性让评审有抓手，出现幻觉时快速识别；也便于知识沉淀与新人学习。
- 取舍：说明增加 token 成本，但换取可审查性，值得；关键链路强制，低风险可简化。
- 追问钩子：AI 给出了看起来很合理的「解释」，但测试其实是错的，如何防止被解释「带偏」？

```javascript
// AI 生成结果带「意图说明」 + 追溯
const generated = {
  code: `it('金额为 0 时不报错', () => expect(formatMoney(0)).toBe('¥0.00'));`,
  explanation: {
    requirement: 'REQ-12 金额格式化',
    riskPoint: '零值边界，历史曾因除零崩溃',
    boundary: '0 / 负数 / NaN 的等价类划分',
  },
  traceability: { requirementId: 'REQ-12', coveredBy: ['zero', 'negative'] },
};
// 评审时先读 explanation 判断是否测到点子上，再看 code
console.log(generated.explanation.riskPoint);
```
