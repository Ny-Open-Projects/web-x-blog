---
title: [AIC-979] AI Review 的反馈经常是「这里可能有性能问题」这种空话，如何让反馈变得「可操作」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-979：AI Review 的反馈经常是「这里可能有性能问题」这种空话，如何让反馈变得「可操作」？
**答**：
- 可操作的反馈必须包含「三要素」：具体问题（哪行、什么风险）+ 证据（为什么判断，如复杂度的量化）+ 建议改法（给出可直接用的修改方案）——结论：只抛问题不给方案等于制造负担。
- 让 AI 产出时强制结构化输出：问题定位、严重级别、理由、修复建议代码片段；评审系统按模板渲染，缺字段的报告不展示。
- 给反馈配「一键采纳/忽略」：建议能直接生成 patch 让开发者一键应用，降低修复成本；忽略时收集理由反哺规则。
- 追问钩子：能提出「可操作性可用『处置率与采纳后修改率』度量——建议被直接采纳说明够具体」的候选人，用行为数据验证反馈质量。

```typescript
// 结构化可操作反馈
function renderReview(r) {
  const missing = ['location','severity','evidence','suggestion'].filter(k=>!r[k]);
  if (missing.length) return null; // 缺字段不展示，逼迫产出完整
  return {
    title:`[${r.severity}] ${r.location}: ${r.issue}`,
    why:r.evidence,
    patch:r.suggestion, // 可直接应用的修改
  };
}
console.log(renderReview({
  location:'List.tsx:42', severity:'warn', issue:'列表内重复计算',
  evidence:'每次渲染执行 O(n) 过滤，n 可达 1000', suggestion:'用 useMemo 缓存结果',
}));
```
