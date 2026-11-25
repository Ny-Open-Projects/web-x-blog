---
title: [SCN-1248] AI 产品的模型幻觉缓解（不确定性表达）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1248：AI 产品的模型幻觉缓解（不确定性表达）

**答**：
- 缓解：模型输出置信度低时前端提示（"此回答可能不准确"），关键事实要求引用。
- 核实：事实类回答提供核实链接（搜索验证入口）。
- 教育：用户教育（AI 会犯错提示常驻）。

```javascript
// 幻觉缓解
function hallucinationGuard(answer, citations) {
  return {
    citationRequired: isFactual(answer) && !citations.length
      ? '事实类回答建议补充检索依据' : null,
    verify: searchVerifyLink(answer),                  // 核实入口
    banner: 'AI 可能生成不准确信息，请核实重要内容',
  };
}
function isFactual(a) { return /\d{4}|据报道|数据显示/.test(a); }
function searchVerifyLink(a) { return `/verify?q=${encodeURIComponent(a.slice(0, 50))}`; }
```
