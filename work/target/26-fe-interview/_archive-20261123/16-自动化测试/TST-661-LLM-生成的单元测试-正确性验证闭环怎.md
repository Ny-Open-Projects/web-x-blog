---
title: [TST-661] LLM 生成的单元测试，正确性验证闭环怎么设计？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-661：LLM 生成的单元测试，正确性验证闭环怎么设计？

**答**：
- 结论：把生成测试当「候选 PR」——先静态编译/类型检查，再跑通，再做变异测试验证断言强度，最后人工抽检。
- 闭环指标：编译通过率、首次通过率、变异存活率、人工返工率，任一恶化就调 prompt/示例。
- 生成物与人工测试分库存放并标记来源，便于统计真实质量差异。
- 追问钩子：生成测试全绿但变异存活率 90%，说明什么问题？

```javascript
async function verifyGenerated(tests, { run, mutate }) {
  const out = [];
  for (const t of tests) {
    const compiled = compile(t.code);
    const passed = compiled ? await run(t.code) : false;
    const mutation = passed ? await mutate(t.target, t.code) : 0;
    out.push({ id: t.id, compiled, passed, mutation,
      accept: compiled && passed && mutation >= 0.6 });
  }
  return out;
}
```
