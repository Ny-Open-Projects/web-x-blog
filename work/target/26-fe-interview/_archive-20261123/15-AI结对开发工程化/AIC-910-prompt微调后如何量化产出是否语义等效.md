---
title: [AIC-910] prompt 微调了一个词后，如何量化「新旧产出是否语义等效」，而不是靠人肉读几段代码？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-910：prompt 微调了一个词后，如何量化「新旧产出是否语义等效」，而不是靠人肉读几段代码？
**答**：
- 分层判断：先做「结构层」比对（AST 是否同构、导出 API 是否一致），再做「行为层」比对（同一组输入输出是否一致），最后才是「语义层」抽样人工评审。
- 量化指标可用：AST 相似度、测试通过率、快照差异率、关键 API 签名一致率——结论：用一组指标而非单一分数，避免被单一指标误导。
- 语义等效是「针对给定测试集的等效」，不是绝对等效；要承认覆盖率盲区，对高风险变更保留人工评审。
- 追问钩子：能指出「等效性必须绑定测试集与评估维度，脱离评估范围的等效是伪命题」的候选人，具备严谨的度量观。

```typescript
// 多维等效性评分
function equivalence(before, after, cases) {
  const apiSame = JSON.stringify(Object.keys(before).sort()) === JSON.stringify(Object.keys(after).sort());
  const behavior = cases.filter(c => safeRun(before, c) === safeRun(after, c)).length / cases.length;
  const astSame = normalize(before.toString()) === normalize(after.toString());
  return { apiSame, behavior:+behavior.toFixed(2), astSame,
    equivalent: apiSame && behavior === 1 };
}
function safeRun(fn, c){ try { return JSON.stringify(fn(c)); } catch { return 'ERR'; } }
function normalize(s){ return s.replace(/\s+/g,''); }
// 结论：equivalent 只针对给定 cases，覆盖盲区仍需人工评审
```
