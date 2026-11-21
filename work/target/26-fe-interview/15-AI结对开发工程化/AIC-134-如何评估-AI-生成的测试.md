---
title: [AIC-134] 如何评估 AI 生成的测试质量？「变异分数」怎么算、怎么用？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-134：如何评估 AI 生成的测试质量？「变异分数」怎么算、怎么用？
**答**：
- 传统指标（覆盖率）测不出「断言强度」；变异测试补上这一环：对源码做小变异（改条件、翻转布尔、改常量），看测试能否杀死变异体。
- 变异分数 = 被杀死的变异体 / 总变异体。AI 生成的测试常见短板：只断言不报错（变异后照样绿）、快照式断言（啥都能过）——变异分数会精准暴露。
- 实践用量：StrykerJS（JS/TS 生态）跑变异成本高（每个变异全量跑测试），建议只对核心模块、且用「抽样子集」策略（选 20 个变异体）做体检而非全量。
- 反馈循环：变异存活样本（测试没抓到的变异）直接说明测试缺口——把它回喂给 AI 要求补针对性断言，迭代到分数达标。
- 追问钩子：能说出「覆盖率测执行，变异测断言」并给成本控制策略，就是完整答案。

```javascript
// 变异算子示例 + 分数计算
const mutators = [
  src => src.replace(/===\s*0/g, '=== 1'),        // 常量替换
  src => src.replace(/&&/g, '||'),                 // 逻辑翻转
  src => src.replace(/return\s+(\w+)/, 'return -$1'), // 返回值取反
];
function mutationScore(src, tests, { sample = 20 } = {}) {
  const mutants = sampleMutants(src, mutators, sample);
  const killed = mutants.filter(m => runTests(tests, m) === 'FAIL').length;
  return { score: killed / mutants.length, threshold: 0.75 };
}
```
