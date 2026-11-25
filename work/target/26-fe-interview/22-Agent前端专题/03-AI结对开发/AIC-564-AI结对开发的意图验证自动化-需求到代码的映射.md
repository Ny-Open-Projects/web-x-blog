---
title: [AIC-564] 需求到代码的映射验证
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-564：需求到代码的映射验证

**答**:
- 需求到代码的自动化验证（RBL-538 意图漂移的工程化）：1) **需求的结构化**（用户故事 → Given/When/Then 格式——可映射到测试用例的声明式需求 RBL-518 Agent 分解器的需求版）；2) **代码 → 需求的反向追踪**（生成的代码中有多少 Given/When/Then 被覆盖——需求覆盖率；3) **映射验证**：每条需求 → 对应的代码标识（函数名/测试名——"需求 1.2 → test_user_can_login"）——映射矩阵 = 需求与代码的双向追踪。
- 映射的自动化实现：1) **需求解析**（Given/When/Then → 结构化对象——`{ given: 'user is logged in', when: 'clicks submit', then: 'redirects to dashboard' }`）；2) **代码匹配**（代码中搜索与 GWT 对应的函数名/条件/断言——正则或 AST 匹配 RBL-538 的映射版）；3) **映射矩阵**：需求 × 代码的覆盖表（每行 = 一条需求、每列 = 一个代码标识——交叉点 = 匹配状态）。
- 追问钩子：为什么「需求到代码的映射」是 AI 结对的核心验证手段？——AI 生成的代码可能"看起来对"但"缺少某个需求的功能"（意图漂移 RBL-538 的自动化检测）；映射矩阵 = 需求覆盖的量化（覆盖率 < 100% = 有需求未实现）；映射的自动化 = 人不需要逐条比对需求与代码（工具自动匹配——人的审查聚焦在"映射了但实现不对"的项）。

```typescript
// 需求结构化（Given/When/Then）
interface Requirement {
  id: string;
  given: string; when: string; then: string;
  keywords: string[];                                  // 自动提取的匹配关键词
}
function parseRequirement(text: string, id: string): Requirement {
  const given = /Given\s+(.+?)(?:\s+When|$)/i.exec(text)?.[1] ?? '';
  const when = /When\s+(.+?)(?:\s+Then|$)/i.exec(text)?.[1] ?? '';
  const then = /Then\s+(.+)/i.exec(text)?.[1] ?? '';
  const keywords = [...`${given} ${when} ${then}`.toLowerCase().match(/\w{3,}/g) ?? []];
  return { id, given, when, then, keywords };
}
// 需求覆盖检测
function checkRequirementCoverage(requirements: Requirement[], code: string) {
  return requirements.map(req => {
    const matched = req.keywords.filter(k => code.toLowerCase().includes(k));
    return { id: req.id, covered: matched.length >= Math.ceil(req.keywords.length * 0.5),
      matchedKeywords: matched };
  });
}
```
