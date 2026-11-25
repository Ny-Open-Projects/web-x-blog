---
title: [AIC-604] AI 代码的 Test Coverage 缺口分析
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-604：AI 代码的测试缺口分析

**答**:
- AI 生成代码的测试缺口分析：1) **函数级缺口**（哪些导出函数没有对应的测试——`getUser` 函数存在但无 `getUser.test`—— uncovered function RBL-655 金字塔的缺口层；2) **边界级缺口**（函数有测试但不覆盖边界——null/empty/error 路径未测试（RBL-535 边界覆盖的缺口检测）；3) **集成级缺口**（函数有单测但与其他函数的组合未测试——`getUser + updateProfile` 的交互未测；4) **AI 的缺口特征**：AI 倾向生成"正常路径"测试——边界路径和错误路径的覆盖不足（RBL-534 断言强度的边界维度）。
- 缺口的分析方法：1) **函数-测试映射**（源码函数 → 测试函数的映射——`getUser` → `getUser.test.ts` 中的 test 块）；2) **覆盖率工具**（Istanbul/c8 的行覆盖+分支覆盖——分支覆盖 = 边界覆盖的度量；3) **缺口的优先级排序**（导出函数 > 内部函数、核心逻辑 > 辅助函数——修复的优先级）。
- 追问钩子：为什么「AI 生成代码的测试缺口」需要「边界级缺口分析」而不只是「函数级覆盖率」？——函数级覆盖率 100% = 每个函数都有测试 → 但测试可能只覆盖正常路径（"happy path test"——`getUser(1)` 有测试但 `getUser(null)` 没有）；AI 生成的测试倾向于 happy path（RBL-534 弱断言的边界维度）→ 函数覆盖率 100% 但分支覆盖率可能只有 50%；「分支覆盖 = 边界覆盖的代理指标」：if/else 的每个分支都测试了 = 边界条件覆盖了——分支覆盖率 < 80% = 有未测试的边界路径。

```typescript
// 测试缺口分析
interface TestGap {
  type: 'uncovered-function' | 'missing-edge-cases' | 'missing-integration';
  target: string;
  priority: number;                                    // 1 高
}
function analyzeTestGaps(sourceCode: string, testCode: string, coverage: { lines: number; branches: number }) {
  const gaps: TestGap[] = [];
  // 1) 函数级缺口
  const exportedFns = [...sourceCode.matchAll(/export\s+(?:async\s+)?function\s+(\w+)/g)].map(m => m[1]);
  for (const fn of exportedFns) {
    if (!testCode.includes(fn))
      gaps.push({ type: 'uncovered-function', target: fn, priority: 1 });
  }
  // 2) 边界级缺口（分支覆盖率低）
  if (coverage.branches < 80)
    gaps.push({ type: 'missing-edge-cases', target: `${coverage.branches}% branches`, priority: 1 });
  // 3) 集成级缺口（多函数但无集成测试）
  if (exportedFns.length > 3 && !testCode.includes('integration'))
    gaps.push({ type: 'missing-integration', target: 'multi-function', priority: 2 });
  return gaps.sort((a, b) => a.priority - b.priority);
}
```
