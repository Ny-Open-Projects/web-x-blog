---
title: [TST-878] AI 生成测试的「版权与合规」风险如何管控？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-878：AI 生成测试的「版权与合规」风险如何管控？
**答**：
- 结论：AI 生成代码的版权/合规风险要靠「来源可追溯 + 许可证扫描 + 人工审查」管控，不能因为「是 AI 写的」就免责。
- 风险点：AI 可能复现训练数据中的受版权保护代码、引入不兼容许可证片段、泄漏内部敏感信息到外部模型。
- 管控：生成代码做license/相似度扫描（SCA）、敏感信息检查；企业版模型确保数据不用于训练。
- 流程：AI 产物标注「AI 生成」来源，纳入常规 code review，责任人与人工代码一视同仁。
- 追问钩子：AI 生成的一段测试代码与某开源项目的测试高度相似，你如何判定是「合理模式」还是「侵权」？

```javascript
// AI 生成产物的合规检查清单
function complianceCheck(generated) {
  const flags = [];
  if (generated.containsSecret) flags.push('疑似敏感信息，禁止外传模型');
  if (generated.licenseConflict) flags.push('许可证冲突，需替换');
  if (generated.similarity > 0.85) flags.push('与开源代码高度相似，人工审查');
  return {
    source: 'AI-generated', // 来源标注，纳入常规评审
    pass: flags.length === 0,
    flags,
  };
}
console.log(complianceCheck({ containsSecret: false,
  licenseConflict: false, similarity: 0.9 })); // 需人工审查
```
