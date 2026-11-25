---
title: [AIC-601] AI 生成代码的上线前检查清单
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-601：AI 生成代码上线前检查

**答**:
- AI 代码上线前的综合检查清单（RBL-536 CI 门禁 + RBL-532 人审的综合）：1) **功能正确性**（测试通过 + 需求覆盖 RBL-565）；2) **安全性**（无注入/无敏感数据/权限校验——RBL-733/597）；3) **性能**（无 N+1/无不必要重渲染/内存无泄漏——RBL-578/680）；4) **可维护性**（可读性 RBL-588/命名 RBL-592/注释 RBL-514）；5) **合规**（Copyright RBL-572/License RBL-807/SBOM RBL-659）；6) **意图一致性**（需求覆盖 RBL-565/无意图漂移 RBL-538）。
- 检查清单的自动化程度：1) 全自动（lint/类型/测试/安全扫描——CI 门禁 RBL-536）；2) 半自动（性能分析需要 RUM 数据/意图覆盖需要需求文档）；3) 全人工（架构决策/领域知识验证——AI 无法替代 RBL-600）。
- 追问钩子：为什么「AI 代码的上线前检查」比「人写代码的上线前检查」多了「意图验证」这一步？——人写代码：写代码的过程 = 理解需求的过程（写的时候就在实现需求——代码即需求的实现）；AI 写代码：AI 基于 prompt 生成（prompt 可能不准确——AI 的理解可能偏离人的意图 RBL-538 漂移）；「意图验证的必要性」：AI 代码 = prompt 的实现而非需求的实现——需要验证 prompt→代码 的映射是否忠实于 需求→prompt 的映射（两层映射的一致性验证）。

```typescript
// AI 代码上线前综合检查
async function preReleaseCheck(code: string, context: {
  requirements: Requirement[]; testResults: TestResult[];
  securityScan: SecurityResult[]; rumMetrics?: Record<string, number>;
}) {
  const checks = [];
  // 1) 功能正确性
  checks.push({ check: 'tests', pass: context.testResults.allPass });
  // 2) 需求覆盖
  const coverage = requirementCoverage(context.requirements, code);
  checks.push({ check: 'requirements', pass: coverage.coverage >= 100, coverage: coverage.coverage });
  // 3) 安全
  checks.push({ check: 'security', pass: context.securityScan.every(s => s.severity !== 'error') });
  // 4) 性能（RUM 如有）
  if (context.rumMetrics) {
    checks.push({ check: 'performance', pass: context.rumMetrics.lcp < 2500 });
  }
  // 5) 可读性
  const readability = assessReadability(code);
  checks.push({ check: 'readability', pass: readability.readable });
  // 6) 版权
  const copyright = scanCopyright(code, []);
  checks.push({ check: 'copyright', pass: copyright.ok });
  return { checks, ok: checks.every(c => c.pass) };
}
```
