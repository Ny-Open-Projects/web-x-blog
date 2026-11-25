---
title: [AIC-536] AI 代码的自动化质量门禁
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-536：AI 代码的自动化质量门禁

**答**:
- AI 代码的 CI 门禁流水线（RBL-536 扩展）：1) **幻觉检测门禁**（依赖幻觉 + API 幻觉 RBL-507/508——编译+构建即可检出）；2) **测试质量门禁**（断言强度 + 边界覆盖 RBL-535——弱断言的测试不通过）；3) **规范一致性门禁**（provenance 驱动——AI 代码的规范违规 = error（RBL-523）；4) **安全扫描门禁**（敏感数据/注入——RBL-762 产物审计）；5) **信任分级门禁**（T0 路径强制人工审——RBL-505）。
- 门禁的流程编排（RBL-631 PR 流水线）：幻觉检测（编译）→ 规范审计（lint）→ 测试质量评估（AST 分析）→ 安全扫描（模式匹配）→ 信任路由（分级审批）——「五段门禁」每段的失败即阻断。
- 追问钩子：为什么「AI 代码的质量门禁」需要「额外的门禁」（而非仅用传统 CI）？——传统 CI（编译/测试/lint）检查「代码是否正确运行」；AI 代码的额外风险 = 幻觉（不存在的依赖/API）/ 规范违规（AI 不遵守团队规范）/ 测试质量（AI 写的弱断言测试通过但不检出 bug）；「传统 CI 的盲区」：编译通过的幻觉依赖（typosquatting 包名——编译不报但运行时崩）；传统 lint 不检查断言强度；「AI 代码的 CI = 传统 CI + AI 专属门禁」——幻觉检测/测试质量/信任分级是新增的门禁段。

```typescript
// AI 代码的 CI 门禁编排
async function aiCodeGate(pr, { pipeline } = {}) {
  const results = {};
  // 1) 幻觉检测（编译+依赖审计）
  results.hallucination = await runHallucinationCheck(pr);
  // 2) 规范一致性（lint + provenance）
  results.styleConsistency = await runStyleAudit(pr);
  // 3) 测试质量（AST 断言强度分析）
  results.testQuality = await runTestQualityCheck(pr);
  // 4) 安全扫描
  results.security = await runSecurityScan(pr);
  // 5) 信任分级路由
  results.trustRouting = routeReview(pr, config);
  const ok = Object.values(results).every(r => r.ok !== false);
  return { ok, results, action: ok ? results.trustRouting?.action : 'blocked' };
}
// 门禁的阻断规则
// hallucination.ok === false → 阻断（幻觉依赖 = 必须修）
// testQuality.verdict === 'weak' → 阻断（弱断言测试不可信）
// trustRouting.action === 'manual-review-required' → 阻断（T0 人工审）
```
