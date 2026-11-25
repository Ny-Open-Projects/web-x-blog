---
title: [TST-663] AI 做测试用例的「自动补全与意图理解」怎么落地？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-663：AI 做测试用例的「自动补全与意图理解」怎么落地？

**答**：
- 结论：让 AI 补全「用例意图」而非直接写断言——先产出 Given/When/Then 大纲，人确认后再生成代码。
- 用现有用例库做 few-shot，提示词注入业务术语表提升意图准确率。
- 补全结果以 diff 形式让人 review，不自动合入。
- 追问钩子：AI 总漏掉边界条件，你怎么在 prompt 里系统性补齐？

```javascript
function buildPrompt(change, examples, glossary) {
  return [
    '你是资深测试工程师，基于变更补全测试意图。',
    `术语表：${JSON.stringify(glossary)}`,
    ...examples.map(e => `例：${e.change} => ${e.intents.join(';')}`),
    `变更：${change}`,
    '输出 JSON: {intents:[{given,when,then}]}，覆盖正常/边界/异常三类。',
  ].join('\n');
}
```
