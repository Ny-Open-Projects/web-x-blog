---
title: [TST-970] 要评估 AI 生成测试，却缺少「标准答案」，如何构建可靠性基准数据集？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-970：要评估 AI 生成测试，却缺少「标准答案」，如何构建可靠性基准数据集？
**答**：
- 结论：基准集 = 一组「已知缺陷 + 已知正确行为」的固定代码版本与种子用例，AI 生成的用例在上面跑，用能否检出注入缺陷来评分。
- 做法：从历史 bug 中抽取 commit 前版本注入（bug-injection），配套「应当失败」的断言；覆盖多框架多场景防止过拟合。
- 防污染：基准集不公开给模型训练，定期更新防止 AI 背答案。
- 追问钩子：AI 在你的基准集上得分 90%，但线上用例还是常漏 bug，基准集可能有什么问题？

```javascript
function buildBenchmark(bugs) {
  return bugs.map((b, i) => ({
    id: `B${i}`,
    codeVersion: b.parentCommit,          // 缺陷注入前的版本
    injectedBug: b.patch,
    expectedAssertion: b.regressionTest,  // 应检出的断言
    tags: b.tags,                         // 场景/框架标签
  }));
}
function scoreOnBenchmark(generatedTests, benchmark) {
  let killed = 0;
  for (const b of benchmark) {
    const test = generatedTests.find(t => t.target === b.id);
    if (test && test.assertion === b.expectedAssertion) killed++;
  }
  return { score: +(killed / benchmark.length).toFixed(2), killed, total: benchmark.length };
}
console.log(scoreOnBenchmark([{ target: 'B0', assertion: 'expect(price).toBe(9900)' }],
  buildBenchmark([{ parentCommit: 'abc', patch: 'off-by-one',
    regressionTest: 'expect(price).toBe(9900)', tags: ['支付'] }])));
// { score:1, killed:1, total:1 }
```
