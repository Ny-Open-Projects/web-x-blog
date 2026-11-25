---
title: [AIC-741] AI 质量工程中的质量左移如何从 PR 阶段前移到需求阶段
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-741：AI 质量工程中的质量左移如何从 PR 阶段前移到需求阶段

**答**：
- 结论先行：质量左移 = 把质量活动从「PR 后审查」提前到「需求澄清 → 方案设计 → prompt 编写」——越早发现缺陷，修复成本越低；AI 时代尤其重要，因为错误需求会被 AI 高效放大成错误代码。
- 左移的三个抓手：1) 需求阶段定义可机器验证的验收标准；2) 方案阶段让 AI 做「威胁建模」预判风险；3) prompt 阶段内置质量约束（禁用 API、边界要求）。
- 与传统的区别：传统左移是「测试提前」，AI 左移是「约束前置」——把质量要求写进 AI 的输入，而不是事后检查输出。
- 追问钩子：为什么「错误需求 + AI」比「错误需求 + 人工」危害更大？——AI 会以极高效率把错误理解扩散到多个文件，返工面呈指数放大。

```javascript
// 质量左移：需求阶段就定义可验证验收，作为 AI 生成的硬约束
function shiftLeft(requirement) {
  return {
    acceptance: requirement.acceptance.map(a => ({ desc: a, testable: /should|must|返回|显示/.test(a) })),
    constraints: ['禁止 mock 真实接口', '必须处理空态'],
    prompt: `实现需求：${requirement.desc}\n约束：禁止 mock 真实接口；必须处理空态`,
  };
}
const r = shiftLeft({ desc: '商品列表', acceptance: ['无货时应显示无货', '好看一点'] });
console.log(r.acceptance.map(a => a.testable)); // [true, false] → 不可测项需澄清
```
