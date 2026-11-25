---
title: [AIC-582] AI 代码的认知复杂度匹配
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-582：AI 代码的认知复杂度匹配

**答**:
- AI 代码的认知复杂度问题：1) **过简**（AI 生成"过度简化"的代码——忽略了业务复杂度（"10 行解决"但实际需要 100 行——AI 的简化与业务需求不匹配 RBL-507 幻觉的简化维度）；2) **过繁**（AI 生成"过度工程"的代码——不必要的抽象/设计模式/防御性编程（"100 行解决 10 行的事"——AI 的过度工程 RBL-522 规范违背的反向）；3) **匹配**：代码的认知复杂度 = 业务复杂度（简陋业务 + 简陋代码 = 好；复杂业务 + 复杂代码 = 好——"匹配"而非"越简越好"或"越繁越好"）。
- 认知复杂度的度量：Cognitive Complexity（SonarSource 的度量——嵌套深度 × 条件数量 = 认知负担；不是圈复杂度（CC 计算分支数——认知复杂度计算"人理解有多难"）；「认知复杂度 > 15 = 需要重构」。
- 追问钩子：为什么「AI 生成的代码」的认知复杂度经常与业务不匹配？——AI 的"复杂度校准"基于训练数据的分布（简单 demo 多、复杂业务少——AI 倾向生成简单代码）；业务复杂度 > AI 默认复杂度 → AI "过度简化"（漏了业务逻辑——用户需求没完全实现）；「复杂度匹配的验证」：对比"AI 代码的认知复杂度"与"类似人写代码的认知复杂度"——差异大 = AI 的复杂度与项目不匹配（需要 prompt 校准 RBL-506）。

```typescript
// 认知复杂度计算（简化版 SonarSource）
function cognitiveComplexity(code: string): number {
  let complexity = 0; let nesting = 0;
  const keywords = /\b(if|else\s+if|for|while|catch|&&|\|\||\?)\b/g;
  const nestingKeywords = /\b(if|for|while|switch|try)\b/g;
  // 按行扫描
  code.split('\n').forEach((line) => {
    const trimmed = line.trim();
    // 嵌套深度检测（缩进作为近似）
    const indent = (line.match(/^\s*/)?.[0].length ?? 0) / 2;
    nesting = indent;
    // 条件/循环/catch 加分
    for (const m of line.matchAll(/\b(if|for|while|catch)\b/g)) {
      complexity += 1 + nesting;                     // 嵌套越深越复杂
    }
    // 逻辑运算符
    for (const m of line.matchAll(/&&|\|\|/g)) {
      complexity += 1;
    }
    // 三元
    for (const m of line.matchAll(/\?[^:]*:/g)) {
      complexity += 1;
    }
  });
  return complexity;
}
```
