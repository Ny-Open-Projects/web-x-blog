---
title: [AIC-231] 「AI 生成的测试」要从哪些维度评估质量？为什么行覆盖率不够？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-231：「AI 生成的测试」要从哪些维度评估质量？为什么行覆盖率不够？
**答**：
- 断言强度：是否只断言「不抛错」，缺关键业务断言——行覆盖 100% 也可能无价值。
- 变异分数（mutation score）：用变异测试验证测试能否杀死变异体，AI 测试常见存活率过高。
- 独立性：是否依赖执行顺序/共享状态/flaky 网络行为。
- 可维护性：命名是否表达意图、是否有大量魔法值与脆弱快照。

```javascript
// 评估 AI 测试的三板斧
const assess = async (testFile: string) => ({
  mutation: await runStryker(testFile),      // 变异分数：核心指标
  assertions: countAssertionTypes(testFile), // 深断言 vs toBeDefined 类弱断言
  flaky: await runN(testFile, 10),           // 10 次通过率 < 100% 即 flaky
});
r
```
