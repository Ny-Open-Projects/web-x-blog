---
title: [TST-964] 大家都在说「AI 生成测试的质量」，为什么还要单独谈「可靠性」？两者有何不同？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-964：大家都在说「AI 生成测试的质量」，为什么还要单独谈「可靠性」？两者有何不同？
**答**：
- 结论：质量看「单次产物好不好」（语法对、断言合理），可靠性看「反复运行稳不稳、长期维护久不久」——好质量不等于高可靠性。
- 可靠性三维度：确定性（同样输入结果一致）、稳定性（不 flaky）、可维护性（代码变更后存活率高）。
- 为何单列：AI 用例常见问题正是「首次看着不错，跑几次就飘、改次代码就废」，这正是可靠性问题而非质量问题。
- 追问钩子：一个 AI 用例首次运行通过、覆盖率也涨了，但一周后 80% 的 AI 用例都失效了，这是质量问题还是可靠性问题？你怎么度量？

```javascript
const RELIABILITY_DIMS = {
  determinism: results => new Set(results).size === 1, // 多次运行结果一致
  stability: flakes => flakes / results.length < 0.01,
  maintainability: (survived, total) => survived / total > 0.8,
};
function reliabilityReport({ runs, flakeCount, survived, total }) {
  const results = runs.map(r => JSON.stringify(r));
  return {
    determinism: RELIABILITY_DIMS.determinism(results),
    stability: RELIABILITY_DIMS.stability(flakeCount, runs.length),
    maintainability: RELIABILITY_DIMS.maintainability(survived, total),
  };
}
console.log(reliabilityReport({
  runs: [{ pass: true }, { pass: true }], flakeCount: 0, survived: 9, total: 10,
})); // { determinism:true, stability:true, maintainability:true }
```
