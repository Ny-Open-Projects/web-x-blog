---
title: [AIC-532] 人审 AI 代码的核心检查点
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-532：人审 AI 代码的核心检查点

**答**:
- 人审 AI 代码的检查点体系（RBL-501 Navigator 角色的操作化）：1) **意图验证**（AI 是否理解了需求——"我要分页，AI 给了无限滚动" = 意图错误；2) **边界条件**（空值/null/空数组/并发——AI 常忽略边界条件（"边界测试" RBL-518）；3) **副作用**（网络请求/状态修改/全局变量——AI 可能引入意外副作用；4) **安全**（注入/越权/敏感数据——RBL-733 安全清单；5) **性能**（N+1/内存泄漏/不必要的重渲染——RBL-542）；6) **一致性**（与项目现有代码风格/模式一致——命名/架构/错误处理模式）。
- 审查的优先级排序：意图 > 安全 > 边界 > 副作用 > 性能 > 一致性——「意图错误 = 全部重写（最高成本）；一致性 = 微调（最低成本）」。
- 追问钩子：为什么「意图验证」是人审 AI 代码的第一优先级？——意图错误 = AI 做了错的事（不是做错了事——是做了不该做的事）；边界/安全/性能错误 = 可以在正确意图上修复（修 bug）；意图错误 = 修不了（方向错了——需要推翻重来）；「意图验证的效率」：读 AI 代码的第一分钟判断"这是不是我想要的"——是 → 继续审细节；否 → 立即停止重新 prompt（避免在错误方向上浪费时间审查细节）。

```typescript
// AI 代码审查清单（人审检查点）
const REVIEW_CHECKPOINTS = [
  { priority: 1, check: 'intent', question: 'AI 是否理解了需求？', cost: 'rewrite' },
  { priority: 2, check: 'security', question: '有无注入/越权/敏感数据？', cost: 'fix' },
  { priority: 3, check: 'edge-cases', question: '空值/null/并发处理了吗？', cost: 'fix' },
  { priority: 4, check: 'side-effects', question: '有无意外副作用？', cost: 'fix' },
  { priority: 5, check: 'performance', question: 'N+1/内存/渲染问题？', cost: 'optimize' },
  { priority: 6, check: 'consistency', question: '与项目模式一致吗？', cost: 'refine' },
];
// 审查流程：按优先级逐步深入
function reviewAICode(aiOutput: string, intent: string) {
  // 1) 意图验证（1 分钟）
  const intentMatch = doesIntentMatch(aiOutput, intent);
  if (!intentMatch) return { verdict: 'reject', reason: '意图不匹配——重新 prompt' };
  // 2) 安全扫描（30 秒）
  const securityIssues = scanSecurity(aiOutput);
  if (securityIssues.length) return { verdict: 'reject', reason: '安全问题', issues: securityIssues };
  // 3) 边界条件（2 分钟）
  const edgeCases = checkEdgeCases(aiOutput);
  // 4) 通过 → 细节审
  return { verdict: 'approve-with-notes', edgeCases };
}
```
