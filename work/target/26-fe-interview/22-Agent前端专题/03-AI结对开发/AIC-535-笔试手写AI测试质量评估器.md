---
title: [AIC-535] 笔试：手写 AI 测试质量评估器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-535：笔试：手写 AI 测试质量评估

**答**：实现 `assessTestQuality(testCode)`。规则：1) **断言强度**：提取所有 expect() 行——每行按强度评分（RBL-534）；平均分 = 断言质量分；2) **边界覆盖**：检测 null/empty/error/zero/large 边界的测试用例——覆盖数 = 边界覆盖分；3) **弱断言检测**：toBeDefined/toBeTruthy 的比例（> 50% = 'weak-assertions' 告警）；4) **综合评分**：断言分 × 0.4 + 边界分 × 0.3 + 强度比 × 0.3（0~100 分）。5) 返回 `{ assertionAvg, edgeCoverage, weakRatio, score, verdict }`。边界：无 expect（score 0——"没有断言的测试不是测试"）；无测试代码（no-data）；全弱断言（score 极低）。

```javascript
function assessTestQuality(testCode = '') {
  const expects = testCode.match(/expect\s*\([^)]*\)[\s\S]*?;/g) ?? [];
  if (!expects.length && !testCode.trim())
    return { noData: true, assertionAvg: 0, edgeCoverage: [], weakRatio: 0, score: 0, verdict: null };
  // 断言强度
  const scores = expects.map(exp => {
    if (/toBeDefined|toBeTruthy/.test(exp)) return 1;
    if (/toEqual|toStrictEqual/.test(exp)) return 3;
    if (/toMatchObject|toBe\s*\(\s*\d|toBe\s*\(\s*['"]/.test(exp)) return 5;
    if (/toBeGreaterThan|toBeLessThan|toHaveLength/.test(exp)) return 4;
    return 2;
  });
  const assertionAvg = expects.length
    ? +(scores.reduce((s, x) => s + x, 0) / scores.length).toFixed(1) : 0;
  // 边界覆盖
  const edges = [
    { pattern: /null|undefined/i, name: 'null' },
    { pattern: /\[\]|\{\}/, name: 'empty' },
    { pattern: /toThrow|rejects/i, name: 'error' },
    { pattern: /\b0\b/, name: 'zero' },
  ];
  const edgeCoverage = edges.filter(e => e.pattern.test(testCode)).map(e => e.name);
  // 弱断言比例
  const weak = expects.filter(exp => /toBeDefined|toBeTruthy/.test(exp)).length;
  const weakRatio = expects.length ? +(weak / expects.length * 100).toFixed(1) : 0;
  // 综合分
  const assertionScore = Math.min(10, assertionAvg) / 10 * 40;
  const edgeScore = edgeCoverage.length / 4 * 30;
  const strengthScore = expects.length ? ((100 - weakRatio) / 100) * 30 : 0;
  const score = Math.round(assertionScore + edgeScore + strengthScore);
  const verdict = !expects.length ? 'no-assertions'
    : score >= 70 ? 'good' : score >= 40 ? 'moderate' : 'weak';
  return { assertionAvg, edgeCoverage, weakRatio, score, verdict };
}

// 自测
const goodTest = `
  it('handles normal case', () => {
    expect(validate('user@test.com')).toEqual({ valid: true, domain: 'test.com' });
    expect(validate('a@b.com')).toBe(5);
  });
  it('handles null', () => {
    expect(validate(null)).toEqual({ valid: false });
  });
  it('handles empty', () => {
    expect(validate('')).toThrow();
  });
  it('handles zero', () => {
    expect(validate(0)).toEqual({ valid: false });
  });
`;
let r = assessTestQuality(goodTest);
console.log(r.score >= 70 && r.verdict === 'good');
console.log(r.edgeCoverage.join(',').length > 0);         // null+empty+error+zero
console.log(r.weakRatio === 0);                          // 无弱断言

// 弱断言测试
const weakTest = `
  it('test', () => {
    expect(validate('x')).toBeDefined();
    expect(validate(null)).toBeTruthy();
  });
`;
r = assessTestQuality(weakTest);
console.log(r.weakRatio === 100);
console.log(r.verdict === 'weak');

// 无断言
r = assessTestQuality('const x = 1;');
console.log(r.verdict === 'no-assertions' && r.score === 0);
// 空
console.log(assessTestQuality('').noData === true);
```

**评分点**：
- 断言强度四级评分（弱 1/中 3/范围 4/强 5）；边界覆盖四类检测
- weakRatio 告警（> 50% 弱断言 = AI 测试质量问题 RBL-534）；综合分公式
- 边界（无断言 no-assertions/空 no-data/全弱断言 weak）；verdict 三级
- 能说清「AI 测试的质量评估 = 断言强度 × 边界覆盖 × 弱断言比例——弱断言的变异测试检测」属于加分
