---
title: [AIC-534] AI 测试生成的断言强度
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-534：AI 测试生成的断言强度

**答**:
- AI 生成测试的质量问题：1) **弱断言**（`expect(result).toBeDefined()`——只检查"存在"不检查"正确"——AI 倾向生成弱断言（"至少不会崩"的最低保障）；2) **边界缺失**（只测正常路径——不测空/null/异常/并发（RBL-518 边界条件的测试版）；3) **断言强度分级**：toBeDefined（弱）< toEqual（中）< toMatchObject+精确值（强）< 快照+边界（最强）；4) **AI 测试的评估**：断言强度评分（每个断言按强度打分）+ 边界覆盖率（测试了多少边界条件）。
- 提升 AI 测试质量的方法：1) **prompt 注入**（"测试必须包含空值、null、异常路径的用例"——RBL-506 prompt 的测试版）；2) **变异测试**（AI 写的测试 → 变异实现代码（改 `>` 为 `>=`）→ 测试应该 fail——不 fail = 断言太弱 RBL-587 的测试版；3) **人审测试的断言**（RBL-504 T1 的信任链——人审测试的断言强度而非实现）。
- 追问钩子：为什么「变异测试」是检测 AI 测试质量的最佳手段？——变异测试 = 自动验证"测试是否能检出 bug"（改变实现代码 → 测试应该 fail）；如果变异后测试仍然 pass = 断言太弱（测试"什么都能过"）；AI 写的测试的常见问题 = 弱断言（toBeDefined 而非精确值——变异后仍 pass）；「变异测试 = 测试的测试」——自动化验证测试质量（不需要人工审每个断言——变异器自动发现弱断言）。

```typescript
// AI 测试的断言强度评分
function scoreAssertion(assertion: string): number {
  if (/toBeDefined|toBeTruthy/.test(assertion)) return 1;         // 弱
  if (/toEqual|toStrictEqual/.test(assertion)) return 3;           // 中
  if (/toMatchObject|toBe\s*\(\s*\d|toBe\s*\(\s*['"]/.test(assertion)) return 5;  // 强：精确值
  if (/toBeGreaterThan|toBeLessThan|toHaveLength/.test(assertion)) return 4;      // 范围
  return 2;                                                        // 其他
}
// 边界覆盖检测
function checkEdgeCoverage(testCode: string) {
  const edgePatterns = [
    { pattern: /null|undefined/, name: 'null/undefined' },
    { pattern: /\[\]|\{\}/, name: 'empty' },
    { pattern: /toThrow|rejects/, name: 'error' },
    { pattern: /0\s*[,)]/, name: 'zero' },
    { pattern: /-?\d{4,}/, name: 'large-number' },
  ];
  return edgePatterns
    .filter(p => p.pattern.test(testCode))
    .map(p => p.name);                                   // 已覆盖的边界类型
}
// 变异测试验证
function mutationScore(mutations: { code: string; shouldFail: boolean }[], testFn: (code: string) => boolean) {
  let killed = 0;
  for (const m of mutations) {
    if (!testFn(m.code)) continue;                       // 变异后测试仍 pass = 逃逸
    killed++;
  }
  return { score: mutations.length ? +(killed / mutations.length * 100).toFixed(1) : 0,
    survived: mutations.length - killed };
}
```
