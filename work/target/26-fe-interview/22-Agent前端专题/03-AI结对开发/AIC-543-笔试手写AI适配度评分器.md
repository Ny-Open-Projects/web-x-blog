---
title: [AIC-543] 笔试：手写 AI 适配度评分器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-543：笔试：手写 AI 适配度评分器

**答**：实现 `aiReadinessScore(project)`。project: `{ language: 'ts'|'js', strict?: boolean, hasSchema: boolean, framework: 'react'|'vue'|'angular'|'svelte', hasComments: boolean, hasTests: boolean }`. 规则：1) **评分维度**（每项 0~20 分，总分 100）：language：ts=20, js=0；strict：true=20, false=10, 无 strict=0（仅 ts）；hasSchema：true=20, false=0；framework：react=20, svelte=15, vue=10, angular=5（训练数据量）；hasComments+hasTests：各 10；2) **分级**：≥ 80 'ai-ready'（AI 补全质量高）；≥ 50 'partial'（需要改进）；< 50 'low'（AI 补全质量差——先加类型/schema）；3) 返回 `{ score, level, suggestions: string[] }`（建议按缺失项排序）。边界：language=js 且 strict=true（不加分——JS 无 strict 概念）；framework 未知值（0 分）；空 project。

```javascript
function aiReadinessScore(project = {}) {
  const p = { language: 'js', strict: false, hasSchema: false,
    framework: 'unknown', hasComments: false, hasTests: false, ...project };
  let score = 0; const suggestions = [];
  // language
  if (p.language === 'ts') score += 20;
  else { suggestions.push('迁移到 TypeScript（最大杠杆——类型 = AI 约束）'); }
  // strict
  if (p.language === 'ts') {
    if (p.strict) score += 20;
    else { score += 10; suggestions.push('开启 strict 模式'); }
  }
  // schema
  if (p.hasSchema) score += 20;
  else suggestions.push('添加 zod/OpenAPI schema（数据契约 = AI 的数据约束）');
  // framework
  const fwScores = { react: 20, svelte: 15, vue: 10, angular: 5 };
  score += fwScores[p.framework] ?? 0;
  if ((fwScores[p.framework] ?? 0) < 15)
    suggestions.push(`框架 ${p.framework} 的 AI 训练数据较少——考虑文档增强`);
  // comments + tests
  if (p.hasComments) score += 10; else suggestions.push('添加意图注释（RBL-514 注释即 Prompt）');
  if (p.hasTests) score += 10; else suggestions.push('添加测试（Agent 的传感器 RBL-518）');
  const level = score >= 80 ? 'ai-ready' : score >= 50 ? 'partial' : 'low';
  return { score, level, suggestions };
}

// 自测
// 最佳适配栈：React + TS strict + schema + comments + tests
let r = aiReadinessScore({ language: 'ts', strict: true, hasSchema: true,
  framework: 'react', hasComments: true, hasTests: true });
console.log(r.score === 100 && r.level === 'ai-ready');

// 最差：JS 无 schema 无注释无测试
r = aiReadinessScore({ language: 'js', framework: 'angular' });
console.log(r.score < 30 && r.level === 'low');
console.log(r.suggestions.some(s => s.includes('TypeScript')));
console.log(r.suggestions.some(s => s.includes('schema')));

// TS 但无 strict
r = aiReadinessScore({ language: 'ts', strict: false, hasSchema: true,
  framework: 'react', hasComments: true, hasTests: true });
console.log(r.score === 90);                           // strict 只给 10
console.log(r.suggestions.some(s => s.includes('strict')));

// JS strict=true 不加分
r = aiReadinessScore({ language: 'js', strict: true, hasSchema: false,
  framework: 'angular', hasComments: false, hasTests: false });
console.log(r.score === 5);                            // 只有 angular 5 分
// 空
r = aiReadinessScore({});
console.log(r.score === 0 && r.level === 'low');
```

**评分点**：
- 六维评分（language/strict/schema/framework/comments/tests——各 20/20/20/20/10/10 分）；suggestions 按缺失项
- framework 的 AI 友好度排序（react > svelte > vue > angular——训练数据量映射）；JS strict 不加分
- 边界（最佳栈 100 分/最差栈低分/空 project/JS strict 忽略）；建议的可执行性
- 能说清「AI 补全质量 = 类型约束 × 训练数据 × 注释质量——TS strict 是最大杠杆（类型 = AI 的护栏）」属于加分
